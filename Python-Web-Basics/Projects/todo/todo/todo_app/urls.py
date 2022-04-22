from django.urls import path
from todo.todo_app import views


urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create_todo'),
    path('update/<int:todo_id>', views.update, name='update_todo'),
    path('delete/<int:todo_id>', views.delete, name='delete_todo'),
    path('save/', views.save_todo, name='save_todo'),
]
