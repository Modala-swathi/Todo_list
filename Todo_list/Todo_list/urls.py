from django.contrib import admin
from django.urls import path,include
from . import views 
urlpatterns = [
    path('',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('todo/',views.todo,name='todo'),
    path('edit_task/<int:srno>',views.edit_task,name='edit_task'),
    path('delete_task/<int:srno>',views.delete_task,name='delete_task'),
    path('logout/',views.logout,name='logout'),
    path('admin/', admin.site.urls),
]
