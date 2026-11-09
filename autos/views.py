from django.shortcuts import redirect, render

from .forms import AutoForm
from .models import Auto


def lista_autos(request):
    autos = Auto.objects.order_by("marca", "modelo")
    return render(request, "autos/auto_list.html", {"autos": autos})


def agregar_auto(request):
    if request.method == "POST":
        form = AutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("autos:lista")
    else:
        form = AutoForm()

    return render(request, "autos/auto_form.html", {"form": form})
