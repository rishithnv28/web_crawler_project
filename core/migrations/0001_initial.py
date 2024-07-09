# Generated by Django 5.0.6 on 2024-07-08 10:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CrawlRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CrawlResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.URLField()),
                ('linkedin_page', models.URLField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('products_services', models.TextField(blank=True, null=True)),
                ('revenue_last_three_years', models.TextField(blank=True, null=True)),
                ('ceo', models.CharField(blank=True, max_length=100, null=True)),
                ('ceo_linkedin_url', models.URLField(blank=True, null=True)),
                ('ceo_official_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('cfo', models.CharField(blank=True, max_length=100, null=True)),
                ('cfo_linkedin_url', models.URLField(blank=True, null=True)),
                ('cfo_official_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('procurement_head', models.CharField(blank=True, max_length=100, null=True)),
                ('procurement_head_linkedin_url', models.URLField(blank=True, null=True)),
                ('procurement_head_official_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('swot_strengths', models.TextField(blank=True, null=True)),
                ('swot_weaknesses', models.TextField(blank=True, null=True)),
                ('swot_opportunities', models.TextField(blank=True, null=True)),
                ('swot_threats', models.TextField(blank=True, null=True)),
                ('close_competitors', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('crawl_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.crawlrequest')),
            ],
        ),
    ]
