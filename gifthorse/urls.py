"""
URL configuration for gifthorse project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from main_app import views
from main_app.views import GiftViewSet, OccasionViewSet, RecipientViewSet, RecipientOccasionsView, GiftsForOccasionAndRecipient

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'gifts', GiftViewSet)
router.register(r'occasions', OccasionViewSet)
router.register(r'recipients', RecipientViewSet)

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name ='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name ='token_refresh'),
    path('home/', views.HomeView.as_view(), name ='home'),
    path('logout/', views.LogoutView.as_view(), name ='logout'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('recipient-occasions/<int:recipient_id>/', RecipientOccasionsView.as_view(), name='recipient-occasions'),
    path('gifts-for-occasion/<int:occasion_id>/recipient/<int:recipient_id>/', GiftsForOccasionAndRecipient.as_view(), name='gifts-for-occasion-recipient'),


]
