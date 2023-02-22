
from .views import UserPcView, UserMonitorView, UserMonitorDestroyView, UserPcDeleteView, VideoCardView, \
    VideoCardDeleteView, UserProcessorView, UserProcessorDeleteView, UserMotherBoardView, UserMotherBoardDeleteView, \
    UserDriveDiskView, UserDriveDiskDeleteView, UserRAMView, UserRAMDeleteView
from django.urls import path

urlpatterns = [
    path('api/user-pc/', UserPcView.as_view(),),
    path('api/user-pc-delete/<str:pk>', UserPcDeleteView.as_view(), ),
    path('api/users-create-monitor', UserMonitorView.as_view(),),
    path('api/users-delete-monitor/<str:pk>', UserMonitorDestroyView.as_view(),),
    path('api/users-create-videocard', VideoCardView.as_view(),),
    path('api/users-delete-videocard/<str:pk>', VideoCardDeleteView.as_view(),),
    path('api/users-create-processor', UserProcessorView.as_view(), ),
    path('api/users-delete-processor/<str:pk>', UserProcessorDeleteView.as_view(), ),
    path('api/users-create-motherboard', UserMotherBoardView.as_view(), ),
    path('api/users-delete-motherboard/<str:pk>', UserMotherBoardDeleteView.as_view(), ),
    path('api/users-create-drive', UserDriveDiskView.as_view(), ),
    path('api/users-delete-drive/<str:pk>', UserDriveDiskDeleteView.as_view(), ),
    path('api/users-create-ram', UserRAMView.as_view(), ),
    path('api/users-delete-ram`/<str:pk>', UserRAMDeleteView.as_view(), ),
]