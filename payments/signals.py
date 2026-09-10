from django.db.models.signals import (
    post_save,
    post_delete
)

from django.dispatch import receiver

from .models import Member, Payment
from .excel import generate_member_excel


@receiver(
    post_save,
    sender=Payment
)
def payment_saved(
    sender,
    instance,
    created,
    **kwargs
):

    generate_member_excel(
        instance.member
    )


@receiver(
    post_delete,
    sender=Payment
)
def payment_deleted(
    sender,
    instance,
    **kwargs
):

    generate_member_excel(
        instance.member
    )


@receiver(
    post_save,
    sender=Member
)
def member_saved(
    sender,
    instance,
    created,
    **kwargs
):

    generate_member_excel(
        instance
    )