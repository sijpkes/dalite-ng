# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
#from django.views.decorators.csrf import csrf_exempt
from django.utils.translation import ugettext_lazy as _

import views

admin.site.site_header = admin.site.site_title = _('Dalite NG administration')

urlpatterns = [
    url(r'', include('peerinst.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'admin_index_wrapper/', views.admin_index_wrapper, name='admin_index_wrapper'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^lti/', include('django_lti_tool_provider.urls')),
     #url(r'^__debug__/', include(debug_toolbar.urls)),#apache WSGI
    #url(r'^dalite-ng/lti/', include('django_lti_tool_provider.urls')), for dev
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
