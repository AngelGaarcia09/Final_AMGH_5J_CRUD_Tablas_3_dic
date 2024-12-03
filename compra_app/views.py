from django.shortcuts import render, redirect
from .models import Compra

# Create your views here.
def inicio_vistaCompras(request):
    lascompras = Compra.objects.all()
    return render(request, "gestionarCompras.html", {"miscompras": lascompras})

def registrarCompra(request):
    id_compra = request.POST["txtcodigo"]
    fecha_compra = request.POST["txtfecha"]
    id_trabajador = request.POST["txttrabajador"]
    id_troca = request.POST["txttroca"]
    ganancias = request.POST["txtganancias"]
    forma_de_pago = request.POST["txtforma"]
    total = request.POST["txttotal"]

    Compra.objects.create(
        id_compra=id_compra,
        fecha_compra=fecha_compra,
        id_trabajador=id_trabajador,
        id_troca=id_troca,
        ganancias=ganancias,
        forma_de_pago=forma_de_pago,
        total=total,
    )

    return redirect("compras")

def seleccionarCompra(request, codigo):
    compra = Compra.objects.get(id_compra=codigo)
    fecha_compra = compra.fecha_compra.strftime('%Y-%m-%d')
    return render(request, "editarCompra.html", {"miscompras": compra, "miscompras": compra, "fecha_compra": fecha_compra})

def editarCompra(request):
    id_compra = request.POST["txtcodigo"]
    fecha_compra = request.POST["txtfecha"]
    id_trabajador = request.POST["txttrabajador"]
    id_troca = request.POST["txttroca"]
    ganancias = request.POST["txtganancias"]
    forma_de_pago = request.POST["txtforma"]
    total = request.POST["txttotal"]

    compra = Compra.objects.get(id_compra=id_compra)
    compra.fecha_compra = fecha_compra
    compra.id_trabajador = id_trabajador
    compra.id_troca = id_troca
    compra.ganancias = ganancias
    compra.forma_de_pago = forma_de_pago
    compra.total = total
    compra.save()

    return redirect("compras")

def borrarCompra(request, codigo):
    compra = Compra.objects.get(id_compra=codigo)
    compra.delete()
    return redirect("compras")
