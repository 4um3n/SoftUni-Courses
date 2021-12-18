from django.urls import path
from secondary_app.views import index

urlpatterns = [
    path('', index)
]
