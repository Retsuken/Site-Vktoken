from django.contrib import admin
from .models import Vk, Squad


@admin.register(Vk)
class VkAdmin(admin.ModelAdmin):
    fields = ['nick', 'id_vk', 'token_vk']


admin.site.register(Squad)