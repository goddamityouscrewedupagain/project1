from django.core.management.base import BaseCommand, CommandError
from search_replicas.models import CompanySearchReplica


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        for company in CompanySearchReplica.objects.all():
            if CompanySearchReplica.objects.filter(company_id=company.company_id).count() > 1:
                company.delete()