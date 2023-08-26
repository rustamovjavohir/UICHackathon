from django.contrib import admin
from apps.product.models import Pet, Category, Tag


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category_pretty', 'status', 'tags_pretty')
    list_display_links = ('id', 'name')
    readonly_fields = ('slug', 'created_at', 'updated_at')

    def category_pretty(self, obj):
        if obj.category:
            return obj.category.name.capitalize()
        return '-'

    category_pretty.short_description = 'Категория'

    def photoUrls_pretty(self, obj):
        if obj.photoUrls.objects.all():
            return ",\n".join([p.name.capitalize() for p in obj.photoUrls.objects.all()])
        return '-'

    photoUrls_pretty.short_description = 'Фото питомца'

    def tags_pretty(self, obj):
        if obj.tags.all():
            return ",\n".join([p.name.capitalize() for p in obj.tags.all()])
        return '-'

    tags_pretty.short_description = 'Теги'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent')
    list_display_links = ('id', 'name')
    list_filter = ('parent',)
    search_fields = ('name',)
    empty_value_display = '-пусто-'
    readonly_fields = ('slug', 'created_at', 'updated_at')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    empty_value_display = '-пусто-'
    readonly_fields = ('slug', 'created_at', 'updated_at')
