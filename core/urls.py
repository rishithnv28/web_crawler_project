from django.urls import path
from .views import home, start_crawl, crawl_status, crawl_results

urlpatterns = [
    path('', home, name='home'),
    path('start-crawl/', start_crawl, name='start_crawl'),
    path('crawl-status/', crawl_status, name='crawl_status'),
    path('crawl-results/', crawl_results, name='crawl_results'),
]