from django.utils import timezone

def calculate_default_date():
    now = timezone.now()
    delta = timezone.timedelta(days=7)

    default_date = now + delta

    return default_date.date()