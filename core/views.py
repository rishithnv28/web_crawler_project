import csv
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CrawlRequest, CrawlResult
from .crawling.scrapper import start_crawling

def home(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        crawl_request = CrawlRequest.objects.create(url=url)
        return redirect('crawl_status')
    return render(request, 'index.html')

def start_crawl(request):
    crawl_request = CrawlRequest.objects.last()
    start_crawling(crawl_request.url)
    return redirect('crawl_results')

def crawl_status(request):
    return render(request, 'status.html')

def crawl_results(request):
    results = CrawlResult.objects.all()
    if request.GET.get('download') == 'csv':
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="crawl_results.csv"'

        writer = csv.writer(response)
        writer.writerow([
            'Website', 'LinkedIn page', 'Address', 'E-mail', 'Phone', 'Products/services',
            'Revenue last three years', 'CEO', 'CEO LinkedIn URL', 'CEO Official email',
            'CFO', 'CFO LinkedIn', 'CFO Official email', 'Procurement Head', 
            'Procurement Head LinkedIn', 'Procurement Head Official email', 'SWOT Strengths', 
            'SWOT Weaknesses', 'SWOT Opportunities', 'SWOT Threats', 'Close Competitors'
        ])
        for result in results:
            writer.writerow([
                result.website, result.linkedin_page, result.address, result.email, result.phone,
                result.products_services, result.revenue_last_three_years, result.ceo, result.ceo_linkedin_url,
                result.ceo_official_email, result.cfo, result.cfo_linkedin_url, result.cfo_official_email,
                result.procurement_head, result.procurement_head_linkedin_url, result.procurement_head_official_email,
                result.swot_strengths, result.swot_weaknesses, result.swot_opportunities, result.swot_threats,
                result.close_competitors
            ])
        return response
    return render(request, 'result.html', {'results': results})