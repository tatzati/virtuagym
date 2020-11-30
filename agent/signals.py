from django.db.models.signals import post_save
from django.dispatch import receiver

from agent.models import User
from virtuagym.common.utils import email_to


@receiver(post_save, sender=User)
def post_save(sender, instance, created, **kwargs):
    if not created:
        update_fields = kwargs.get('update_fields') or set()

        # value of `plan` has changed:
        if 'plan' in update_fields:
            email_to(instance.email, instance.plan.name)
