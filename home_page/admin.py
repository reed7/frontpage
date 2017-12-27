from django.contrib import admin
from .models import MyProfile, QuestionAnswer, ContactMethod


class ContactMethodAdmin(admin.ModelAdmin):
    list_display = ["id", "profile", "contact_type", "address"]


class QAAdmin(admin.ModelAdmin):
    list_display = ["id", "profile", "question", "display", "display_order"]

admin.site.register(MyProfile)
admin.site.register(QuestionAnswer, QAAdmin)
admin.site.register(ContactMethod, ContactMethodAdmin)
