from django.core.management.base import BaseCommand
from search_replicas.models import CompanySearchReplica

from main.models import Company


class Command(BaseCommand):
    help = 'reindex active company from Company to CompanySearchReplica'

    def handle(self, *args, **options):
        company_replicas_count = CompanySearchReplica.objects.count()
        CompanySearchReplica.objects.all().delete()
        msg = f'Successfully deleted company_replicas: {company_replicas_count}'
        self.stdout.write(self.style.SUCCESS(msg))
        companies_count = Company.objects.moderated().count()
        for index, company in enumerate(Company.objects.moderated().iterator(), start=1):
            company.reindex()
            msg = f'... indexed {index} of {companies_count}'
            self.stdout.write(msg)
        msg = 'reindex has been done'
        self.stdout.write(self.style.SUCCESS(msg))
