from django.urls import path

from . import views


urlpatterns = [

    path(
        "",
        views.dashboard,
        name="dashboard"
    ),

    path(
        "members/",
        views.member_list,
        name="member_list"
    ),

    path(
        "members/add/",
        views.member_create,
        name="member_create"
    ),

    path(
        "members/<int:pk>/",
        views.member_detail,
        name="member_detail"
    ),

    path(
        "payments/add/",
        views.payment_create,
        name="payment_create"
    ),

    path(
        "import-excel/",
        views.import_excel,
        name="import_excel"
    ),

    path(
        "export-excel/",
        views.export_excel,
        name="export_excel"
    ),

    path(
        "members/<int:pk>/excel/",
        views.download_member_excel,
        name="download_member_excel"
    ),
]