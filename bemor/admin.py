from django.contrib import admin
from import_export.admin import ExportMixin
from .models import Manzil, OperatsiyaBolganJoy, Jinsi, BemorningHolati, Bemor


class BemorInline(admin.TabularInline):  # Bemorlarni boshqa adminlarda ichki jadval sifatida ko‘rsatish
    model = Bemor
    extra = 1
    autocomplete_fields = ['jinsi', 'manzil', 'bemor_holati']


@admin.register(Manzil)
class ManzilAdmin(ExportMixin, admin.ModelAdmin):  # Export funksiyasi qo‘shildi
    list_display = ('mamlakat', 'hudud', 'tuman', 'mahalla', 'kocha_nomi', 'biriktirilgan_tuman')
    search_fields = ('mamlakat', 'hudud', 'tuman', 'mahalla')
    list_filter = ('mamlakat', 'hudud', 'tuman')
    ordering = ('mamlakat', 'hudud', 'tuman')
    list_per_page = 20


@admin.register(OperatsiyaBolganJoy)
class OperatsiyaBolganJoyAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ('mamlakat', 'operatsiya_bolgan_joy', 'transplantatsiya_sana', 'operatsiya_oxirlangan_sana', 'ishlatilgan_miqdor')
    search_fields = ('mamlakat', 'operatsiya_bolgan_joy')
    list_filter = ('mamlakat', 'transplantatsiya_sana')
    ordering = ('transplantatsiya_sana',)
    date_hierarchy = 'transplantatsiya_sana'
    list_per_page = 20


@admin.register(Jinsi)
class JinsiAdmin(admin.ModelAdmin):
    list_display = ('gender',)
    list_filter = ('gender',)
    search_fields = ('gender',)
    ordering = ('gender',)


@admin.register(BemorningHolati)
class BemorningHolatiAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ('holati', 'ozgarish')
    search_fields = ('holati',)
    ordering = ('holati',)
    list_per_page = 20


@admin.register(Bemor)
class BemorAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ('ism', 'familiya', 'tugilgan_sana', 'jinsi', 'manzil', 'bemor_holati', 'arxivga_olingan_sana')
    search_fields = ('ism', 'familiya', 'JSHSHIR')
    list_filter = ('jinsi', 'tugilgan_sana', 'arxivga_olingan_sana')
    date_hierarchy = 'tugilgan_sana'
    autocomplete_fields = ('jinsi', 'manzil', 'bemor_holati', 'operatsiya_bolgan_joy')
    ordering = ('tugilgan_sana',)
    list_per_page = 20
    fieldsets = (
        ('Shaxsiy ma’lumotlar', {
            'fields': ('JSHSHIR', 'ism', 'familiya', 'tugilgan_sana', 'jinsi')
        }),
        ('Qo‘shimcha ma’lumotlar', {
            'fields': ('manzil', 'bemor_holati', 'operatsiya_bolgan_joy', 'qoshimcha_malumotlar'),
            'classes': ('collapse',)
        }),
        ('Arxiv', {
            'fields': ('arxivga_olingan_sana', 'biriktirilgan_file'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('arxivga_olingan_sana',)  # O‘zgartirib bo‘lmaydigan maydon

