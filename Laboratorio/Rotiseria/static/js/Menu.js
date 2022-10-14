/*PARA MENU VAR */


var c = document.querySelectorAll('.icono');

    for(i=0;i<c.length;i++){
    if(c[i].style.display != 'none')
    c[i].style.display = 'none';

        }


var d = document.getElementById("celiacos");


d.addEventListener('mouseover',function control1(){
    for(i=0;i<c.length;i++){
            c[1] = document.getElementById("icono").style.display = '';
            c[1] = document.getElementById("icono").style.marginRight = 20;
            document.getElementById("enlaceceliacos").style.paddingLeft = 2 + 'px';
        }
       
    });

    d.addEventListener('mouseleave',function control2(){
        for(i=0;i<c.length;i++){
            c[1] = document.getElementById("icono").style.display = 'none';
            c[1] = document.getElementById("icono").style.marginRight = 20;
            document.getElementById("enlaceceliacos").style.paddingLeft = 2 + 'px';
           
        }
                
    });

    
var v = document.querySelectorAll('.icono');

    
var f = document.getElementById("diabeticos");


f.addEventListener('mouseover',function control1(){
    for(i=0;i<v.length;i++){
            v[0] = document.getElementById("iconod").style.display = '';
            v[0] = document.getElementById("iconod").style.marginRight = 20;
            document.getElementById("enlacediabeticos").style.paddingLeft = 2 + 'px';
        }
       
    });

    f.addEventListener('mouseleave',function control2(){
        for(i=0;i<v.length;i++){
            v[0] = document.getElementById("iconod").style.display = 'none';
            v[0] = document.getElementById("iconod").style.marginRight = 20;
            document.getElementById("enlacediabeticos").style.paddingLeft = 2 + 'px';
           
        }
                
    });

     
var y = document.querySelectorAll('.icono');

 
var g = document.getElementById("vegetarianos");


g.addEventListener('mouseover',function control1(){
    for(i=0;i<y.length;i++){
            y[2] = document.getElementById("iconov").style.display = '';
            y[2] = document.getElementById("iconov").style.marginRight = 20;
            document.getElementById("enlacevegetarianos").style.paddingLeft = 2 + 'px';
        }
       
    });

    g.addEventListener('mouseleave',function control2(){
        for(i=0;i<y.length;i++){
            y[2] = document.getElementById("iconov").style.display = 'none';
            y[2] = document.getElementById("iconov").style.marginRight = 20;
            document.getElementById("enlacevegetarianos").style.paddingLeft = 2 + 'px';
           
        }
                
    });
    //d.removeEventListener('mouseleave',control());   

    var z = document.querySelectorAll('.icono');

        
    var h = document.getElementById("generales");
    
    
    h.addEventListener('mouseover',function control1(){
        for(i=0;i<z.length;i++){
                z[3] = document.getElementById("iconog").style.display = '';
                z[3] = document.getElementById("iconog").style.marginRight = 20;
                document.getElementById("enlacegenerales").style.paddingLeft = 2 + 'px';
            }
           
        });
    
        h.addEventListener('mouseleave',function control2(){
            for(i=0;i<z.length;i++){
                z[3] = document.getElementById("iconog").style.display = 'none';
                z[3] = document.getElementById("iconog").style.marginRight = 20;
                document.getElementById("enlaceg").style.paddingLeft = 2 + 'px';
               
            }
                    
        });

const btnMenu = document.querySelector("#btnMenu");
const menu = document.querySelector("#menu");

btnMenu.addEventListener("click", function() {
    menu.classList.toggle("mostrar")
});


const subMenuBtn = document.querySelectorAll(".submenu-btn");

for(let i=0; i<subMenuBtn.length; i++){ /*Recorre a cual de los submenu le di un click*/

    subMenuBtn[i].addEventListener("click",function() {
       
        if (window.innerWidth < 1024) {
            
            const subMenu = this.nextElementSibling;
            const height = subMenu.scrollHeight;

                if (subMenu.classList.contains("desplegar")) {
                    
                    subMenu.classList.remove("desplegar");
                    subMenu.removeAttribute("style");

                } else {
                    
                    subMenu.classList.add("desplegar");
                    subMenu.style.height = height + "px";
                }

        }

    });

}





/*PARA TIPO DE PLATO */

var c = document.getElementById("tipoplato").style.display = 'none';
var p = document.getElementById("platodiabetico");

p.addEventListener('mouseover',controlestado);

var d = document.getElementById("tipoplato");

d.addEventListener('mouseleave',mousefuera);

function mousefuera(){
    var p = document.getElementById("platodiabetico");
    if(document.getElementById("tipoplato").style.display != 'none'){
        document.getElementById("tipoplato").style.display = 'none';
        }

}


function controlestado(){
    var p = document.getElementById("platodiabetico");
    console.log(p)
    if(document.getElementById("tipoplato").style.display == 'none'){
        document.getElementById("tipoplato").style.display = '';
        }

}







function cambiarListaMenu(){
    
    var item = document.getElementById('platos-diabeticos') 

    //item.setAttribute('href','../templates/ListaDeMenu.html')

    
    //item.setAttribute('href','../templates/ListaDeMenu.html')
    
}
//cambiarTituloMenu("Diabeticoo")


function cambiarTituloMenu() {
   //document.getElementById('titulo-tipo-plato').innerHTML='VJKDVNS'
     var contenedorListaMenu = document.getElementById('lista-menu')
     var template = document.getElementById('contenido-lista-menu').content
     var fragment = document.createDocumentFragment();
     template.getElementById("titulo-tipo-plato").textContent = "titulo"
    
     const clone = template.cloneNode(true)
     fragment.appendChild(clone)
     contenedorListaMenu.appendChild(fragment)

     var item = document.getElementById('platos-diabeticos') 

    item.setAttribute('href','../templates/ListaDeMenu.html')

}

//si se seleccciona delovery debe abilitarse los campos telefono 
//y domicilio

