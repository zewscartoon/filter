from django.urls import path

from . import views

app_name = 'cartoons'
urlpatterns = [
    path('', views.EIndexView.as_view(), name='index'),
    path('<int:cartoon_id>/', views.detail, name = 'detail'),
    path('<int:cartoon_id>/leave_comment/', views.leave_comment, name = 'leave_comment'),
]
