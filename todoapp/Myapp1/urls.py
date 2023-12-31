from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView, RegisterPage,Tasks
from django.contrib.auth.views import LogoutView
from . import views





urlpatterns = [
    path('task/', TaskList.as_view(), name="task"),
    path('task-create/', TaskCreate.as_view(), name="task-create"),
    path('login/', CustomLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page='log'), name="logout"),
    path('register/', RegisterPage.as_view(), name="register"),
    path('task/<int:pk>/', TaskDetail.as_view(), name="tasks-detail"),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name="tasks-update"),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name="tasks-delete"),
    path('tasks/',Tasks.as_view(),name='tasks'),
    path('log/',views.log,name='log'),
    path('',views.home,name='home'),



]