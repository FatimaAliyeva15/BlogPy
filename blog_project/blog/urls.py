from django.urls import path, include
from .views import index, post_create, post_edit, post_delete, signup
from .views import BlogPostListCreateAPIView, BlogPostRetrieveUpdateDestroyAPIView

app_name = "blog"

urlpatterns = [
    path('', index, name='index'),
    path('new/', post_create, name="post_create"),
    path('<int:pk>/edit/', post_edit, name="post_edit"),
    path('<int:pk>/delete/', post_delete, name="post_delete"),

    #Authentication URL
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', signup, name='signup'),

    #API URL
    path('api/posts/', BlogPostListCreateAPIView.as_view(), name='post_list_create'),
    path('api/posts/<int:pk>/', BlogPostRetrieveUpdateDestroyAPIView.as_view(), name='post_detail'),
]




