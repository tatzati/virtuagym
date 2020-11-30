# from django.db.models.signals import post_save
# from django.dispatch import receiver

# from plan.models import Plan
# from virtuagym.common.utils import email_to


# @receiver(post_save, sender=Plan)
# def post_save(sender, instance, created, **kwargs):
#     if created:
        # print(sender, instance, kwargs)
        # value of `users` has changed:
        # for user in instance.id:
        #     email_to(user.email, instance.name)
