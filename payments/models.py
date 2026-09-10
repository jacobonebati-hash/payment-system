from decimal import Decimal
from django.db import models


class Member(models.Model):
    jina = models.CharField(max_length=200)

    simu = models.CharField(
        max_length=20,
        blank=True
    )

    eneo = models.CharField(
        max_length=150,
        blank=True
    )

    kiasi_anachotakiwa = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=Decimal("0.00")
    )

    tarehe_ya_mwisho = models.DateField(
        null=True,
        blank=True
    )

    tarehe_ya_usajili = models.DateTimeField(
        auto_now_add=True
    )

    active = models.BooleanField(
        default=True
    )

    def jumla_ya_malipo(self):
        total = self.payments.aggregate(
            total=models.Sum("kiasi")
        )["total"]

        return total or Decimal("0.00")

    def deni(self):
        deni = (
            self.kiasi_anachotakiwa
            - self.jumla_ya_malipo()
        )

        return max(
            deni,
            Decimal("0.00")
        )

    def status(self):
        if self.deni() <= 0:
            return "AMEMALIZA"

        return "ANA DENI"

    def __str__(self):
        return self.jina


class Payment(models.Model):

    PAYMENT_METHODS = [
        ("Cash", "Cash"),
        ("M-Pesa", "M-Pesa"),
        ("Airtel Money", "Airtel Money"),
        ("Mixx by Yas", "Mixx by Yas"),
        ("Halopesa", "Halopesa"),
        ("Benki", "Benki"),
        ("Nyingine", "Nyingine"),
    ]

    member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
        related_name="payments"
    )

    kiasi = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    payment_method = models.CharField(
        max_length=50,
        choices=PAYMENT_METHODS,
        default="Cash"
    )

    transaction_number = models.CharField(
        max_length=100,
        blank=True
    )

    tarehe = models.DateTimeField(
        auto_now_add=True
    )

    maelezo = models.TextField(
        blank=True
    )

    def __str__(self):
        return f"{self.member.jina} - {self.kiasi}"