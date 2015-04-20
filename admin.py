from django.contrib import admin
from calendario.apps.cal.models import calendario

class calenAdmin(admin.ModelAdmin):
   list_display = ["creador", "fecha", "titulo", "snippet"]
   search_fields = ["titulo", "snippet"]
   list_filter = ["creador"]

admin.site.register(calendario,calenAdmin)
