from django.urls import path
from . import views

urlpatterns = [
    path('', views.story_list, name='story_list'),
    path('play/<int:story_id>/', views.play_story, name='play_story'),
    path('page/<int:page_id>/', views.page_view, name='page'),
    path('stats/', views.stats_view, name='stats'),
    path('signup/', views.signup_view, name='signup'),
    path('author/', views.author_dashboard, name='author_dashboard'),
    path('author/create-story/', views.create_story, name='create_story'),
    path('author/my-stories/', views.my_stories, name='my_stories'),
    path('my-history/', views.my_history, name='my_history'),
    path('admin/stats/', views.admin_stats, name='admin_stats'),
    path('admin/suspend/<int:story_id>/', views.suspend_story, name='suspend_story'),
    path('rate/<int:story_id>/', views.rate_story, name='rate_story'),
    path('report/<int:story_id>/', views.report_story, name='report_story'),
    path('rate/<int:story_id>/', views.rate_story, name='rate_story'),
    path('comment/<int:story_id>/', views.add_comment, name='add_comment'),
    path('report/<int:story_id>/', views.report_story, name='report_story'),
    path('rate/<int:story_id>/', views.rate_story, name='rate_story'),
]
