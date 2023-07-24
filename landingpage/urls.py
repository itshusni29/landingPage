from django.urls import path, include
from landingpage import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    
    path('create_blog_post/', views.create_blog_post, name='create_blog_post'),
    path('blog_list/', views.blog_list, name='blog_list'),
    path('ckeditor/', include('ckeditor_uploader.urls')),   
]

# Add the URL for serving media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)