from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import url
from django.urls import path

from ActuTopic import settings
from app import views as p

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^signup/$', p.sign_up, name="sign_up"),
    url(r'^login/$', p.sign_in, name="sign_in"),
    url(r'^logout/$', p.log_out, name="logout"),
    url(r'^create/$', p.post_create, name="create"),
    path('', p.PostList.as_view(), name='post_list'),
    path('<slug:slug>/', p.PostDetail.as_view(), name='post_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)