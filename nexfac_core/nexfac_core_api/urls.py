"""
Nexfac Core API Url file
"""
from django.urls import path, include
from rest_framework import routers
from .views import get_user_tasks, UserTasksView

router = routers.DefaultRouter()
router.register(r'users', UserTasksView)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('user_tasks/<int:user_id>', get_user_tasks),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
