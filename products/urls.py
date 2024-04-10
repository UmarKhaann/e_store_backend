from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListAPIView.as_view(), name='products-list'),
    # path('', views.ProductListCreate.as_view(), name='products create'),
    path('<int:pk>', views.ProductLisUpdateDestroy.as_view(), name='products update')
]
