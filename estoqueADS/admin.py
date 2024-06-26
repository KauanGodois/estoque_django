from django.contrib import admin
from .models import Produtos, Categoria

class adminProdutos(admin.ModelAdmin):
    list_display = ['id', 'nome', 'preco', 'quantidade', 'em_estoque', 'categoria']
    list_filter = ['em_estoque']
    search_fields = ['nome']
    list_editable = ['quantidade']
    list_per_page = 5

admin.site.register(Produtos, adminProdutos)
admin.site.register(Categoria)


# Register your models here.
