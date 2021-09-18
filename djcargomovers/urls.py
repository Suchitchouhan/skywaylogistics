"""djcargomovers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls import url
from django.http import HttpResponse
from package.views import *
from django.conf.urls.static import static
from django.conf import settings
from cmr.views import *
from django.contrib.sitemaps.views import sitemap
from djcargomovers.sitemaps import StaticViewSitemap
sitemaps = {
    'static': StaticViewSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",index,name="index"),
    path("about_us",about_us,name="about_us"),
    path("view_core_service",view_core_service,name="view_core_service"),
    path("intustry_service",intustry_service,name="intustry_service"),
    path("Specialized_Logistic",Specialized_Logistic,name="Specialized_Logistic"),
    path("feight_Quote",feight_Quote,name='feight_Quote'),
    path("track",track,name="track"),
    path("login_view",login_view,name="login_view"),
    path("logout_view",logout_view,name="logout_view"),
    path("panel",panel),
    path("view_contact_us",view_contact_us),
    path("view_feight",view_feight),
    path("add_consignment",add_consignment),
    path('view_consignment',view_consignment,name='view_consignment'),
    path('add_single_consignment',add_single_consignment,name='add_single_consignment'),
    path('update_single_consignment/<str:uid>',update_single_consignment,name='update_single_consignment'),
    path("add_shipping_history/<int:pk>",add_shipping_history,name='add_shipping_history'),
    path('view_shippment_history/<int:pk>',view_shippment_history,name='view_shippment_history'),
    path('delete_shippment_history/<int:pk>',delete_shippment_history,name='delete_shippment_history'),
    path('update_shipping_history/<int:pk>',update_shipping_history,name='update_shipping_history'),
    path('add_pof/<int:pk>',add_pof),
    path('add_feedback',add_feedback,name='add_feedback'),
    path('view_feedback',view_feedback),
    path('view_slider',view_slider),
    path('delete_slider/<int:pk>',delete_slider),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),    
    url(r'^robots.txt', lambda x: HttpResponse("User-Agent: *\nDisallow:", content_type="text/plain"), name="robots_file"),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
