from django.contrib import admin

from .models import Building, Bathroom

class BathroomInline(admin.TabularInline):
    model = Bathroom
    extra = 3


class BuildingAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['building_name']}),
        # ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [BathroomInline]

admin.site.register(Building, BuildingAdmin)
