from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from news.views import *
from django.views.generic import TemplateView
from image.views import *
from gifa.views import IndexView
from teams.views import TeamsList,TeamdetailView,FeaturedTeamsList
from match.views import MatchList
from accounts.views import Userview,Logoutview,UserDetailView
from news.api_views import NewsListApiView,NewsDetailApiView
from teams.api_views import TeamsListApiView,TeamsDetailApiView
from image.api_views import ImagelistingApiView,ImageDisableApiView
from match.api_views import MatchlistingApiView
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView
from contact.views import *


urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', IndexView.as_view(),name="home"),
    url(r'^news/listing.htm$', NewsList.as_view(),{'html_id':'news'}),
    url(r'^teams/listing.htm$', TeamsList.as_view(),{'html_id':'team'}),
    url(r'^final-team/listing.htm$', FeaturedTeamsList.as_view(),{'html_id':'team'}),
    url(r'^matches.htm$', MatchList.as_view(),{'html_id':'match'}),
    url(r'^news/(?P<slug>[-\w]+)/article(?P<news_id>[-\w]+).htm$', NewsdetailView.as_view(),name="news_detail"),
    url(r'^team/(?P<slug>[-\w]+)/(?P<team_id>[-\w]+).htm$', TeamdetailView.as_view(),name="team_detail"),
    url(r'^write_article.htm', Addarticleview.as_view()),
    url(r'^writer.htm',TemplateView.as_view(template_name="writer.html")),
    url(r'^gurgaon-final.htm',TemplateView.as_view(template_name="gurgaon-final.html")),
    url(r'^delhi-final.htm',TemplateView.as_view(template_name="delhi-final.html")),
    url(r'^gallery.htm',ImageListview.as_view(),{'html_id':'gallery'}),
    url(r'^edit/article(?P<news_id>[-\w]+).htm$', Editarticleview.as_view()),
    url(r'^image/upload/',NewsImageview.as_view()),
    url(r'^upload_image.htm$',Imageview.as_view()),
    url(r'^approve-article.htm$', NewsapprovalView.as_view()),
    url(r'^approve-image.htm$', ImageapprovalView.as_view()),
    url(r'^profile/(?P<slug>[-\w]+)/(?P<user_id>[-\w]+).htm$', UserDetailView.as_view()),
    url(r'^gallery/(?P<image_id>[-\w]+).htm$', ImageDetail.as_view()),
    url(r'^api/news/listing/$', NewsListApiView.as_view()),
    url(r'^api/teams/listing/$', TeamsListApiView.as_view()),
    url(r'^api/news/detail/$', NewsDetailApiView.as_view()),
    url(r'^api/teams/detail/$', TeamsDetailApiView.as_view()),
    url(r'^api/image/listing/$', ImagelistingApiView.as_view()),
    url(r'^api/image_disable/$', ImageDisableApiView.as_view()),
    url(r'^api/match/listing/$', MatchlistingApiView.as_view()),
    url(r'^api/user_data/',Userview.as_view()),
    url(r'^api/logout_user/',Logoutview.as_view()),
    url(r'^api/mobileupload/image/',MobileImageUpload.as_view()),
    url(r'^api/news_enable/',SaveNews.as_view()),
    url(r'^api/news_reject/',RejectNews.as_view()),
    url(r'^api/image_enable/',SaveImage.as_view()),
    url(r'^api/image_reject/',RejectImage.as_view()),
    url(r'^api/query_resolved',QueryResolved.as_view()),
    url(r'^sponsors.htm',TemplateView.as_view(template_name="sponsers.html")),
    url(r'^rules.htm',TemplateView.as_view(template_name="rules.html")),
    url(r'^thankyou.htm', TemplateView.as_view(template_name="thankyou.html")),
    url(r'^venue/delhi.htm', TemplateView.as_view(template_name="venue_delhi.html"),{'html_id':'venue'}),
    url(r'^venue/gurgaon.htm', TemplateView.as_view(template_name="venue_gurgaon.html"),{'html_id':'venue'}),
    url(r'^contact.htm', ContactView.as_view(),{'html_id':'contact'}),
    url(r'^query-list.htm', ContactlistView.as_view()),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_ROOT}),

    
]

urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.STATIC_ROOT}),
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
        (r'^.*$', RedirectView.as_view(pattern_name='home')),
)