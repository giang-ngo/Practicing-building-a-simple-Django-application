from django.urls import path
from .import views

urlpatterns = [
    path('', views.students, name='students'),
    path('student/<str:pk>', views.student_detail, name='student_detail'),
    path('create-student/', views.create_student, name='create_student'),
    path('update-student/<str:pk>/', views.update_student, name='update_student'),
    path('delete-student/<str:pk>/', views.delete_student, name='delete_student'),

]
