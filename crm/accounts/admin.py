from django.contrib import admin
from .models import*
from django.utils.html import format_html

# Register your models here.

admin.site.site_header = "ACLEDA University of Business"
admin.site.site_title = "AUB Admin Panel"
admin.site.index_title = "Dashboard Panel"

admin.site.register(Category)


admin.site.register(Product)
admin.site.register(ProductDetail)

# class ProductAdmin(admin.ModelAdmin):
#     def image_preview(self, obj):
#         if obj.productImage:
#             return format_html('<img src="/static{}" style="width: 100px; height: auto;" />', obj.productImage.url)
#         return "No Image"

#     list_display = ["image_preview", "productName", "categoryId", "quantity", "price", "productDate"]
#     list_filter = ["productDate"]
#     search_fields = ["productName"]
#     date_hierarchy = "productDate"
#     list_per_page = 2
#     readonly_fields = ["image_preview"]
#     image_preview.short_description = 'Image preview'

# admin.site.register(Products, ProductAdmin)

admin.site.register(CarouselSlide)
admin.site.register(BannerOffer)
admin.site.register(PromoBox)
admin.site.register(Banner)
admin.site.register(BillingDetail)