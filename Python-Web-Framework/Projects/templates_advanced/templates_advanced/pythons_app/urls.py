from django.urls import path
from templates_advanced.pythons_app.views import index, create, IndexView, CreatePythonView


urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('create/', CreatePythonView.as_view(), name="create"),
]
