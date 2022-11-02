
var total=0;
let celdasPrecio=document.querySelectorAll( ' td + td + td + td + td + td'); 
console.log(celdasPrecio.length);
for ( let i = 0 ;i<document.getElementById("ventasdiarias").rows.length-1;++i) {
total += parseInt(celdasPrecio[i].firstChild.data );
console.log(total);

}


function crearfila(total){

let nuevaFila = document.createElement ('tr') ;
let celdaTotal = document.createElement('td') ;
let textoceldatotal=document.createTextNode('Total: ');
celdaTotal.appendChild(textoceldatotal);
nuevaFila.appendChild(celdaTotal);

let celdavalortotal=document.createElement('td');
let textoceldavalortotal=document.createTextNode(total);
celdavalortotal.appendChild(textoceldavalortotal);
nuevaFila.appendChild(celdavalortotal);
return nuevaFila;
}

//Estadistica cantidad de pedido entregada por cadete
;

document.getElementById("ventasdiarias").appendChild(crearfila(total));


var total1=0;
let celdasPrecio1=document.querySelectorAll ( ' td + td + td + td' ) ; 
for ( let i = 0 ;i<celdasPrecio1.length;++i) {
    if(i>=document.getElementById("entregadasporcadete").rows.length-1){
    total1 += parseInt(celdasPrecio1[i].firstChild.data) ;}
}

document.getElementById("entregadasporcadete").appendChild(crearfila(total1));


graficaLinea();
function graficaLinea() {
    let grafica = document.getElementById('myChart')
    var xValues = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"];
    var yValues = [55, 49, 44, 24, 15];
    var barColors = [
      "#b91d47",
      "#00aba9",
      "#2b5797",
      "#e8c3b9",
      "#1e7145"
    ];
    
    new Chart(grafica, {
      type: "pie",
      data: {
        labels: xValues,
        datasets: [{
          backgroundColor: barColors,
          data: yValues
        }]
      },
      options: {
        title: {
          display: true,
          text: "Ventas semanales de la rotiseria"
        }
      }
    });
}