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
    list_display = UserAdmin.list_display + ("years_of_experiments",)
    fieldsets = UserAdmin.fieldsets + (("Important data", {"fields": ("years_of_experiments",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((
                                                   "Important data", {
                                                       "fields": (
                                                           "years_of_experiments",
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
