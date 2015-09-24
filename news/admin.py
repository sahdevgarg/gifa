from django.contrib import admin
from news.models import FeaturedNews,News

class FeaturedAdmin(admin.ModelAdmin):
    model = FeaturedNews
    list_display = ['get_news','enabled' ]

    def get_news(self, obj):
        return obj.faetured_news.title

class NewsAdmin(admin.ModelAdmin):
    model = News
    list_display = ['title','enabled','rejected','tags','team_a' ]
    exclude = ('content','coverimage','fb_id')
    search_fields = ['title']


    def get_news(self, obj):
        return obj.faetured_news.title

admin.site.register(News,NewsAdmin)
admin.site.register(FeaturedNews,FeaturedAdmin)

# Register your models here.
