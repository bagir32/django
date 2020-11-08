from django.contrib import admin
from .models import Product
# Register your models here.
# DataFlair

# Admin Action Functions
def change_rating(modeladmin, request, queryset):
    queryset.update(rating = 'e')


# Action description
change_rating.short_description = "Mark Selected Products as Excellent"




# ModelAdmin Class # DataFlair
class ProductA(admin.ModelAdmin):

    list_filter = ('mfg_date', 'name', 'rating' )
    list_display = ('name', 'description', 'mfg_date')
    actions = [change_rating]

# add any product you register in your model
admin.site.register(Product, ProductA)


## remove those apps from admin
#admin.site.unregister(Groups)
admin.site.site_header = "Sudanes IT Python Group -DataFlair Django Tutorials"

