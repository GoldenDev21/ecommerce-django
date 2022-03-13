from celery import shared_task
from celery.utils.log import get_task_logger
from datetime import datetime
from store.models import PromoCode

logger = get_task_logger(__name__)

@shared_task
def check_for_expired_promo_codes():
    today = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    PromoCode.objects.create(active=True, code="FREE20", discount_percent=15, type=1, expiration_date='03/25/2022 11:59:59')
    active_promo_codes = PromoCode.objects.filter(active=True)
    for promo_code in active_promo_codes:
        exp = promo_code.expiration_date.strptime("%m/%d/%Y %H:%M:%S")
        if exp < today:
            promo_code.active = False
            promo_code.save()
        else:
            print('faeifoajw')
