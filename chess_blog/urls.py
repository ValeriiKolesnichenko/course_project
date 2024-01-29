from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('login_user/', views.login_user, name='login_user'),
    path('register_user/', views.register_user, name='register_user'),
    path('add_article/', views.add_article, name='add_article'),
    path('add_comment/<int:post_id>/', views.add_comment, name='add_comment'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('strategy/', views.strategy, name='strategy'),
    path('post/<int:post_id>/', views.show_post, name='post'),
    path('world_champions/', views.world_champions, name='world_champions'),
    path('advices_for_beginners/', views.advices_for_beginners, name='advices_for_beginners'),
    path('why_the_chess/', views.why_the_chess, name='why_the_chess'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment')
]
