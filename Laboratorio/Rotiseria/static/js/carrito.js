//VARIABLES
let contenidoPrincipal = document.querySelector('#lista-productos')
let contenedorTablaCarrito = document.querySelector('#lista-carrito tbody')
let vaciarCarritoBtn = document.getElementById('vaciar-carrito')
let realizarPedidoBtn = document.getElementById('procesar-pedido');
let tablaListaCompra = document.querySelector('#lista-compra tbody');

let procesarcompra = document.getElementById('procesar-compra');

let listacomprarProductos =[];

//funciones
cargarEvento()

function cargarEvento() {
    contenidoPrincipal.addEventListener('click', addProducto);
    contenedorTablaCarrito.addEventListener('click', eliminarProducto);
    vaciarCarritoBtn.addEventListener('click', vaciarCarrito);
    procesarcompra.addEventListener('click', procesarCompra);
}

function addProducto(e) {
    e.preventDefault();
    if(e.target.classList.contains('agregar-carrito')){
        const productoSeleccionado = e.target.parentElement.parentElement;
        leerContenido(productoSeleccionado)
        // console.log(e.target.parentElement.parentElement)
    }

}

function eliminarProducto(e) {

    e.preventDefault();

    if (e.target.parentElement.parentElement.classList.contains('borrar-producto')) {
        const idElementoEliminar = e.target.parentElement.parentElement.getAttribute('data-id');

        e.target.parentElement.parentElement.parentElement.parentElement.remove(); //remuevo de la tabla

        listacomprarProductos = listacomprarProductos.filter(product => product.id != idElementoEliminar) //filtra todos los productos distintos del id seleccionado

        Swal.fire({
            icon: 'error',
            title: 'Producto Eliminado',
            // text: mensaje,
        })
        // console.log('lista filrada',listacomprarProductos)

    }
}

function leerContenido(producto) {
    const infoProducto = {
        //imagen: producto.querySelector('div img').src,
        titulo: producto.querySelector('.titulo_tarjeta').textContent,
        precio: producto.querySelector('.precio_tarjeta-rest span').textContent,
        id: producto.querySelector('.botones-tarjeta a').getAttribute('data-id'),
        cantidad: 1
    }

    const existe = listacomprarProductos.some(producto => producto.id == infoProducto.id);
    if(existe){
        const pro = listacomprarProductos.map(product => {
            if (product.id == infoProducto.id) {
                product.cantidad++;
                let precio_producto = product.precio.slice(1) //le saco el simblo peso
                let precio_cantidad = parseFloat(precio_producto) * parseFloat(product.cantidad);
                product.precio ='$'+precio_cantidad.toFixed(2)
                return product;
            }else{
                return product
            }
        });
        listacomprarProductos = [...pro]
    }else{
        listacomprarProductos = [...listacomprarProductos, infoProducto]
    }
    Swal.fire({
        icon: 'success',
        title: 'Producto agregado',
        showConfirmButton: true,
      })
    insertarCarritoArray() //Segunda forma

}


//SEGUNDA FORMA DE INSERTAR PRODUCTO AL CARRITO
function insertarCarritoArray() {
    limpiarLista();
    let i=1;
    listacomprarProductos.forEach(producto =>{
      
        const {titulo,precio,id,cantidad} = producto;
        const row = document.createElement('tr');
    row.innerHTML = `
        <td>
            ${titulo}
        </td>
        <td>
            ${precio}
        </td>

        <td>
            ${cantidad}
        </td>
        <td>
            <a href="#" class="borrar-producto" data-id="${id}"><i class="fas fa-trash-alt"></i></a>
            <input type="hidden" name="producto${i}" value="${id}" />
        </td>
        
        
        
    `;
        i=i+1;
        contenedorTablaCarrito.appendChild(row)
        // console.log(contenedorTablaCarrito)
    });
}

function limpiarLista() {
    contenedorTablaCarrito.innerHTML="";
}

function vaciarCarrito(e) {
    e.preventDefault()
    while (contenedorTablaCarrito.firstChild) {
        contenedorTablaCarrito.removeChild(contenedorTablaCarrito.firstChild)
        listacomprarProductos =[] //inicializo el array
    }
    // console.log('lista:',listacomprarProductos)
    return false
}

function procesarPedido(e){

    if (listacomprarProductos.length == 0) {
        e.preventDefault()
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'El carrito esta vacio, debes agregar un producto',
        })
    }
}

function procesarCompra(e) {
    console.log('entro a JAVA SCRIPTS PROCESAR COMPRA')
    e.preventDefault()
        Swal.fire({
            "title": "Felicitaciones!!!",
            "text": "Gracias por su compra.",
            "icon": "success"
        })
}

