
from django.urls import path, include
from . import views
urlpatterns = [
    path("", views.home, name="home"),
    #user
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    # path('add/', views.person_create, name='person_create'),
    # path('edit/<str:tz>/', views.person_update, name='person_update'),
    # path('delete/<str:tz>/', views.person_delete, name='person_delete'),
    # path('enroll/<str:tz>/', views.student_enroll, name='student_enroll'),
    path("register/", views.register_view, name="register"),
    path('list/', views.user_list, name='user_list'),
    path('choose/', views.choose_team, name='choose_team'),

    #task
    path('tasks/', views.task_list, name='task_list'),
    path('task_take/', views.task_take, name='task_take'),
    path('tasks/add/', views.task_create, name='task_create'),
    path('tasks/edit/<int:pk>/', views.task_update, name='task_update'),
    path('tasks/delete/<int:pk>/', views.task_delete, name='task_delete'),
    #team






]