from django.urls import path

from . import views

app_name = 'series'
urlpatterns = [
    path('', views.EIndexView.as_view(), name='index'),
    path('<int:serie_id>/', views.detail, name = 'detail'),
    path('<int:serie_id>/leave_comment/', views.leave_comment, name = 'leave_comment'),
]
