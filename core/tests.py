from django.test import TestCase
from .models import CrawlRequest, CrawlResult

class CrawlRequestModelTest(TestCase):
    def setUp(self):
        CrawlRequest.objects.create(url='http://example.com')

    def test_crawl_request_creation(self):
        crawl_request = CrawlRequest.objects.get(url='http://example.com')
        self.assertEqual(crawl_request.url, 'http://example.com')

class CrawlResultModelTest(TestCase):
    def setUp(self):
        crawl_request = CrawlRequest.objects.create(url='http://example.com')
        CrawlResult.objects.create(
            crawl_request=crawl_request,
            website='http://example.com',
            email='info@example.com',
        )

    def test_crawl_result_creation(self):
        crawl_request = CrawlRequest.objects.get(url='http://example.com')
        crawl_result = CrawlResult.objects.get(crawl_request=crawl_request)
        self.assertEqual(crawl_result.website, 'http://example.com')
        self.assertEqual(crawl_result.email, 'info@example.com')