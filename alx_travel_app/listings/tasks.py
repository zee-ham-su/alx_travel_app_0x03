from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_booking_confirmation_email(booking_id):
    from listings.models import Booking
    booking = Booking.objects.get(id=booking_id)
    subject = f'Booking Confirmation for {booking.listing.title}'
    message = f'Hi {booking.user.username},\n\nYour booking for {booking.listing.title} has been confirmed!'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [booking.user.email]
    send_mail(subject, message, email_from, recipient_list)
