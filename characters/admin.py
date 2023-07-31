from django.contrib import admin

from characters.models import Character, CharactersList

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
