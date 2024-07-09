import csv
from core.models import CrawlRequest, CrawlResult

def start_crawling(url):
    # Simulate reading from the CSV file
    csv_file_path = 'core/crawling/sample_data.csv'
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            crawl_request = CrawlRequest.objects.create(url=url)
            CrawlResult.objects.create(
                crawl_request=crawl_request,
                website=row['Website'],
                linkedin_page=row['LinkedIn page'],
                address=row['Address'],
                email=row['E-mail'],
                phone=row['Phone'],
                products_services=row['Products/services'],
                revenue_last_three_years=row['Revenue last three years'],
                ceo=row['CEO'],
                ceo_linkedin_url=row['CEO LinkedIn URL'],
                ceo_official_email=row['CEO Official email'],
                cfo=row['CFO'],
                cfo_linkedin_url=row['CFO LinkedIn'],
                cfo_official_email=row['CFO Official email'],
                procurement_head=row['Procurement Head'],
                procurement_head_linkedin_url=row['Procurement Head LinkedIn'],
                procurement_head_official_email=row['Procurement Head Official email'],
                swot_strengths=row['SWOT Strengths'],
                swot_weaknesses=row['SWOT Weaknesses'],
                swot_opportunities=row['SWOT Opportunities'],
                swot_threats=row['SWOT Threats'],
                close_competitors=row['Close Competitors']
            )