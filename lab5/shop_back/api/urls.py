from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

# router = DefaultRouter()
# router.register(r'categories/<int:id>/products',
#                 views.ProductByCategoryView,
#                 basename='products_by_categories')
# router.register(r'products', views.ProductViewSet, basename='products')
# router.register(r'categories', views.CategoryViewSet, basename='categories')
# urlpatterns = router.urls
urlpatterns = [
    path(r'categories/<int:pk>/products', views.ProductByCategoryView.as_view({'get': 'retrieve'})),
    # path('', include(router.urls))
]
# urlpatterns = router.urls
