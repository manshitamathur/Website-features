from django.contrib import admin
from .models import Subscriber,Newsletter,Mentor_TV2,MTV_Category
from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import Mentor_TV

admin.site.register(Subscriber)
# Register your models here.
# admin.site.register(SubscribeModel)
# admin.site.register(Subscriber)

def send_newsletter(modeladmin, request, queryset):
    for newsletter in queryset:
        newsletter.send(request)

send_newsletter.short_description = "Send selected Newsletters to all subscribers"


class NewsletterAdmin(admin.ModelAdmin):
    actions = [send_newsletter]

admin.site.register(Newsletter,NewsletterAdmin)


class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Mentor_TV, MyModelAdmin)


admin.site.register(MTV_Category)
admin.site.register(Mentor_TV2)


