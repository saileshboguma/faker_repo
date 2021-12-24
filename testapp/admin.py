from django.contrib import admin
from testapp.models import *
# Register your models here.
class HydjobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

class BangalorejobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

class ChennaijobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

class PunejobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']


admin.site.register(Hydjob,HydjobsAdmin)
admin.site.register(Bangalorejob,BangalorejobsAdmin)
admin.site.register(Chennaijob,ChennaijobsAdmin)
admin.site.register(Punejob,PunejobsAdmin)
