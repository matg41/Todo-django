from django.urls import path
from . import views


urlpatterns = [
    #Adding Tasks
    path('addTask/', views.addTask, name='addTask'),
    
    #Mark as Done and Undone
    path('mark_as_done/<int:pk>', views.mark_as_done, name='mark_as_done'),
    path('mark_as_undone/<int:pk>', views.mark_as_undone, name='mark_as_undone'),

    #Edit tasks
    path("edit_task/<int:pk>", views.edit_task, name='edit_task'),

    #Delete task
    path('delete_task/<int:pk>', views.delete_task, name='delete_task')
]