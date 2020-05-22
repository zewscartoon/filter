from django.urls import path

from . import views

app_name = 'films'
urlpatterns = [
    path('', views.EIndexView.as_view(), name='index'),
    path('<int:film_id>/', views.detail, name = 'detail'),
    path('<int:film_id>/leave_comment/', views.leave_comment, name = 'leave_comment'),
]
