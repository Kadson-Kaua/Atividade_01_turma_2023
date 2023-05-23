from django.contrib import admin
from .models import categoria, cliente, locacao, filme
# Register your models here.


@admin.register(categoria)
class Admincategoria(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(cliente)
class Admincliente(admin.ModelAdmin):
    list_display = ('nome','email',)

@admin.register(filme)
class Adminfilme(admin.ModelAdmin):
    list_display = ('titulo','valor',)

@admin.register(locacao)
class Adminregister(admin.ModelAdmin):
    list_display = ('nome','data',)