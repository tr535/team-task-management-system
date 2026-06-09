from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.update_profile, name='update_profile'),


    path('tasks/', views.task_list, name='task_list'),

    path('add/', views.add_task, name='add_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),

    path('claim/<int:task_id>/', views.claim_task, name='claim_task'),
    path('update_status/<int:task_id>/', views.update_status, name='update_status'),
]