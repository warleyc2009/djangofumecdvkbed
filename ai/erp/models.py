from django.db import models

class Region(models.Model):
    country = models.CharField(max_length=250, default="Brasil")
    state = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Store(models.Model):
    name = models.CharField(max_length=250)
    region = models.ForeignKey(to=Region, on_delete=models.DO_NOTHING)
    neighborhood = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    cep = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ProductCategory(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Product(models.Model):
    category = models.ForeignKey(to=ProductCategory, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=250)
    sku = models.CharField(max_length=100, unique=True)
    brand = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Sale(models.Model):
    store = models.ForeignKey(to=Store, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    discounts = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Employee(models.Model):
    store = models.ForeignKey(to=Store, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    department = models.CharField(max_length=250)
    role = models.CharField(max_length=250)
    birth_date = models.DateTimeField()
    gender = models.CharField(max_length=10, choices=[('M', 'Masculino'), ('F', 'Feminino')])
    education_level = models.CharField(max_length=100, choices=[
        ('BS', 'Ensino Médio'),
        ('GD', 'Graduação'),
        ('EP', 'Especialização'),
        ('MT', 'Mestrado'),
    ])
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    hire_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)