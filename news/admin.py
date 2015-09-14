from django.contrib import admin
from news.models import FeaturedNews

class FeaturedAdmin(admin.ModelAdmin):
    model = FeaturedNews
    list_display = ['get_news','enabled' ]

    def get_news(self, obj):
        return obj.faetured_news.title


admin.site.register(FeaturedNews,FeaturedAdmin)

# Register your models here.
