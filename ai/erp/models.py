from django.db import models

# Modelo para representar uma região geográfica
class Region(models.Model):
    country = models.CharField(max_length=250, default="Brasil")  # País da região, com valor padrão "Brasil"
    state = models.CharField(max_length=250)  # Estado da região
    city = models.CharField(max_length=250)  # Cidade da região
    created_at = models.DateTimeField(auto_now_add=True)  # Data e hora de criação do registro
    updated_at = models.DateTimeField(auto_now=True)  # Data e hora da última atualização do registro

# Modelo para representar uma loja
class Store(models.Model):
    name = models.CharField(max_length=250)  # Nome da loja
    region = models.ForeignKey(to=Region, on_delete=models.DO_NOTHING)  # Relação com a região onde a loja está localizada
    neighborhood = models.CharField(max_length=250)  # Bairro onde a loja está localizada
    address = models.CharField(max_length=250)  # Endereço da loja
    cep = models.CharField(max_length=20)  # CEP da loja
    created_at = models.DateTimeField(auto_now_add=True)  # Data e hora de criação do registro
    updated_at = models.DateTimeField(auto_now=True)  # Data e hora da última atualização do registro

# Modelo para representar uma categoria de produto
class ProductCategory(models.Model):
    name = models.CharField(max_length=250)  # Nome da categoria de produto
    description = models.TextField(null=True, blank=True)  # Descrição da categoria (opcional)
    created_at = models.DateTimeField(auto_now_add=True)  # Data e hora de criação do registro
    updated_at = models.DateTimeField(auto_now=True)  # Data e hora da última atualização do registro

# Modelo para representar um produto
class Product(models.Model):
    category = models.ForeignKey(to=ProductCategory, on_delete=models.DO_NOTHING)  # Relação com a categoria do produto
    name = models.CharField(max_length=250)  # Nome do produto
    sku = models.CharField(max_length=100, unique=True)  # Código SKU do produto (deve ser único)
    brand = models.CharField(max_length=250)  # Marca do produto
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Preço do produto
    created_at = models.DateTimeField(auto_now_add=True)  # Data e hora de criação do registro
    updated_at = models.DateTimeField(auto_now=True)  # Data e hora da última atualização do registro

# Modelo para representar uma venda
class Sale(models.Model):
    store = models.ForeignKey(to=Store, on_delete=models.CASCADE)  # Relação com a loja onde a venda foi realizada
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)  # Relação com o produto vendido
    quantity = models.PositiveIntegerField()  # Quantidade do produto vendido
    discounts = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Valor dos descontos aplicados
    created_at = models.DateTimeField(auto_now_add=True)  # Data e hora de criação do registro
    updated_at = models.DateTimeField(auto_now=True)  # Data e hora da última atualização do registro

# Modelo para representar um funcionário
class Employee(models.Model):
    store = models.ForeignKey(to=Store, on_delete=models.CASCADE)  # Relação com a loja onde o funcionário trabalha
    name = models.CharField(max_length=250)  # Nome do funcionário
    department = models.CharField(max_length=250)  # Departamento do funcionário
    role = models.CharField(max_length=250)  # Cargo do funcionário
    birth_date = models.DateTimeField()  # Data de nascimento do funcionário
    gender = models.CharField(max_length=10, choices=[('M', 'Masculino'), ('F', 'Feminino')])  # Gênero do funcionário
    education_level = models.CharField(max_length=100, choices=[
        ('BS', 'Ensino Médio'),
        ('GD', 'Graduação'),
        ('EP', 'Especialização'),
        ('MT', 'Mestrado'),
    ])  # Nível de escolaridade do funcionário
    salary = models.DecimalField(max_digits=10, decimal_places=2)  # Salário do funcionário
    hire_date = models.DateTimeField()  # Data de admissão do funcionário
    created_at = models.DateTimeField(auto_now_add=True)  # Data e hora de criação do registro
    updated_at = models.DateTimeField(auto_now=True)  # Data e hora da última atualização do registro