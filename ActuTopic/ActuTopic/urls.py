from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from ActuTopic import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls')),
    path('', include('posts.urls')),

    # url(r'^admin/', admin.site.urls),
    # url(r'^signup/$', p.sign_up, name="sign_up"),
    # url(r'^login/$', p.sign_in, name="sign_in"),
    # url(r'^logout/$', p.log_out, name="logout"),
    # url(r'^nouveau-post/$', p.post_create, name='create'),
    # url(r'modifier/(?P<pk>\d+)/$', p.PostUpdateView.as_view(), name='update'),
    # url(r'supprimer/(?P<pk>\d+)/$', p.PostDeleteView.as_view(), name='delete'),
    # url(r'^account_activation_sent/$', core_views.account_activation_sent, name='account_activation_sent'),
    # url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     core_views.activate, name='activate'),
    # # url(r'^create/$', p.post_create, name="create"),
    # # path('mes-publications/update/<int:pk>', p.PostUpdateView.as_view(), name='update'),
    # # path('mes-publications/delete/<int:pk>', p.PostDeleteView.as_view(), name='delete'),
    # path('', p.PostList.as_view(), name='post_list'),
    # path('<slug:slug>', p.PostDetail.as_view(), name='post_detail'),
    # path('mes-publications/', p.MyPostList.as_view(), name='my_posts'),
    # path('mes-publications/<slug:slug>', p.PostDetail.as_view(), name='my_posts_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)