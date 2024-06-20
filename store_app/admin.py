from django.contrib import admin


from .models import Categories,Brand,Color,Filter_Price,Product,Images,Tag,Contact_us,Order,Orderitem


class ImagesTublerinline(admin.TabularInline):
    model=Images

class TagTublerinline(admin.TabularInline):
    model=Tag

class ProductAdmin(admin.ModelAdmin):
    inlines=[ImagesTublerinline,TagTublerinline]        

class OrderitemTabularInline(admin.TabularInline):
    model = Orderitem
    extra = 1  # Optional: the number of extra forms the formset will display

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderitemTabularInline]


# class OrderitemTublerinline(admin.TabularInline):
#     model=Orderitem
    
 
# class OrderAdmin(admin.TabularInline):
#     inlines = [OrderitemTublerinline]
    
       
admin.site.register(Images)
admin.site.register(Tag)

# Register your models here.
admin.site.register(Categories)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Filter_Price)
admin.site.register(Product,ProductAdmin)
admin.site.register(Contact_us)

admin.site.register(Order, OrderAdmin)
admin.site.register(Orderitem)