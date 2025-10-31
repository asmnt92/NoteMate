from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from users.models import Profile
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from decouple import config

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
        
        


@receiver(post_save,sender=User)
def send_activation_email(sender, instance, created, **kwargs):
    if created:
        print
        token=default_token_generator.make_token(instance)
        activation_url=f"{settings.FRONTEND_URL}user/activate/{instance.id}/{token}/"

        subject = "Activate your account"
        body = (
            f"Hi {instance.username},\n\n"
            f"Thank you for signing up! Please activate your account by clicking the link below:\n"
            f"{activation_url}\n\n"
            f"If you didn’t create this account, please ignore this email."
        )
        try:

            send_mail(
                subject,
                body,
                settings.EMAIL_HOST_USER,
                [instance.email],
                fail_silently=False,
            )
        except Exception as e:
            print(e)
        print('**********************************')