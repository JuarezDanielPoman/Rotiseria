
var listaProducto = [
    {
        //imagen: producto.querySelector('div img').src,
        titulo: "milanesa",
        precio: 800,
        id: 1,
        cantidad: 2
   }
]


let tablaPedidosCliente = document.querySelector('#lista-compra .body')

document.addEventListener('DOMContentLoaded',cargarTabla);

function cargarTabla(){

    let precio_cantidad;
    let cantidad_prod; 
    let precio_prod 

    listaProducto.forEach(producto =>{
        
            precio_prod = Number(producto.precio)
            cantidad_prod = Number(producto.cantidad)
            precio_cantidad = precio_prod * cantidad_prod

            const row = document.createElement('tr');
            row.innerHTML = `
            <td>
                ${producto.titulo}
            </td>
            <td>
                ${producto.precio}
            </td>
            <td>
                <input type="number" class="form-control cantidad" min="1" value=${producto.cantidad}>
            </td>
            <td>
                ${precio_cantidad.toFixed(2)}
            </td>
            <td>
                <a href="#" class="borrar-producto" data-id="${producto.id}"><i class="fas fa-trash-alt"></i></a>
            </td>
    
        `;
        tablaPedidosCliente.appendChild(row)
        console.log('lista 2',tablaListaCompra)
    });

}
