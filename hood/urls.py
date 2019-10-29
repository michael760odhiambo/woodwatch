from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns= [
    url(r'^$', views.home, name='home'),
    url(r'^authorities',views.authorities, name='authorities'),
    url(r'^alert',views.alert, name='alert'),
    url(r'^post/',views.posted, name='posted'),
    url(r'^biz',views.biz, name='biz'),
    url(r'^hoods/',views.neighbourhoods, name='create-hoods'),
    url(r'^nhoods/',views.joinone, name='join-one'),
    url(r'^joinhood/',views.joinhood, name='join-hood'),
    #url(r'^view/post/<post>',views.view_post,name='view-post'),
    url(r'^userprofile/',views.userprofile,name='userprofile'),
    url(r'^new/post$',views.create_post, name='create-post'),
    url(r'^create/profile$',views.create_profile, name='create-profile'),
    url(r'^new/trending$',views.trending, name='new-trends'),
    url(r'^update/profile$',views.update_profile, name='update-profile'),
   # url(r'^search/',views.search_results, name='search_results'),

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)