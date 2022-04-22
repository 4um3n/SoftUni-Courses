from django.urls import path
from petstagram.pets.views import pet_all, create_pet, edit_pet, delete_pet, pet_detail, like_pet

urlpatterns = [
    path('', pet_all, name='pet all'),
    path('create/', create_pet, name='create pet'),
    path('edit/<int:pet_pk>', edit_pet, name='edit pet'),
    path('delete/<int:pet_pk>', delete_pet, name='delete pet'),
    path('detail/<int:pet_pk>', pet_detail, name='pet details'),
    path('like/<int:pet_pk>', like_pet, name='like pet'),
]
