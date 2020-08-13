from django.urls import path, include
from .views import HelloApiView, HelloViewSet,UserProfileViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('hello-viewset', HelloViewSet, base_name='hello-viewset')
router.register('profile',UserProfileViewSet)

urlpatterns = [
    path('hello-view/',HelloApiView.as_view()),
    path('', include(router.urls)),
]
