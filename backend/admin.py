from django import forms
from django.contrib import admin
from .models import Product, Customer, Order, Category


class ProductAdminForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':5,'cols':80}))

    class Meta:
        model = Product
        fields = '__all__'
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','description','stock']


admin.site.register(Product,ProductAdmin)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Category)

