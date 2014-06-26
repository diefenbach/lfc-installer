# python imports
import os

# django imports
from django.conf import settings
from django.conf.urls import include, patterns, url
from django.contrib import admin
from django.contrib.auth.views import login, logout

admin.autodiscover()
DIRNAME = os.path.dirname(__file__)

handler500 = 'lfc.views.fiveohoh'

# Django
urlpatterns = patterns('',
    url('^accounts/login/?$', login, {"template_name": "admin/login.html"}, name='auth_login'),
    url('^accounts/logout/?$', logout, name='auth_logout'),
    (r'^admin/', include(admin.site.urls)),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
)

# LFC
urlpatterns += patterns('',
    (r'^manage', include('lfc.manage.urls')),
    (r'^manage/', include('lfc.manage.urls')),
    (r'', include('lfc.urls')),
)
