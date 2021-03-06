from django.conf.urls import patterns, include, url
from rest_framework import routers
from LMServer import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'lmusers', views.LMUserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'events', views.EventViewSet)

urlpatterns = patterns('',

	# Wire up our API using automatic URL routing.
	# Additionally, we include login URLs for the browseable API.

    # Examples:
    # url(r'^$', 'lastminute.views.home', name='home'),
    # url(r'^lastminute/', include('lastminute.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^', include(router.urls)),
    url(r'^api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^login/$', 'LMServer.views.login'),
    url(r'^signup/$', 'LMServer.views.signup'),
)
