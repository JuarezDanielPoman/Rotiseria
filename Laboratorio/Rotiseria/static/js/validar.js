var insertodiv = false;

document.getElementById("opcion").style.display = 'NONE';

function muestraopciondelivery(){

    let opcionselecciondada = document.getElementById("tipo_pedido");
    console.log(opcionselecciondada.value);
    document.querySelector('#pedido');

    if(opcionselecciondada.value==1 && insertodiv == false){
    
    
    document.getElementById("opcion").style.display = '';
    
    insertodiv = true;
    
        // insertartelefonodomicilio.appendChild(telefonodomicilio);
    
    }else{if(opcionselecciondada.value!=1 && document.getElementById("opcion").style.display == 'none' && insertodiv==true){
       // insertartelefonodomicilio.parentNode.removeChild(telefonodomicilio);
       document.getElementById("opcion").style.display = '';
        insertodiv=false;
    }
    
    }
    if(opcionselecciondada.value==2){
        document.getElementById("opcion").style.display = 'NONE';
        console.log("Llego aca ")
    }
    //insertartelefonodomicilio.removeChild(telefonodomicilio);

console.log(insertodiv)
//console.log(telefono)
//console.log(insertartelefono)
}
//muestraopciondelivery();

var fechaActual = new Date();

const fechaInput = document.getElementById("fechanacimiento");

console.log(fechaActual.toISOString().split('T')[0]);
console.log(fechaInput);

fechaInput.value = fechaActual.toISOString().split('T')[0];


const formulario = document.getElementById('formulario-pedido')
formulario.addEventListener('submit', (e)=>{
    verificarFecha(e)
})

function verificarFecha(e) {
    const fechaIngresada = document.getElementById('fechanacimiento')

    if(fechaIngresada.value >= fechaActual.toISOString().split('T')[0]){
        console.log(fechaIngresada.value);
        console.log(fechaActual.toISOString().split('T')[0]);

        e.preventDefault()
        alert('LA FECHA INGRESADA ES INCORRECTA')
    }
}



function mostrarInputFijo(){
    const inputFijo = document.getElementById('estado-fijo')
    const inputCelular = document.getElementById('estado-celular')
    const resultadoInputFijo = inputFijo.classList.contains('inactivo')
    
    if(!resultadoInputFijo){
        inputFijo.classList.add('inactivo')
        inputCelular.classList.remove('inactivo')
    }

    inputFijo.classList.toggle('inactivo')
    inputCelular.classList.add('inactivo')
}

function mostrarInputCelular() {
    const inputCelular = document.getElementById('estado-celular')
    const inputFijo = document.getElementById('estado-fijo')   
    const resultaldoInputCelular = inputCelular.classList.contains('inactivo')

    if(!resultaldoInputCelular){
        inputCelular.classList.add('inactivo')
        inputFijo.classList.remove('inactivo')
    }
    
    inputCelular.classList.toggle('inactivo')
    inputFijo.classList.toggle('inactivo')
}

var total=0;
let celdasPrecio=document.querySelectorAll( ' td + td + td + td'); 
console.log(celdasPrecio.length);
for ( let i = 0 ;i<document.getElementById("RegistroPedido").rows.length-1;++i) {
total += parseInt(celdasPrecio[i].firstChild.data) ;
}

let nuevaFila = document.createElement ('tr') ;
let celdaTotal = document.createElement('td') ;
let textoceldatotal=document.createTextNode('Total: ');
celdaTotal.appendChild(textoceldatotal);
nuevaFila.appendChild(celdaTotal);

let celdavalortotal=document.createElement('td');
let textoceldavalortotal=document.createTextNode(total);
celdavalortotal.appendChild(textoceldavalortotal);
nuevaFila.appendChild(celdavalortotal);

document.getElementById("RegistroPedido").appendChild(nuevaFila);
