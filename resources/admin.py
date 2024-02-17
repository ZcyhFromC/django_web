from django.contrib import admin

from resources.models import ResourceNode, ResourceGroup

from mptt.admin import MPTTModelAdmin

class ResourceGroupAdmin(admin.ModelAdmin):
    filter_horizontal = ['nodes']

class ResourceNodeMPTTModelAdmin(MPTTModelAdmin):
    mptt_level_indent = 20

admin.site.register(ResourceNode, ResourceNodeMPTTModelAdmin)
admin.site.register(ResourceGroup, ResourceGroupAdmin)

