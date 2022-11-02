def importe_total(request):
    total = 0
    if request.user.is_authenticated:
        if "carrito" in request.session:
            for key, value in request.session["carrito"].items():
                total += int(value["subtotal"]) * 1.21
    return {"importe_total": round(total,2)}

def sub_total(request):
    subtotal=0
    if request.user.is_authenticated:
        if "carrito" in request.session:
            for key, value in request.session["carrito"].items():
                subtotal += int(value["subtotal"])
    return {"sub_total":round(subtotal,2)}
