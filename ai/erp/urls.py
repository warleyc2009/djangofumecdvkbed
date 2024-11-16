from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("products/", views.product_list, name="product_list"),
    path('product/create', views.product_create, name='product_create'),
    path('product/update/<int:product_id>/', views.product_update, name='product_update'),
    path('product/delete/<int:product_id>/', views.product_delete, name='product_delete'),

    path('prodcategs/', views.prodcateg_list, name='prodcateg_list'),
    path('prodcateg/create', views.prodcateg_create, name='prodcateg_create'),
    path('prodcateg/update/<int:category_id>/', views.prodcateg_update, name='prodcateg_update'),
    path('prodcateg/delete/<int:category_id>/', views.prodcateg_delete, name='prodcateg_delete'),
    
    # Definição da rota para listar as regiões
    path('regions/', views.region_list, name='region_list'),
    # Definição da rota para adicionar uma nova região
    path('regions/create', views.region_create, name='region_create'),
    # Definição da rota para editar uma região
    path('regions/update/<int:region_id>/', views.region_update, name='region_update'),
    # Definição da rota para deletar uma região
    path('regions/delete/<int:region_id>/', views.region_delete, name='region_delete'),
    
    # Definição da rota para listar as lojas
    path('stores/', views.store_list, name='store_list'),
    # Definição da rota para adicionar uma nova loja
    path('stores/create', views.store_create, name='store_create'),
    # Definição da rota para editar uma loja
    path('stores/update/<int:store_id>/', views.store_update, name='store_update'),
    # Definição da rota para deletar uma loja
    path('stores/delete/<int:store_id>/', views.store_delete, name='store_delete'),
    
    # Definição da rota para listar os funcionários
    path('employees/', views.employee_list, name='employee_list'),
    # Definição da rota para adicionar um novo funcionário
    path('employees/create', views.employee_create, name='employee_create'),
    # Definição da rota para editar um funcionário
    path('employees/update/<int:employee_id>/', views.employee_update, name='employee_update'),
    # Definição da rota para deletar um funcionário
    path('employees/delete/<int:employee_id>/', views.employee_delete, name='employee_delete'),
    
    # Definição da rota para listar as vendas
    path('sales/', views.sale_list, name='sale_list'),
    # Definição da rota para adicionar uma nova venda
    path('sales/create', views.sale_create, name='sale_create'),
    # Definição da rota para editar uma venda
    path('sales/update/<int:sale_id>/', views.sale_update, name='sale_update'),
    # Definição da rota para deletar uma venda
    path('sales/delete/<int:sale_id>/', views.sale_delete, name='sale_delete'),
]