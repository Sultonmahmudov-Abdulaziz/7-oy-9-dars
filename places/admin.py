from django.contrib import admin
from .models import Owner ,Place ,PlaceOwner ,Comment


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('id','first_name', 'last_name', 'email')
    search_fields = ('first_name','last_name','email')


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'address')
    search_fields = ('name',)
    list_display_links = ('name', )


class PlaceOwnerAdmin(admin.ModelAdmin):
    list_display = ('id','place', 'owner')
    search_fields = ('owner',)







admin.site.register(Place, PlaceAdmin)
admin.site.register(Owner, OwnerAdmin)
admin.site.register(PlaceOwner, PlaceOwnerAdmin)
admin.site.register(Comment)

