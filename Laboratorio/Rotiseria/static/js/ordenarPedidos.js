
// var p = document.getElementById("estado");
// p.addEventListener('click',controlestado);
// controlestado();

// function controlestado(){
// if(p.value=='D' || p.value=='C'){
//     $("#ventanaModalPedido").modal();
//     console.log(p.value);
//     console.log($("#ventanaModalPedido").modal('show'));
// }
// console.log(p.value);
// }



function ordenarTocandoColumna(n) {
    var tabla, fila, i,x,y,cambiar ,debeCambiar, dir, contador =0; 

    tabla = document.getElementById('tabla-pedidos-pendientes')
    
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
                if(x != null && y!= null ){
                
                if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
                    debeCambiar = true;
                    break; 
                }}
            }else{
                if (dir == "desc") {
                    if(x != null && y!= null ){
                    if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
                        debeCambiar = true;
                        break; 
                    }
                }}
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

var tablaPedidos = document.getElementById('tabla-pedidos-pendientes'); 
obtenerValoresHora(tablaPedidos,4)

function obtenerValoresHora(tabla, numeroColumna) {
    let listaDeHoras =[]; 

    for (let i = 1, columna; i < tabla.rows.length; i++) {
        columna = tabla.rows[i].cells[numeroColumna];
        if(columna != null ){

        listaDeHoras[i]=columna.innerHTML; 
        }
    }
    console.log('Lista de horas: ',listaDeHoras)

    compararHoraEntrega(listaDeHoras)
}

function compararHoraEntrega(listaDeHoras) {
    var fechaActual = new Date();
    var horaActual = Number(fechaActual.getHours()); 
    var horaEnMinutosLocal = Number(fechaActual.getHours()) * 60 ; 
    var minutosLocal = Number(fechaActual.getMinutes());
    var horaEnMinutosActual = horaEnMinutosLocal + minutosLocal; 
    var tabla = document.getElementById('tabla-pedidos-pendientes');

    for (let i = 1; i <= listaDeHoras.length; i++) {
        var horaTabla = Number(listaDeHoras[i].substring(0,2));
        var minutosTabla = Number(listaDeHoras[i].substring(3,5));
        var horaEnMinutosTabla = (horaTabla * 60) + minutosTabla
        
        if ((horaEnMinutosTabla - horaEnMinutosActual)===60 || (horaTabla - horaActual)===1) {
            //console.log('FALTA UNA HORA')
            tabla.rows[i].style.backgroundColor="#f77335"; //naranja
        }else{
            if (horaEnMinutosTabla > horaEnMinutosActual) {
                 tabla.rows[i].style.backgroundColor="#92F56C"; //verde
            } else {
                tabla.rows[i].style.backgroundColor="#E13C2D"; //Rojo
            }
        }
    }
}


    
/*
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <title>Bootstrap Example</title>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
      <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
      <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
    </head>
    <body>
    
    <script>
    function myFunction() {
    var option_value = document.getElementById("numbers").value;
    if (option_value == "3") {
      //  alert("Hai !");
       $("#myModal").modal();
     }
    }
       
    
    </script>
    <select id = "numbers" onchange = "myFunction()">
     <option value = "1">1</option>
     <option value = "2">2</option>
     <option value = "3">Click me !</option>
    </select>
    <div class="container">
      <h2>Basic Modal Example</h2>
      <!-- Trigger the modal with a button -->
    
    
      <!-- Modal -->
      <div class="modal fade" id="myModal" role="dialog">
        <div class="modal-dialog">
        
          <!-- Modal content-->
          <div class="modal-content">
            <div class="modal-header">
              <button type="button" class="close" data-dismiss="modal">&times;</button>
              <h4 class="modal-title">Modal Header</h4>
            </div>
            <div class="modal-body">
              <p>Some text in the modal.</p>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
            </div>
          </div>
          
        </div>
      </div>
      
    </div>
    
    </body>
    </html>*/