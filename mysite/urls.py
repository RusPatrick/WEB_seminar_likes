from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from ask import views

urlpatterns = [
    path('', views.index, name='main-view'),
    path('add_article/', views.add_article, name='add_article'),
    path('like/', views.like, name='like'),
    path('admin/', admin.site.urls),
    path(r'^article/like/(?P<article_id>[0-9]+)/$', views.like, name='article'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
