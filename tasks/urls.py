from django.urls import path

from . import views

urlpatterns = [
    path('', views.TaskList.as_view(), name='tasks'),
    path('task/<str:pk>', views.TaskDetail.as_view(), name='task'),
    path('create-task/', views.TaskCreate.as_view(), name='create-task'),
    path('update-task/<str:pk>', views.TaskUpdate.as_view(), name='update-task'),
    path('delete-task/<str:pk>', views.TaskDelete.as_view(), name='delete-task'),

]