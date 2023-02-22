
from django.urls import path

from pc_components.views import ComponentListView,ComponentDetailedView, ComponentCreateView

urlpatterns = [
    path('components/', ComponentListView.as_view()),
    path('component/', ComponentCreateView.as_view()),
    path('component/<str:pk>',ComponentDetailedView.as_view()),
]