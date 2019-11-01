"""web_e_commerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from products.views import home, register, sigin, sigout, add_to_cart, remove_from_cart, \
    ShoppingCart, catalog, product_modal, product_detail, confirm_order
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', home, name='home'),
                  path('register/', register, name="register"),
                  path('login/', sigin, name='login'),
                  path('logout/', sigout, name='sigout'),
                  path('add_cart/<id>', add_to_cart, name='cart'),
                  path('remove_cart/<id>', remove_from_cart, name='remove_from_cart'),
                  path('cart/', ShoppingCart, name='cart'),
                  path('product/catalog/<id>', catalog, name='catalog'),
                  path('product_modal/<id>', product_modal, name='product_modal'),
                  path('product/<name>', product_detail, name='product_detail'),
                  path('order/', confirm_order, name='order'),
                  path('admin/', admin.site.urls),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#         urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
