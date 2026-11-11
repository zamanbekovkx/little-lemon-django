from rest_framework.routers import DefaultRouter
from .views import BookingViewSet, MenuItemViewSet

router = DefaultRouter()
router.register("menu", MenuItemViewSet, basename="menu")
router.register("booking", BookingViewSet, basename="booking")

urlpatterns = router.urls
