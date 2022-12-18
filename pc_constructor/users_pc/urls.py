
from .views import UserPcView, UserMonitorView, UserMonitorDestroyView, UserPcDeleteView, VideoCardView, \
    VideoCardDeleteView
from django.urls import path

urlpatterns = [
    path('api/user-pc/', UserPcView.as_view(),),
    path('api/user-pc-delete/<str:pk>', UserPcDeleteView.as_view(), ),
    path('api/users-create-monitor', UserMonitorView.as_view(),),
    path('api/users-delete-monitor/<str:pk>', UserMonitorDestroyView.as_view(),),
    path('api/users-create-videocard', VideoCardView.as_view(),),
    path('api/users-delete-videocard/<str:pk>', VideoCardDeleteView.as_view(),),
]