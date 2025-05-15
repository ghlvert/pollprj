from django.contrib import admin

from pollapp.models import Variant, Poll

# Register your models here.

class VariantInline(admin.StackedInline):
    model = Variant
    extra = 3

@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    fields = ['title', 'text']
    inlines = [VariantInline,]