function irArriba(){
    window.addEventListener('scroll',()=>{
        var scroll = document.documentElement.scrollTop;
        // console.log(scroll)
        var botonAriba = document.getElementById('boton-arriba')

        if(scroll>300){
            botonAriba.style.right=20 + "px";
        }else{
            botonAriba.style.right=-100 + "px";
        }
    })
}
//Se ejecuta la funcion
irArriba(); 
