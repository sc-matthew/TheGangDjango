from django.contrib import admin
from django.urls import path, re_path
from .middlewares.auth import auth_middleware
from .views import Index, store, Signup, Login, logout, Cart, CheckOut, OrderView, product_details

# URLConf
urlpatterns = [
    path("", Index.as_view(), name="homepage"),
    path("store", store, name="store"),
    path("signup", Signup.as_view(), name="signup"),
    path("login", Login.as_view(), name="login"),
    path("logout", logout, name="logout"),
    path("cart", auth_middleware(Cart.as_view()), name="cart"),
    path("check-out", CheckOut.as_view(), name="checkout"),
    path("orders", auth_middleware(OrderView.as_view()), name="orders"),
    # path("product_details", auth_middleware(product_details.as_view()), name="product_details"),
    path('product_details/<int:product_id>/', product_details.as_view(), name='product_details')
]
