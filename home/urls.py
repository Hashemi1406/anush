from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.Home.as_view()),
    path('detail/<int:post_id>/', views.PostDetailView.as_view()),
    path('create/', views.PostCreateView.as_view()),
    path('update/<int:post_id>/', views.UpdatePostView.as_view()),
    path('delete/<int:post_id>/', views.PostDeleteView.as_view()),
    path('comments/',views.CommentsView.as_view()),
    path('comments/create/',views.CreateCommentsView.as_view()),
    path('comments/update/<int:comment_id>/',views.UpdateCommentsView.as_view()),
    path('comments/delete/<int:comment_id>/',views.DeleteCommentsView.as_view()),
    # path('comments/reply/',views.ReplyCommentsView.as_view()),
]
