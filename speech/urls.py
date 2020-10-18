from . import views
from django.urls import path

urlpatterns = [
	path('recognize_interface/', views.recognize_interface, name="recognize_interface"),
	path("recognize_api/", views.recognize_api, name="recognize_api")
]