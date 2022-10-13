from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
    path('admin/',admin.site.urls),
    path('api/',views.products.as_view()),
    path('post/',views.create_prod.as_view()),
    path('update/<int:id>',views.update_product.as_view()),
    path('delete/<int:id>',views.del_product),
    path('dis/<pk>',views.ret_prod.as_view()),

]