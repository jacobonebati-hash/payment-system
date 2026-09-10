from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Payment, Member
from .excel import generate_member_excel


@receiver(post_save, sender=Payment)
def payment_saved(sender, instance, created, **kwargs):
    """
    Kila malipo mapya yakihifadhiwa,
    Excel ya mwanachama inasasishwa.
    """
    generate_member_excel(instance.member)


@receiver(post_delete, sender=Payment)
def payment_deleted(sender, instance, **kwargs):
    """
    Malipo yakifutwa,
    Excel inasasishwa tena.
    """
    generate_member_excel(instance.member)


@receiver(post_save, sender=Member)
def member_saved(sender, instance, created, **kwargs):
    """
    Mwanachama akitengenezwa/kusasishwa,
    Excel yake inatengenezwa.
    """
    generate_member_excel(instance)