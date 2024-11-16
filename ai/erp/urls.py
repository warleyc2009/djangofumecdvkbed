from django.urls import path

from . import views

urlpatterns = [
    # Rota da página inicial
    path("", views.index, name="index"),

    # Rotas para produtos
    path("products/", views.product_list, name="product_list"),
    path('product/create', views.product_create, name='product_create'),
    path('product/update/<int:product_id>/', views.product_update, name='product_update'),
    path('product/delete/<int:product_id>/', views.product_delete, name='product_delete'),

    # Rotas para categorias de produtos
    path('prodcategs/', views.prodcateg_list, name='prodcateg_list'),
    path('prodcateg/create', views.prodcateg_create, name='prodcateg_create'),
    path('prodcateg/update/<int:category_id>/', views.prodcateg_update, name='prodcateg_update'),
    path('prodcateg/delete/<int:category_id>/', views.prodcateg_delete, name='prodcateg_delete'),
    
    # Rotas para regiões
    path('regions/', views.region_list, name='region_list'),
    path('regions/create', views.region_create, name='region_create'),
    path('regions/update/<int:region_id>/', views.region_update, name='region_update'),
    path('regions/delete/<int:region_id>/', views.region_delete, name='region_delete'),
    
    # Rotas para lojas
    path('stores/', views.store_list, name='store_list'),
    path('stores/create', views.store_create, name='store_create'),
    path('stores/update/<int:store_id>/', views.store_update, name='store_update'),
    path('stores/delete/<int:store_id>/', views.store_delete, name='store_delete'),
    
    # Rotas para funcionários
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/create', views.employee_create, name='employee_create'),
    path('employees/update/<int:employee_id>/', views.employee_update, name='employee_update'),
    path('employees/delete/<int:employee_id>/', views.employee_delete, name='employee_delete'),
    
    # Rotas para vendas
    path('sales/', views.sale_list, name='sale_list'),
    path('sales/create', views.sale_create, name='sale_create'),
    path('sales/update/<int:sale_id>/', views.sale_update, name='sale_update'),
    path('sales/delete/<int:sale_id>/', views.sale_delete, name='sale_delete'),
]