from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from agency.models import Redactor, Topic, Newspaper


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ["name",]
    list_filter = ["name",]
    search_fields = ["name",]


@admin.register(Redactor)
class RedactorAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("years_of_experience",)
    fieldsets = UserAdmin.fieldsets + (("Important data", {"fields": ("years_of_experience",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((
                                                   "Important data", {
                                                       "fields": (
                                                           "years_of_experience",
                                                           "first_name",
                                                           "last_name",
                                                       )
                                                   }
                                               ),)


@admin.register(Newspaper)
class TopicAdmin(admin.ModelAdmin):
    list_display = ["title", "topic", "published_date",]
    list_filter = ["published_date",]
    search_fields = ["name",]
