from django.contrib import admin
from .models import Event, Speaker, Session

# Register your models here.


admin.site.register(Event)
admin.site.register(Speaker)
admin.site.register(Session)
# admin.site.register(Sponsor)
