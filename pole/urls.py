from django.urls import path

from .views import (
    PoleListView,
    PoleUpdateView,
    PoleDeleteView,
    PoleCreateView,
    PoleCreateImageView,
    PoleDetailView,
)
urlpatterns = [
    path('<int:pk>/edit/', PoleUpdateView.as_view(), name='pole_edit'),
    path('<int:pk>/', PoleDetailView.as_view(), name='pole_detail'),
    path('<int:pk>/delete/', PoleDeleteView.as_view(), name='pole_delete'),
    path('new/', PoleCreateView.as_view(), name='pole_new'),
    path('', PoleListView.as_view(), name='pole_list'),
    path('<int:pk>/create_image/', PoleCreateImageView.as_view(), name='pole_create_image'),
]
