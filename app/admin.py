from django.contrib import admin
from .models import User,Photographer,Event,Rating, PhotographerAccount,BoughtPhotos,Portfolio,PhotographerAccount,BoughtPhotos,Photos,PhotoUsers

# Register your models here

admin.site.register(User)
admin.site.register(Photographer)
admin.site.register(Event)
admin.site.register(Rating)
admin.site.register(PhotographerAccount)
admin.site.register(BoughtPhotos)
admin.site.register(Portfolio)
admin.site.register(PhotographerAccount)
admin.site.register(BoughtPhotos)
admin.site.register(Photos)
admin.site.register(PhotoUsers)