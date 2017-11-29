from django.core.management.base import BaseCommand

from juntagrico.models import *


class Command(BaseCommand):
    # entry point used by manage.py
    def handle(self, *args, **options):
        for user in User.objects.all():
            if user.is_superuser:
                signals.post_save.disconnect(Member.create, sender=Member)
                member = Member.objects.create(user=user, first_name='super', last_name='duper', email=user.email,
                                               addr_street='superstreet', addr_zipcode='8000',
                                               addr_location='SuperCity', phone='012345678', confirmed=True)
                member.save()
                user.member = member
                user.save()
                signals.post_save.connect(Member.create, sender=Member)
