from django.shortcuts import render, get_object_or_404, redirect
from django.utils.dateparse import parse_date
from .models import Product, ProductCategory, Region, Store, Employee, Sale

# View para renderizar a página inicial
# Essa função simplesmente renderiza a página "home.html"
def index(request):
    return render(request, "home.html")

# View para listar todos os produtos
# Busca todos os registros de produtos e passa para o template 'product/product_list.html'
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product/product_list.html', {"products": products})

# View para criar um novo produto
# Caso o método seja POST, cria o produto com os dados recebidos, senão, renderiza o formulário
# Busca todas as categorias de produtos e passa para o template 'product/product_form.html'
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

# View para atualizar um produto existente
# Caso o método seja POST, atualiza o produto com os dados recebidos, senão, renderiza o formulário com os dados atuais
# Busca todas as categorias de produtos e passa para o template 'product/product_form.html'
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

# View para deletar um produto
# Deleta o produto e redireciona para a lista de produtos
def product_delete(request, product_id):
    produto = get_object_or_404(Product, pk=product_id)
    produto.delete()
    return redirect('product_list')

# View para listar categorias de produtos
def prodcateg_list(request):
    categorias = ProductCategory.objects.all()
    return render(request, 'productCategory/productCategory_list.html', {"categorias": categorias})

# View para criar uma nova categoria de produto
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

# View para atualizar uma categoria de produto
def prodcateg_update(request, category_id):
    categoria = get_object_or_404(ProductCategory, pk=category_id)
    if request.method == 'POST':
        categoria.name = request.POST['name']
        categoria.description = request.POST.get('description', '')
        categoria.save()
        return redirect('prodcateg_list')

    return render(request, 'productCategory/productCategory_form.html', {'categoria': categoria})

# View para deletar uma categoria de produto
def prodcateg_delete(request, category_id):
    categoria = get_object_or_404(ProductCategory, pk=category_id)
    categoria.delete()
    return redirect('prodcateg_list')

# View para listar regiões
def region_list(request):
    regions = Region.objects.all()
    return render(request, 'region/region_list.html', {"regions": regions})

# View para criar uma nova região
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

# View para atualizar uma região existente
def region_update(request, region_id):
    region = get_object_or_404(Region, pk=region_id)
    if request.method == 'POST':
        region.country = request.POST['country']
        region.state = request.POST['state']
        region.city = request.POST['city']
        region.save()
        return redirect('region_list')
    return render(request, 'region/region_form.html', {'region': region})

# View para deletar uma região
def region_delete(request, region_id):
    region = get_object_or_404(Region, pk=region_id)
    region.delete()
    return redirect('region_list')

# View para listar lojas
def store_list(request):
    stores = Store.objects.all()
    return render(request, 'store/store_list.html', {"stores": stores})

# View para criar uma nova loja
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

# View para atualizar uma loja existente
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

# View para deletar uma loja
def store_delete(request, store_id):
    store = get_object_or_404(Store, pk=store_id)
    store.delete()
    return redirect('store_list')