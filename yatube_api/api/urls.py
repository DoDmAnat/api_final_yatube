from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

jwt_patterns = [
    path('jwt/create/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

v1_router = DefaultRouter()
v1_router.register('posts', PostViewSet)
v1_router.register('groups', GroupViewSet)
v1_router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet,
                   basename='comments')
v1_router.register('follow', FollowViewSet, basename='followers')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/', include(jwt_patterns)),
]
