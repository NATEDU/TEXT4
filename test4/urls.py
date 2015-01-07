from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'test4.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^hello$', 'test4.views.home'),
    url(r'^html/(\w+)$', 'test4.views.hello'),
    url(r'^new$', 'test4.views.new'),
    url(r'^del/(\d+)$', 'test4.views.delete'),
    url(r'^edit/(\d+)$', 'test4.views.edit'),
    url(r'^edit_view/(\d+)$', 'test4.views.edit_view'),    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
 	{'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),
 	
)
