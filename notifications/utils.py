from django.core.mail import send_mail
from decouple import config

def send_notification_email(user, subject, message):
    if not hasattr(user, 'notificationpreference'):
        return

    if user.notificationpreference.email_notifications:
        send_mail(
            subject,
            message,
            config('DEFAULT_FROM_EMAIL', default='no-reply@example.com'),
            [user.email],
            fail_silently=True,
        )
def format_notification_message(notification):
    if notification.task:
        return f"Task '{notification.task.title}' - {notification.message}"
    return notification.message
