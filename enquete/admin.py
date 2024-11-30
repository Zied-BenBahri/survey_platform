from django.contrib import admin
from .models import *
# Register your models here.
"""
class InlineAgent(admin.TabularInline):
    model = Agent

class AgentAdmin(admin.ModelAdmin):
    list_display = ("__str__","gouvernorat")
    list_filter =("gouvernorat",)

"""

class InlineLocalite(admin.TabularInline):
    model = Localite

class InlineDelegation(admin.TabularInline):
    model = Delegation

class EnqueteAdmin(admin.ModelAdmin):
    list_display = ("__str__","created_at","agent","localite")
    list_filter = ("created_at","agent","localite")


class UserAdmin(admin.ModelAdmin):
    #inlines = [InlineAgent]
    list_display = ("__str__","is_staff","email","date_joined")
    list_filter = ("is_staff","date_joined")
    search_fields = ("username",)


class LocaliteAdmin(admin.ModelAdmin):
    list_display = ("__str__","delegation")
    list_filter =("delegation",)
    search_fields = ("libelle",)


class delegationAdmin(admin.ModelAdmin):
    inlines = [InlineLocalite]
    list_display = ("__str__","gouvernorat")
    list_filter =("gouvernorat",)
    search_fields = ("libelle",)
    
class GouvAdmin(admin.ModelAdmin):
    inlines = [InlineDelegation]
    search_fields = ("libelle",)





  
admin.site.register(User,UserAdmin)
admin.site.register(Enquete,EnqueteAdmin)
#admin.site.register(Agent,AgentAdmin)
admin.site.register(Gouvernorat,GouvAdmin)
admin.site.register(Delegation,delegationAdmin)
admin.site.register(Localite,LocaliteAdmin)