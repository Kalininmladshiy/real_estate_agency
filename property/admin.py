from django.contrib import admin

from .models import Flat, Complaint, Owner


class PropertyownerInline(admin.TabularInline):
    model = Flat.flats_by.through
    raw_id_fields = ('owner', 'flat')

@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address')
    readonly_fields = ('created_at',)
    list_display = ('address','price','new_building','construction_year', 'town')
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony', 'floor')
    raw_id_fields = ('liked_by',)
    inlines = [PropertyownerInline,]

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'flat')

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)
    
