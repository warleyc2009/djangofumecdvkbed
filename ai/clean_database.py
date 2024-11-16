# Importando os modelos
from erp.models import Region, Store, ProductCategory, Product, Employee, Sale

# Função para deletar todos os registros do banco de dados
def delete_all_records():
    try:
        Sale.objects.all().delete()
        Employee.objects.all().delete()
        Product.objects.all().delete()
        ProductCategory.objects.all().delete()
        Store.objects.all().delete()
        Region.objects.all().delete()
        print("Todos os registros foram removidos com sucesso.")
    except Exception as e:
        print(f"Ocorreu um erro ao remover os registros: {e}")

# Executando a função
delete_all_records()
