from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('ads/', views.ads_page, name='ads_page'),
    path('categories/', views.categories_page, name='categories_page'),
    path('favorite/', views.favorite_page, name='favorite_page'),
    path('neighbor/', views.neighbor_page, name='neighbor_page'),
    path('neighbor/detail/<int:pk>/', views.neighbor_detail_page, name='neighbor_detail_page'),
    path('ads/detail/<int:pk>/', views.ads_detail_page, name='ads_detail_page'),
    path('category/ads/<slug:slug>/', views.ads_by_categories_page, name='ads_by_categories_page'),
    path('sign-up/', views.sign_up_page, name='sign_up_page'),
    path('login/', views.login_page, name='login_page'),
    path('logout/',views.logout_action, name='logout_action'),
    path('add/', views.add_post, name='add_post'),
    path('post/<int:post_id>/delete/', views.delete_post, name='post_delete'),
    
]