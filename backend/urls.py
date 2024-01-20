from django.urls import path

from . import views
from .views import AllProductsView, ProductView, CategoryProductView, HomeTemplateView, CategoryTemplateView
from .views import ProductTemplateView , ContactTemplateView, AboutTemplateView, add_product, edit_product
from .views import ChangePasswordView, profile, register
from django.contrib.auth.views import LoginView,LogoutView


urlpatterns = [
        path('login/', LoginView.as_view(template_name='login.html'), name='login'),
        path('logout/', LogoutView.as_view(), name='logout'),
        path('profile/', views.profile, name = 'profile'),
        path('change_password/', ChangePasswordView.as_view(),name = 'change_password'),

        path('register/', views.register, name = 'register'),

        path('',HomeTemplateView.as_view(), name='home'),
        path('product/<int:pk>/',ProductTemplateView.as_view(),name='product'),
        path('category/<int:pk>/',CategoryTemplateView.as_view(),name='category'),
        path('contact/',ContactTemplateView.as_view(),name='contact'),
        path('about/', AboutTemplateView.as_view(), name='about'),

        path('products/', AllProductsView.as_view(), name='products'),
        path('contact/',ContactTemplateView.as_view(),name='contact'),
        path('products/<int:product_id>/', ProductView.as_view(), name='product_detailed'),
        path('products/category/<int:category_id>/', CategoryProductView.as_view(), name='category_product'),

        path('add_product/', views.add_product,name = 'add_product'),
        path('edit_product/<int:pk>/', views.edit_product,name = 'edit_product'),
]
