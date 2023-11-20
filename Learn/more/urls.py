from django.urls import path
from . import views

app_name = 'more'

urlpatterns = [
    
    path('', views.all_mores,  name ='all_mores'),
    path('<int:more_id>/', views.detail,  name ='detail'),
    # path('post_new/', views.post_new, name='post_new'),
    # path('', views.post_detail,  name ='post_detail'),
    # path('<int:post_id>/', views.post_edit,  name ='post_edit'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/detail/', views.post_detail, name='post_detail'),


]