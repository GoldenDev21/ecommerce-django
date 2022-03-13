from celery import shared_task
from celery.utils.log import get_task_logger
from store.models import PromoCode
from django.utils import timezone

logger = get_task_logger(__name__)

@shared_task
def check_for_expired_promo_codes():
    now = timezone.now()
    active_promo_codes = PromoCode.objects.filter(active=True)
    for promo_code in active_promo_codes:
        if promo_code.expiration_date:
            if promo_code.expiration_date < now:
                promo_code.active = False
                promo_code.save()
