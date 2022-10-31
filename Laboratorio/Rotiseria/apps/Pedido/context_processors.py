def importe_total(request):
    total = 0
    if request.user.is_authenticated:
        if "carrito" in request.session:
            for key, value in request.session["carrito"].items():
                total += float(value["precio"])
    return {"importe_total": total}