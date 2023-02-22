

from django.urls import path

from users_pc.views import UsersPCView, UsersComponentView

urlpatterns = [
    path('user-pc/', UsersPCView.as_view(),),
    path('user-pc/component', UsersComponentView.as_view(),),
]