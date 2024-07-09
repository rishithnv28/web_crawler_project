from django.db import models

class CrawlRequest(models.Model):
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.url

class CrawlResult(models.Model):
    crawl_request = models.ForeignKey(CrawlRequest, on_delete=models.CASCADE)
    website = models.URLField()
    linkedin_page = models.URLField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    products_services = models.TextField(null=True, blank=True)
    revenue_last_three_years = models.TextField(null=True, blank=True)
    ceo = models.CharField(max_length=100, null=True, blank=True)
    ceo_linkedin_url = models.URLField(null=True, blank=True)
    ceo_official_email = models.EmailField(null=True, blank=True)
    cfo = models.CharField(max_length=100, null=True, blank=True)
    cfo_linkedin_url = models.URLField(null=True, blank=True)
    cfo_official_email = models.EmailField(null=True, blank=True)
    procurement_head = models.CharField(max_length=100, null=True, blank=True)
    procurement_head_linkedin_url = models.URLField(null=True, blank=True)
    procurement_head_official_email = models.EmailField(null=True, blank=True)
    swot_strengths = models.TextField(null=True, blank=True)
    swot_weaknesses = models.TextField(null=True, blank=True)
    swot_opportunities = models.TextField(null=True, blank=True)
    swot_threats = models.TextField(null=True, blank=True)
    close_competitors = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f'{self.website} - {self.created_at}'