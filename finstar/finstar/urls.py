from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from finstar_task.views import ReceiptView, ProductView, ShopView, UserShopView, ReceiptListView

router = DefaultRouter()
router.register(r'receipt', ReceiptView, basename='receipt')
router.register(r'product', ProductView, basename='product')
router.register(r'shop', ShopView, basename='shop')
router.register(r'user_shop', UserShopView)
router.register('receipt_list', ReceiptListView)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
