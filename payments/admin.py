from django.contrib import admin

from .models import Member, Payment


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):

    list_display = (
        "jina",
        "simu",
        "eneo",
        "kiasi_anachotakiwa",
        "display_paid",
        "display_debt",
        "display_status",
    )

    search_fields = (
        "jina",
        "simu",
    )

    list_filter = (
        "active",
    )

    def display_paid(self, obj):

        return obj.jumla_ya_malipo()

    display_paid.short_description = "Alicholipa"

    def display_debt(self, obj):

        return obj.deni()

    display_debt.short_description = "Deni"

    def display_status(self, obj):

        return obj.status()

    display_status.short_description = "Status"


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):

    list_display = (
        "member",
        "kiasi",
        "payment_method",
        "transaction_number",
        "tarehe",
    )

    search_fields = (
        "member__jina",
        "transaction_number",
    )

    list_filter = (
        "payment_method",
    )