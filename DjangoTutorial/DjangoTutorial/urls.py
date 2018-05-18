"""
Definition of urls for DjangoTutorial.
"""

from django.conf.urls import include, url
import FirstApp.views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', FirstApp.views.index, name='index'),
	url(r'^home$', FirstApp.views.index, name='home'),
	url(r'^about$', FirstApp.views.about, name='about'),

    # url(r'^DjangoTutorial/', include('DjangoTutorial.DjangoTutorial.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
