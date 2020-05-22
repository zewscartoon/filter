from django.urls import path

from . import views

app_name = 'premiers'
urlpatterns = [
    path('', views.EIndexView.as_view(), name='index'),
    path('<int:premier_id>/', views.detail, name = 'detail'),
    path('<int:premier_id>/leave_comment/', views.leave_comment, name = 'leave_comment'),
]
