"""
Root API URLs.

All API URLs should be versioned, so urlpatterns should only
contain namespaces for the active versions of the API.
"""
from django.conf.urls import url, include

urlpatterns = [
    url(r'^v1/', include('course_discovery.apps.api.v1.urls', namespace='v1')),
]
