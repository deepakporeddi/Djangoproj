from django.contrib import admin
from .models import Collection,Product,Order,Cart,OrderItem,Promotions,Customer,Address,CartItem
admin.site.register(Product)
admin.site.register(Collection)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(OrderItem)
admin.site.register(Promotions)
#admin.site.register(Customer)
admin.site.register(Address)
admin.site.register(CartItem)
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('last_name','first_name','email')
    list_filter = ('last_name','membership')
