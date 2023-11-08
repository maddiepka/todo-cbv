from django.urls import path

from . import views

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.LoginPage.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    path('', views.TaskList.as_view(), name='tasks'),
    path('task/<str:pk>', views.TaskDetail.as_view(), name='task'),
    path('create-task/', views.TaskCreate.as_view(), name='create-task'),
    path('update-task/<str:pk>', views.TaskUpdate.as_view(), name='update-task'),
    path('delete-task/<str:pk>', views.TaskDelete.as_view(), name='delete-task'),

]