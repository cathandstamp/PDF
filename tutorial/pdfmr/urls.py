from django.contrib import admin
from django.urls import path
from . import views



app_name ="pdfmr"

urlpatterns = [
    path('top/', views.top, name='top'),
    path('', views.top, name='top'),#Add
    path('upload/', views.UploadView.as_view(), name='upload'),  

]