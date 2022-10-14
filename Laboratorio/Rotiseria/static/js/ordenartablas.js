
function ordenarTocandoColumna(n) {
    var tabla, fila, i,x,y,cambiar ,debeCambiar, dir, contador =0; 

    tabla = document.getElementById('tabla')
    
    cambiar = true
    dir = "asc"

    while (cambiar) {

        cambiar= false
        fila = tabla.rows;
        
        for ( i = 1; i < (fila.length - 1); i++) {
            debeCambiar = false; 
            x =  fila[i].getElementsByTagName("TD")[n]
            y =  fila[i+1].getElementsByTagName("TD")[n]

            if (dir == "asc") {
                if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
                    debeCambiar = true;
                    break; 
                }
            }else{
                if (dir == "desc") {
                    if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
                        debeCambiar = true;
                        break; 
                    }
                }
            }

        }

        if (debeCambiar) {
            fila[i].parentNode.insertBefore(fila[i + 1], fila[i]);
            cambiar = true;
            contador++;
        }else{
            
            if (contador == 0 && dir == "asc") {
                dir = "desc";
                cambiar = true;
            }
            
        }
    }
}