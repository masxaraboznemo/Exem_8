from rest_framework import routers

from .views import PaperViewSet
router = routers.DefaultRouter()
router.register(r'papers', PaperViewSet)

urlpatterns = [] + router.urls