from rest_framework import routers
from .views import PablicationViewSet

router = routers.DefaultRouter()

router.register(r'pablication', PablicationViewSet)

urlpatterns = [] + router.urls
