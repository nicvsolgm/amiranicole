from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('work/', views.work, name='work'),
    #path('blog/', PostListView.as_view(), name='blog'),
    #path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
