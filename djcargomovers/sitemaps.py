from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
class StaticViewSitemap(Sitemap):
    def items(self):
        return ['index','about_us','view_core_service','intustry_service','Specialized_Logistic','feight_Quote','track','add_feedback']
    def location(self, item):
    	return reverse(item)    