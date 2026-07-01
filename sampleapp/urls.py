from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<int:id>',views.delete_Student,name='delete'),
    path('update/<int:id>',views.update_Student,name='update')
]
