# django imports
from django.conf import settings
from django.conf.urls import include, patterns
from django.conf.urls.static import static
from django.contrib import admin

admin.autodiscover()
handler500 = 'lfc.views.fiveohoh'

# Django
urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# LFC
urlpatterns += patterns('',
    (r'^manage', include('lfc.manage.urls')),
    (r'^manage/', include('lfc.manage.urls')),
    (r'', include('lfc.urls')),
)
