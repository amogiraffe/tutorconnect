from django.urls import path
from . import views

urlpatterns = [
    path('', views.TutorListView.as_view(), name='tutor_list'),
]