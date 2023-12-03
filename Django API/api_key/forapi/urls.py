from rest_framework import routers
from .api import ForAPIViewsSet

router = routers.DefaultRouter()
router.register('api/forapi', ForAPIViewsSet, 'forapi')

urlpatterns = router.urls
