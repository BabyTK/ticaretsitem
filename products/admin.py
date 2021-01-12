from django.contrib import admin
from products.models import Category, Product, Images
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
from django.utils.html import format_html


# class ProductImageInline(admin.TabularInline):
#     model = Images
#     extra = 5 #Eklenebilecek fotoğraf sayısı

class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'status'
    ]

    list_filter = [
        'status'
    ]


class ProductAdmin(admin.ModelAdmin):
    fields = (

        'title',
        'image_tag',
        'image',
        'image2',
        'image3',
        'description',
        'category',
        'price',
        'amount',
        'status',
        'slug',
        'keywords',
        'detail'

    )

    list_display = [

        'title',
        'category',
        'price',
        'status',
        'image_tag',
    ]

    readonly_fields = (
        'image_tag',
    )

    list_filter = [
        'status'
    ]

    prepopulated_fields = {
        'slug': ('title',)
    }
    # inlines = [ProductImageInline] #ürün ekleme anında fotoğraf ekleyebilmek için


class ImagesAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'product',
        'image'
    ]


class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('title',)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
            qs,
            Product,
            'category',
            'products_cumulative_count',
            cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(
            qs,
            Product,
            'category',
            'products_count',
            cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count

    related_products_count.short_description = ''

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count

    related_products_cumulative_count.short_description = ''


admin.site.register(Category, CategoryAdmin2)
admin.site.register(Product, ProductAdmin)
admin.site.register(Images, ImagesAdmin)