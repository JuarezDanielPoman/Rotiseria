var fechaActual = new Date();

const fechaInput = document.getElementById("fechaPedido");

fechaInput.value = fechaActual.toISOString().split('T')[0];


const formulario = document.getElementById('formulario-pedido')
formulario.addEventListener('submit', (e)=>{
    verificarFecha(e)
})

function verificarFecha(e) {
    const fechaIngresada = document.getElementById('fechaPedido')

    if(fechaIngresada.value < fechaActual.toISOString().split('T')[0]){
        e.preventDefault()
        alert('LA FECHA INGRESADA ES INCORRECTA')
    }
}

/*Verificar que el horario para la entrega del pedido, 
sea un horario en el que el local se
encuentra trabajando.*/

var horadesde = document.getElementById("hora-desde");

var horahasta = document.getElementById("hora-hasta");

var time1 = new Date();

horadesde.value = time1.setHours(10,0,0);
horadesde.value = time1.toTimeString().slice(0,5);

var time2 = new Date();

horahasta.value = time2.setHours(12,0,0);
horahasta.value = time2.toTimeString().slice(0,5);


function controlhora(e){

    horadesde.addEventListener('click',controlhora);
    horahasta.addEventListener('click',controlhora);
    
if(horadesde.value<time1.toTimeString().slice(0,5) || horadesde.value>time2.toTimeString().slice(0,5)){
    e.preventDefault()
    alert("La hora seleccionada no es valida")

    horadesde.value = time1.toTimeString().slice(0,5);
    horahasta.value = time2.toTimeString().slice(0,5);
}


}

const formulario1 = document.getElementById('formulario-pedido')
formulario1.addEventListener('submit', (e)=>{
    controlhora(e)
})


/*
En el caso de que se cambie el estado del pedido a “devuelto” o “cancelado”,
requerir al
usuario que ingrese un comentario.*/

var p = document.getElementById("estado");



var c = document.getElementById("divcomentario").style.display = 'none'

p.addEventListener('click',controlestado);

function controlestado(){
        var p = document.getElementById("estado");

        if(p.value=='D' || p.value=='C'){
            var c = document.getElementById("divcomentario").style.display = '';
        }
        else{
            var c = document.getElementById("divcomentario").style.display = 'none'
        }
        }

        const formulario2 = document.getElementById('formulario-pedido')
formulario1.addEventListener('submit', (e)=>{
    controlestado(e)
})
