from . import views
from django.urls import path

urlpatterns = [
	path('recognize/', views.recognize, name = 'recognize'),
	# path("login/", views.login, name="login")
]