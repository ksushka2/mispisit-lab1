from django.shortcuts import render


def home(request):
    return render(
        request,
        "core/home.html",
        {
            "product_name": "IT-Школа",
            "description": (
                "Информационная система детской IT-школы для приёма заявок, "
                "распределения учеников по группам и информирования родителей "
                "и сотрудников."
            ),
            "version": "0.0.1",
        },
    )
