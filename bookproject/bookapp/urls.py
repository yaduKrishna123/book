from django.urls import path

from bookapp import views
app_name='bookapp'

urlpatterns = [
    path('',views.home,name='home'),
    path('demo', views.demo, name='demo'),
    path('books/<int:book_id>/',views.details,name="details"),
    path('book/<int:book_id>/',views.detail,name="detail"),
    path('add/',views.add,name="add"),
    path('update/<int:id>/',views.update,name="update"),
    path('delete/<int:id>/',views.delete,name="delete"),



]