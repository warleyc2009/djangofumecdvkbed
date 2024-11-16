from datetime import datetime

# Importando os modelos
from erp.models import Region, Store, ProductCategory, Product, Employee, Sale

# Dados para popular o banco de dados
regioes = [
    {"country": "Brasil", "state": "Minas Gerais", "city": "Belo Horizonte"},
    {"country": "Brasil", "state": "Minas Gerais", "city": "Uberlândia"},
    {"country": "Brasil", "state": "Minas Gerais", "city": "Contagem"},
    {"country": "Brasil", "state": "Minas Gerais", "city": "Juiz de Fora"},
    {"country": "Brasil", "state": "Minas Gerais", "city": "Betim"},
    {"country": "Brasil", "state": "Minas Gerais", "city": "Montes Claros"}
]

lojas = [
    {"name": "Supermercado Central BH", "country": "Brasil", "state": "Minas Gerais", "city": "Belo Horizonte", "neighborhood": "Centro", "address": "Rua Principal, 123", "cep": "30100-000"},
    {"name": "Supermercado Uberlândia Sul", "country": "Brasil", "state": "Minas Gerais", "city": "Uberlândia", "neighborhood": "Sul", "address": "Avenida Brasil, 456", "cep": "38400-000"},
    {"name": "Supermercado Contagem Norte", "country": "Brasil", "state": "Minas Gerais", "city": "Contagem", "neighborhood": "Norte", "address": "Rua das Flores, 789", "cep": "32000-000"},
    {"name": "Supermercado Juiz de Fora Leste", "country": "Brasil", "state": "Minas Gerais", "city": "Juiz de Fora", "neighborhood": "Leste", "address": "Avenida Independência, 101", "cep": "36000-000"},
    {"name": "Supermercado Betim Oeste", "country": "Brasil", "state": "Minas Gerais", "city": "Betim", "neighborhood": "Oeste", "address": "Rua São João, 202", "cep": "32500-000"},
    {"name": "Supermercado Montes Claros Centro", "country": "Brasil", "state": "Minas Gerais", "city": "Montes Claros", "neighborhood": "Centro", "address": "Praça da Liberdade, 303", "cep": "39400-000"}
]

categorias_produtos = [
    {"name": "Laticínios", "description": "Produtos derivados do leite"},
    {"name": "Bebidas", "description": "Refrigerantes, sucos e águas"},
    {"name": "Higiene Pessoal", "description": "Produtos de higiene e cuidados pessoais"},
    {"name": "Frios e Embutidos", "description": "Presunto, queijo, salame e outros"},
    {"name": "Limpeza", "description": "Produtos de limpeza doméstica"}
]

produtos = [
    {"category": "Laticínios", "name": f"Leite Integral {i}", "sku": f"LT00{i}", "brand": f"Marca {chr(65 + i % 3)}", "price": 4.50 + i} for i in range(1, 11)
] + [
    {"category": "Bebidas", "name": f"Refrigerante {i}", "sku": f"RF00{i}", "brand": f"Marca {chr(65 + i % 3)}", "price": 5.00 + i} for i in range(1, 11)
] + [
    {"category": "Higiene Pessoal", "name": f"Shampoo {i}", "sku": f"SH00{i}", "brand": f"Marca {chr(65 + i % 3)}", "price": 10.90 + i} for i in range(1, 11)
] + [
    {"category": "Frios e Embutidos", "name": f"Queijo {i}", "sku": f"QJ00{i}", "brand": f"Marca {chr(65 + i % 3)}", "price": 15.00 + i} for i in range(1, 11)
] + [
    {"category": "Limpeza", "name": f"Detergente {i}", "sku": f"DT00{i}", "brand": f"Marca {chr(65 + i % 3)}", "price": 3.50 + i} for i in range(1, 11)
]

funcionarios = [
    {"store": "Supermercado Central BH", "name": f"Funcionário {i}", "department": "Caixa", "role": "Operador", "birth_date": datetime(1980 + (i % 30), 1, (i % 28) + 1), "gender": "M" if i % 2 == 0 else "F", "education_level": "BS" if i % 2 == 0 else "GD", "salary": 2000.00 + i * 10, "hire_date": datetime(2021, (i % 12) + 1, (i % 28) + 1)} for i in range(1, 31)
]

vendas = [
    {"store": "Supermercado Central BH", "product_name": f"Leite Integral {i % 10 + 1}", "product_category": "Laticínios", "quantity": (i % 10) + 1, "discounts": 1.50 if i % 3 == 0 else 0.00} for i in range(1, 21)
]

# Criando objetos no banco de dados
for regiao in regioes:
    Region.objects.create(
        country=regiao["country"],
        state=regiao["state"],
        city=regiao["city"]
    )

for loja in lojas:
    region = Region.objects.get(country=loja["country"], state=loja["state"], city=loja["city"])
    Store.objects.create(
        name=loja["name"],
        region=region,
        neighborhood=loja["neighborhood"],
        address=loja["address"],
        cep=loja["cep"]
    )

for categoria in categorias_produtos:
    ProductCategory.objects.create(
        name=categoria["name"],
        description=categoria["description"]
    )

for produto in produtos:
    category = ProductCategory.objects.get(name=produto["category"])
    Product.objects.create(
        category=category,
        name=produto["name"],
        sku=produto["sku"],
        brand=produto["brand"],
        price=produto["price"]
    )

for funcionario in funcionarios:
    store = Store.objects.get(name=funcionario["store"])
    Employee.objects.create(
        store=store,
        name=funcionario["name"],
        department=funcionario["department"],
        role=funcionario["role"],
        birth_date=funcionario["birth_date"],
        gender=funcionario["gender"],
        education_level=funcionario["education_level"],
        salary=funcionario["salary"],
        hire_date=funcionario["hire_date"]
    )

for venda in vendas:
    store = Store.objects.get(name=venda["store"])
    product = Product.objects.get(name=venda["product_name"], category__name=venda["product_category"])
    Sale.objects.create(
        store=store,
        product=product,
        quantity=venda["quantity"],
        discounts=venda["discounts"]
    )