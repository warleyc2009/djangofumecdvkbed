from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils.dateparse import parse_date
from .models import Product, ProductCategory,  Region, Store, Employee, Sale

def index(request):
    return render(request, "home.html")

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product/product_list.html', {"products": products})

def product_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        brand = request.POST['brand']
        price = request.POST['price']
        category_id = request.POST['category']
        sku = request.POST['sku']

        categoria = get_object_or_404(ProductCategory, pk=category_id)

        Product.objects.create(
            name=name,
            brand=brand,
            price=price,
            category=categoria,
            sku=sku
        )
        return redirect('product_list')

    categorias = ProductCategory.objects.all()
    return render(request, 'product/product_form.html', {'categorias': categorias})

def product_update(request, product_id):
    produto = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        produto.name = request.POST['name']
        produto.brand = request.POST['brand']
        produto.price = request.POST['price']
        produto.category = get_object_or_404(ProductCategory, pk=request.POST['category'])
        produto.sku = request.POST['sku']
        produto.save()
        return redirect('product_list')

    categorias = ProductCategory.objects.all()
    return render(request, 'product/product_form.html', {'produto': produto, 'categorias': categorias})

def product_delete(request, product_id):
    produto = get_object_or_404(Product, pk=product_id)
    produto.delete()
    return redirect('product_list')

def prodcateg_list(request):
    categorias = ProductCategory.objects.all()
    return render(request, 'productCategory/productCategory_list.html', {"categorias": categorias})

def prodcateg_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST.get('description', '')

        ProductCategory.objects.create(
            name=name,
            description=description
        )
        return redirect('prodcateg_list')

    return render(request, 'productCategory/productCategory_form.html')

def prodcateg_update(request, category_id):
    categoria = get_object_or_404(ProductCategory, pk=category_id)
    if request.method == 'POST':
        categoria.name = request.POST['name']
        categoria.description = request.POST.get('description', '')
        categoria.save()
        return redirect('prodcateg_list')

    return render(request, 'productCategory/productCategory_form.html', {'categoria': categoria})

def prodcateg_delete(request, category_id):
    categoria = get_object_or_404(ProductCategory, pk=category_id)
    categoria.delete()
    return redirect('prodcateg_list')

def region_list(request):
    regions = Region.objects.all()
    return render(request, 'region/region_list.html', {"regions": regions})

def region_create(request):
    if request.method == 'POST':
        country = request.POST['country']
        state = request.POST['state']
        city = request.POST['city']

        Region.objects.create(
            country=country,
            state=state,
            city=city
        )
        return redirect('region_list')
    return render(request, 'region/region_form.html')

def region_update(request, region_id):
    region = get_object_or_404(Region, pk=region_id)
    if request.method == 'POST':
        region.country = request.POST['country']
        region.state = request.POST['state']
        region.city = request.POST['city']
        region.save()
        return redirect('region_list')
    return render(request, 'region/region_form.html', {'region': region})

def region_delete(request, region_id):
    region = get_object_or_404(Region, pk=region_id)
    region.delete()
    return redirect('region_list')

def store_list(request):
    stores = Store.objects.all()
    return render(request, 'store/store_list.html', {"stores": stores})

def store_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        region_id = request.POST['region']
        neighborhood = request.POST['neighborhood']
        address = request.POST['address']
        cep = request.POST['cep']

        region = get_object_or_404(Region, pk=region_id)

        Store.objects.create(
            name=name,
            region=region,
            neighborhood=neighborhood,
            address=address,
            cep=cep
        )
        return redirect('store_list')

    regions = Region.objects.all()
    return render(request, 'store/store_form.html', {'regions': regions})

def store_update(request, store_id):
    store = get_object_or_404(Store, pk=store_id)
    if request.method == 'POST':
        store.name = request.POST['name']
        store.region = get_object_or_404(Region, pk=request.POST['region'])
        store.neighborhood = request.POST['neighborhood']
        store.address = request.POST['address']
        store.cep = request.POST['cep']
        store.save()
        return redirect('store_list')

    regions = Region.objects.all()
    return render(request, 'store/store_form.html', {'store': store, 'regions': regions})

def store_delete(request, store_id):
    store = get_object_or_404(Store, pk=store_id)
    store.delete()
    return redirect('store_list')


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee/employee_list.html', {"employees": employees})

# View para criar um novo funcionário
def employee_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        store_id = request.POST['store']
        department = request.POST['department']
        role = request.POST['role']
        birth_date = parse_date(request.POST['birth_date'])  # Corrige para garantir que o valor seja uma data válida
        gender = request.POST['gender']
        education_level = request.POST['education_level']
        salary = request.POST['salary']
        hire_date = parse_date(request.POST['hire_date'])  # Corrige para garantir que o valor seja uma data válida

        store = get_object_or_404(Store, pk=store_id)

        # Cria o novo funcionário
        Employee.objects.create(
            name=name,
            store=store,
            department=department,
            role=role,
            birth_date=birth_date,
            gender=gender,
            education_level=education_level,
            salary=salary,
            hire_date=hire_date
        )
        return redirect('employee_list')

    stores = Store.objects.all()
    return render(request, 'employee/employee_form.html', {'stores': stores})

# View para editar um funcionário
def employee_update(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    if request.method == 'POST':
        employee.name = request.POST['name']
        employee.store = get_object_or_404(Store, pk=request.POST['store'])
        employee.department = request.POST['department']
        employee.role = request.POST['role']
        employee.birth_date = request.POST['birth_date']
        employee.salary = request.POST['salary']
        employee.save()
        return redirect('employee_list')

    stores = Store.objects.all()
    return render(request, 'employee/employee_form.html', {'employee': employee, 'stores': stores})

# View para deletar um funcionário
def employee_delete(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    employee.delete()
    return redirect('employee_list')

# View para listar vendas
def sale_list(request):
    sales = Sale.objects.all()
    return render(request, 'sale/sale_list.html', {"sales": sales})

# View para criar uma nova venda
def sale_create(request):
    if request.method == 'POST':
        store_id = request.POST['store']
        product_id = request.POST['product']
        quantity = request.POST['quantity']
        discounts = request.POST.get('discounts', 0.00)

        store = get_object_or_404(Store, pk=store_id)
        product = get_object_or_404(Product, pk=product_id)

        Sale.objects.create(
            store=store,
            product=product,
            quantity=quantity,
            discounts=discounts
        )
        return redirect('sale_list')

    stores = Store.objects.all()
    products = Product.objects.all()
    return render(request, 'sale/sale_form.html', {'stores': stores, 'products': products})

# View para editar uma venda
def sale_update(request, sale_id):
    sale = get_object_or_404(Sale, pk=sale_id)
    if request.method == 'POST':
        sale.store = get_object_or_404(Store, pk=request.POST['store'])
        sale.product = get_object_or_404(Product, pk=request.POST['product'])
        sale.quantity = request.POST['quantity']
        sale.discounts = request.POST.get('discounts', 0.00)
        sale.save()
        return redirect('sale_list')

    stores = Store.objects.all()
    products = Product.objects.all()
    return render(request, 'sale/sale_form.html', {'sale': sale, 'stores': stores, 'products': products})

# View para deletar uma venda
def sale_delete(request, sale_id):
    sale = get_object_or_404(Sale, pk=sale_id)
    sale.delete()
    return redirect('sale_list')