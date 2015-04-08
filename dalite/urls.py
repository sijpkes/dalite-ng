# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

admin.site.site_header = admin.site.site_title = _('Dalite NG administration')

urlpatterns = [
    # Examples:
    # url(r'^$', 'dalite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(br'^admin/', include(admin.site.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
