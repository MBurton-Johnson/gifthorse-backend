from django.contrib.auth.models import User, Group
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, status
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer, GroupSerializer, UserRegistrationSerializer, GiftSerializer, RecipientSerializer, OccasionSerializer
from .models import Gift, Recipient, Occasion


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class HomeView(APIView):
   permission_classes = (IsAuthenticated, )
   def get(self, request):
       content = {'message': 'Welcome to the JWT Authentication page using React Js and Django!'}
       return Response(content)

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class UserRegistrationView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    # permission_classes = [AllowAny]

class GiftViewSet(viewsets.ModelViewSet):
    queryset = Gift.objects.all()
    serializer_class = GiftSerializer

    def create(self, request, *args, **kwargs):
        print("Request Data:", request.data)  # Log the incoming request data
        response = super().create(request, *args, **kwargs)
        if response.status_code == 400:
            print("Error Details:", response.data)  # This will log the detailed error
        return response

class RecipientViewSet(viewsets.ModelViewSet):
    queryset = Recipient.objects.all()
    serializer_class = RecipientSerializer

class OccasionViewSet(viewsets.ModelViewSet):
    queryset = Occasion.objects.all()
    serializer_class = OccasionSerializer

    def create(self, request, *args, **kwargs):
        print(request.data)  # Debugging: print incoming data
        return super().create(request, *args, **kwargs)
    
class RecipientOccasionsView(APIView):
    def get(self, request, recipient_id):
        recipient = get_object_or_404(Recipient, pk=recipient_id)
        gifts = Gift.objects.filter(recipient=recipient)

        # Get unique occasions associated with these gifts
        occasions = Occasion.objects.filter(gift__in=gifts).distinct()

        serializer = OccasionSerializer(occasions, many=True)
        return Response(serializer.data)

class GiftsForOccasionAndRecipient(ListAPIView):
    serializer_class = GiftSerializer

    def get_queryset(self):
        recipient_id = self.kwargs['recipient_id']
        occasion_id = self.kwargs['occasion_id']
        return Gift.objects.filter(recipient_id=recipient_id, occasion_id=occasion_id)
