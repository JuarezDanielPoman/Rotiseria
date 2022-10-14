var insertodiv = false;
document.querySelector(".opcion").innerHTML='';

function muestraopciondelivery(){
    
    let opcionselecciondada = document.getElementById("tipo_pedido");
    console.log(opcionselecciondada.value);
    let insertartelefonodomicilio = document.querySelector('#pedido');
    var telefonodomicilio=document.createElement('div');

    if(opcionselecciondada.value==1 && insertodiv == false){
    
    
    telefonodomicilio.innerHTML=`<div class="opcion">

    <div class="col-auto mb-2">
    
    <div>
        <label>Fijo</label>
        <input  type="radio" name="telefono-seleccionado" id="fijo" onclick="mostrarInputFijo()">
    
        <label>Celular</label>
        <input type="radio" name="telefono-seleccionado" id="celular" onclick="mostrarInputCelular()">
    </div>
    <input class="form-control mb-2 text-center inactivo" type="tel" required id="estado-fijo" placeholder="Ingrese su telefono fijo">
    <input class="form-control mb-2 text-center inactivo" type="tel" required id="estado-celular" placeholder="Ingrese su telefono celular">
    </div>
            
    <div class="col-auto">
        <label>Localidad</label><br>
        <div class="hvr-icon-pulse form-group has-feedback">
            <i class="hvr-icon fa-solid fa-street-view form-control-feedback"></i>
        <input class="form-control mb-2 text-center" list="lista-localidad" placeholder="Localidad">
            <datalist id="lista-localidad">
                <option value="CAPITAL-S.F.DEL VALLE DE CATAMARCA"></option>
                <option value="BANDA DE VARELA- CAPITAL"></option>
                <option value="LA CALERA "></option>
            </datalist>
        </div>
    </div>
    
    <div class="col-auto">
        <label for="zona-domicilicio">Zona</label><br>
        <div class="hvr-icon-pulse form-group has-feedback">
            <i class="hvr-icon fa-solid fa-street-view form-control-feedback"></i>
        <select class="form-control mb-2 text-center" name="zona-domicilio" id="zona-domicilicio">
            <option value="" selected>Seleccione</option>
            <option value="1">Norte</option>
            <option value="2">Sur</option>
            <option value="3">Este</option>
            <option value="4">Oeste</option>
        </select>
        </div>
    </div>
    <div class="col-auto">
        <label>Barrios</label><br>
        <div class="hvr-icon-pulse form-group has-feedback">
            <i class="hvr-icon fa-solid fa-street-view form-control-feedback"></i>
        <input class="form-control mb-2 text-center" list="lista-barrio" placeholder="Barrio">
            <datalist id="lista-barrio">
                <option value="10 VIVIENDA"></option>
                <option value="11 DE MAYO"></option>
                <option value="16 DE AGOSTO"></option>
            </datalist>
        </div>
    </div>
    <div class="col-auto">
        <label for="calle_y_numero">Calle</label>
        <div class="hvr-icon-pulse form-group has-feedback">
            <i class="fa-solid fa-road form-control-feedback hvr-icon"></i>
            <input type="text" class="form-control mb-2 text-center" required id="calle_y_numero" placeholder="Nombre y número de la calle">
        </div>
        </div>
    `
    insertodiv = true;
    
        insertartelefonodomicilio.appendChild(telefonodomicilio);
    
    }else{if(opcionselecciondada.value!=1 && document.querySelector(".opcion").innerHTML!='' && insertodiv==true){
       // insertartelefonodomicilio.parentNode.removeChild(telefonodomicilio);
       document.querySelectorAll(".opcion").innerHTML='';
        insertodiv=false;
    }
    
    }
    if(opcionselecciondada.value==2){
        document.querySelector(".opcion").innerHTML='';
        document.querySelector(".opcion").remove();
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
