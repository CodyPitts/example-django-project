from django.contrib import admin
from .models import Event, Speaker, Session, FeaturedSession, LightningTalk

# Register your models here.


admin.site.register(Event)
admin.site.register(Speaker)
admin.site.register(Session)
# admin.site.register(Sponsor)
admin.site.register(FeaturedSession)
admin.site.register(LightningTalk)
