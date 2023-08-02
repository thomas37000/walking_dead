from django.contrib import admin

from characters.models import Character, CharactersList

admin.site.site_header = "Walking Dead admin"
admin.site.site_title = "admin"
admin.site.index_title = "Users & Tables"

class CharacterInline(admin.TabularInline):
    model=Character
    extra=0

@admin.register(CharactersList)
class CharactersListAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = (CharacterInline,)
    
@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    
    list_display = ('name','lastname', 'is_alive')
    list_filter = ('name', 'is_alive')
    search_fields = ('name', )
