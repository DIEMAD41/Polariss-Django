let clientes = [];

const profiles=document.querySelector(".blur");
const card=document.querySelector(".card");


function cargarEventListeners() {
    document.addEventListener('DOMContentLoaded', () => {
        clientes = JSON.parse(localStorage.getItem('ClientesData')) || [];
        RellenarClientesR();

        const frameC = document.querySelector('.frameC');
        const listoB = frameC.contentWindow.document.querySelector('.calendario-footer2');

        if (listoB) {
            listoB.addEventListener('click', () => {
                const frameC = document.querySelector('.frameC')
                frameC.classList.remove('showC')
    
                let fechas= []
                fechas=JSON.parse(localStorage.getItem('FechaSeleccionada')) || 0
    
                document.querySelector('#dia').value=parseInt(fechas[0].dia)
                document.querySelector('#mes').value=parseInt(fechas[0].mes)
                document.querySelector('#año').value=parseInt(fechas[0].año)
            });
        }
    });
}

//Animacion de operaciones
let list=document.querySelectorAll(".list");
function ActivarClase(){
    list.forEach((item) =>
        item.classList.remove("active2"));
        this.classList.add('active2');
}
list.forEach((item) =>
item.addEventListener('mouseover', ActivarClase));

let list2=document.querySelectorAll(".list2");
function ActivarClase2(){
    list2.forEach((item) =>
        item.classList.remove("active"));
        this.classList.add('active');
}
list2.forEach((item) =>
item.addEventListener('mouseover', ActivarClase2));

//Operaciones; contraer menu para tablets
const operaciones=document.querySelector(".mini");
const botonops=document.querySelector(".btn-expand");
function ExpanderOperaciones() {
    operaciones.classList.remove("mini");
    botonops.classList.add("hidden");
}
botonops.addEventListener('click', ExpanderOperaciones);

const min=document.querySelector(".minimizar-ops");
function MinimizarOperaciones() {
    operaciones.classList.add("mini");
    botonops.classList.remove("hidden");
}
min.addEventListener('click', MinimizarOperaciones);

//Menu dropdown
function mostrar(anything){
    document.querySelector('.textBox').value=anything;
    botonGo();
}

let menudrop = document.querySelector('.dropdown');
menudrop.addEventListener('click',()=>{
    menudrop.classList.toggle('active');
});


function mostrar2(anything2){
    document.getElementById('tb2').value=anything2;
    botonGo();
}

let menudrop2 = document.getElementById('d2');
menudrop2.addEventListener('click',()=>{
    menudrop2.classList.toggle('active');
});

//Boton GO
function botonGo(){
const go=document.querySelector('.goB');
const opS=document.querySelector('.textBox');
const resS=document.getElementById('tb2');
const iconOP=document.createElement('ion-icon');
const iconOP2=document.createElement('ion-icon');
go.innerHTML='GO';

    switch (opS.value) {
        case 'Agregar':
            iconOP.name="add-circle-outline";
            break;
        case 'Modificar':
            iconOP.name="brush-outline";
            break;
        case 'Eliminar':
            iconOP.name="trash-outline";
            break;
        case 'Buscar':
            iconOP.name="search-circle-outline";
            break;
        case 'Consulta':
            iconOP.name="help-circle-outline";
            break;
    }
    go.appendChild(iconOP);
    console.log(resS.value);
    switch (resS.value) {
        case 'Vuelo':
            iconOP2.name="airplane-outline";
            break;
        case 'Hotel':
            iconOP2.name="bed-outline";
            break;
        case 'Transporte':
            iconOP2.name="bus-outline";
            break;
        case 'Maritimo':
            iconOP2.name="boat-outline";
            break;
        case 'Tour':
            iconOP2.name="camera-outline";
            break;
    }
    go.appendChild(iconOP2);
}

//Abrir la ventana de Registro de clientes
const openRC=document.querySelectorAll('.list')
const ventanaRC=document.querySelector('.RegCli');
openRC[0].addEventListener('click',() => {

    document.querySelector('.btn-modificar').classList.add('hide');
    document.querySelector('.btn-agregar').classList.remove('hide');

    document.querySelector('.titulo-regcli').textContent = "Agregar Cliente"
    document.querySelector('.forma').classList.remove('hide')
    document.querySelector('.img-div').classList.remove('hide')
    document.querySelector('.img-delete').classList.add('hide')
     
    ventanaRC.classList.remove('hiddenRC')
    ventanaRC.classList.remove('eliminar')
    profiles.classList.add('show')
    VaciarInputs()
})

openRC[2].addEventListener('click',() => {
    document.querySelector('.titulo-regcli').textContent = "Eliminar Cliente"
    document.querySelector('.forma').classList.add('hide')
    document.querySelector('.img-div').classList.add('hide')
    document.querySelector('.img-delete').classList.remove('hide')

    ventanaRC.classList.remove('hiddenRC')
    ventanaRC.classList.add('eliminar')
    profiles.classList.add('show')

        var elementos = document.querySelectorAll('.addC');
    elementos.forEach(function(elemento) {
        elemento.classList.add('hide');
    });
        var elementos = document.querySelectorAll('.removeC');
    elementos.forEach(function(elemento) {
        elemento.classList.remove('hide');
    });

    RellenarTabla2()

    let clienteT= document.querySelectorAll('.cliente-select')
    let indice_delete
    clienteT.forEach(element => {
        element.addEventListener('click', () =>{
            var resultado = window.confirm(`Estas seguro que desea eliminar al cliente?`);
                if (resultado === true) {
                    window.alert('Cliente eliminado...');
                    ventanaRC.classList.add('hiddenRC')
                    profiles.classList.remove('show')
                    clientes.find(function(value, index){
                        if(value.id == element.querySelector('td').textContent)
                            {
                                indice_delete=index
                            }
                    });
                    clientes.splice(indice_delete,1)
                    RellenarClientesR()
                    sincronizarLS()
                } else { 
                    window.alert('Operacion cancelada');
                }
        })
    });
})


/*
function RellenarTabla2(){
    let table=document.querySelector('.TableClientes2')
    while (table.firstChild) {
        table.removeChild(table.firstChild);
    }
    clientes.forEach(element => {
        table.insertAdjacentHTML('beforeend',
        `
        <tr class="cliente-select">
        <td>${element.id}</td>
        <td>${element.nombre}</td>
        <td>${element.telefono}</td>
        <td>${element.saldo}</td>
        <td>${element.localidad}</td>
        </tr>
        `)
    }); 
}
*/

openRC[1].addEventListener('click',() => {
    document.querySelector('.btn-agregar').classList.add('hide');
    document.querySelector('.btn-modificar').classList.remove('hide');
    document.querySelector('.titulo-regcli').textContent = "Modificar Cliente"
    document.querySelector('.forma').classList.remove('hide')
    document.querySelector('.img-delete').classList.add('hide')
    document.querySelector('.img-div').classList.add('hide')

    var elementos = document.querySelectorAll('.removeC');
    elementos.forEach(function(elemento) {
        elemento.classList.add('hide');
    });
        var elementos = document.querySelectorAll('.addC');
    elementos.forEach(function(elemento) {
        elemento.classList.remove('hide');
    });



    document.querySelector('.btn-reg').textContent="MODIFICAR"
     
    ventanaRC.classList.remove('hiddenRC')
    ventanaRC.classList.add('eliminar')
    profiles.classList.add('show')

    RellenarTabla2()

    let clienteT= document.querySelectorAll('.cliente-select')
    clienteT.forEach(element => {
        element.addEventListener('click', () =>{
            let input=document.querySelectorAll('.dataC')
            input[4].value = element.querySelectorAll('td')[1].textContent
            input[5].value = element.querySelectorAll('td')[2].textContent


            clientes.find(function(value, index){
                if(value.id == element.querySelectorAll('td')[0].textContent)
                    {
                        input[6].value=value.correo
                    }
            });

            input[7].value = element.querySelectorAll('td')[4].textContent

        })
    });
})

function  VaciarInputs() {
    let input=document.querySelectorAll('.dataC')
    input[4].value = ""
    input[5].value = ""
    input[6].value = ""
    input[7].value = ""
}


//Cerrar ventana RC
profiles.addEventListener('click',() =>{
    ventanaRC.classList.add('hiddenRC')
    profiles.classList.remove('show')
    card.classList.add('hide')
    frameC.classList.remove('showC')
})

const cerrarRC=document.querySelector(".closeRC");
cerrarRC.addEventListener('click',() =>{
    ventanaRC.classList.add('hiddenRC')
    profiles.classList.remove('show')
})

//JS de la ventana registrar cliente
const inputRC=document.querySelectorAll('.Campo')
let enterRC
document.addEventListener('click', function(event) {
    enterRC=0
    for (let index = 0; index < inputRC.length; index++) {
        var isClickInside = inputRC[index].contains(event.target);
        if (isClickInside) {
            enterRC=1
            DesactivarTodosRC()
            if( inputRC[index].querySelector('.iconoRG'))
            {
                inputRC[index].querySelector('.iconoRG').classList.add('click')
            }
        }

    }
    if(enterRC != 1)
    DesactivarTodosRC()
});

function DesactivarTodosRC()
{
    inputRC.forEach(element => {
            if(element.querySelector('.iconoRG'))
            element.querySelector('.iconoRG').classList.remove('click')
            
    });
    
}

//Obtener la ruta local de la imagen seleccionada
function init() {
    var archivoSeleccionado = document.getElementById('imagensubida');
    archivoSeleccionado.addEventListener('change', mostrarImagen);
  }
  
  function mostrarImagen(event) {
    var archivoSeleccionado = document.getElementById('imagensubida');
    var archivoIMG = event.target.files[0];
    var reader = new FileReader();
    reader.onload = function(event) {
      var img = document.getElementById('img1');
      img.src= event.target.result;
    }
    reader.readAsDataURL(archivoIMG);
  }
  
  window.addEventListener('load', init);


//Calcular Edad en años
function CalcularEdad()
{
    var d1 = document.getElementById('dia').value;  
    var m1 = document.getElementById('mes').value;  
    var a1 = document.getElementById('año').value;  
    var fecha = new Date();  
    var d2 = fecha.getDate();  
    var m2 = 1 + fecha.getMonth();  
    var a2 = fecha.getFullYear();  
    var mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];  
    if(d1 > d2){  
    d2 = d2 + mes[m2 - 1];  
    m2 = m2 - 1;  
    }  
    if(m1 > m2){  
    m2 = m2 + 12;  
    a2 = a2 - 1;  
    }  
    var d = d2 - d1;  
    var m = m2 - m1;  
    var a = a2 - a1;
    return a  
}

//Agregar cliente a un vector
function AgregarCliente()
{
    let input=document.querySelectorAll('.dataC')
    /* {id: 1251301, nombre: 'Marisol Sanchez', telefono: 3531216500, 
    saldo: 12600, correo: "madenz@gmail.com", edad: 24, localidad: "Sahuayo", imagen: "Imgs/us1.jpg"} */
    
   /*  console.log(clientes[clientes.length-1].id + 1);//id
    console.log(input[4].value);//nombre
    console.log(input[5].value);//tel
    console.log(Math.floor((Math.random() * (10000-500))+500));//saldo
    console.log(input[6].value);//correo  
    console.log(CalcularEdad());//edad
    console.log(input[7].value);//localidad
    console.log(input[0].value);//img
     */
    const Cliente = {
        id: clientes[clientes.length-1].id + 1, 
        nombre: input[4].value, 
        telefono: input[5].value, 
        saldo: Math.floor((Math.random() * (10000-500))+500), 
        correo: input[6].value, 
        edad: CalcularEdad(), 
        localidad: input[7].value, 
        /* imagen: input[0].value */ //No se puede agregar de manera local
        imagen: "Imgs/art.jpg"
    }
    
    ventanaRC.classList.add('hiddenRC')
    profiles.classList.remove('show')
    clientes.push(Cliente);
    sincronizarLS()
    RellenarClientesR()
    /* console.log(input[1].value);//dia
    console.log(input[2].value);//mes
    console.log(input[3].value);//año */
}

   
/*     let nombreCompleto="Diego Manzo"
    console.log(nombreCompleto.split(" ")[0]);
    console.log(nombreCompleto.split(" ")[1]);
 */

//AGREGAR LOS CLIENTES A LA SECCION DE CLIENTES RECIENTES
    
    function RellenarClientesR()
    {
    const clientesPadre=document.querySelector('.clientesRC')
    while (clientesPadre.firstChild) {
        clientesPadre.removeChild(clientesPadre.firstChild);
      }
    for (let index = clientes.length-1; index >=0 ; index--) {
        let nombreCompleto=clientes[index].nombre
        clientesPadre.insertAdjacentHTML('beforeend',
        `
            <tr>
            <td width="60px" class="tdi"><div class="imbBx"><img src="${clientes[index].imagen}"></td>
            <td><h4>${nombreCompleto.split(" ")[0]}</h4>ID: &nbsp<span class="idT">${clientes[index].id}</span>
                <div class="iconos">
                    <ion-icon class="profile" name="person-circle-outline"></ion-icon>
                    <ion-icon name="mail-outline"></ion-icon>
                    <ion-icon name="call-outline"></ion-icon>
                </div>
            </td>  
        </tr>
        `
        )}
        AbrirPerfilCliente()
    }


    document.addEventListener('DOMContentLoaded', function () {
        //Abir el perfil de cliente al dar click
        var elementosTR = document.querySelectorAll('.trC');
        console.log(elementosTR);

        // Agrega un evento de clic a cada elemento td
        elementosTR.forEach(function (elemento) {
            elemento.addEventListener('click', function () {
                // Llama a la función AbrirPerfilCliente() cuando se hace clic
                AbrirPerfilCliente();
            });
        });
    });

function AbrirPerfilCliente()
{
     console.log('Perfil del cliente abierto');
    //Abrir el perfil de los clientes
    const profile=document.querySelectorAll(".ops-right tr");
    console.log(profile);
    const card=document.querySelector(".card");
    const profiles=document.querySelector(".blur");
    profile.forEach(element => {
        element.addEventListener('click',() =>{

            clientes.find(function(value, index) {
                if (value.id == parseInt(element.querySelector('.idT').textContent))
                {
                    console.log("Este es un mensaje informativo.");
                    while (card.firstChild) {
                        card.removeChild(card.firstChild);
                    }
                    card.insertAdjacentHTML('afterbegin',
                    `   <ion-icon name="close-outline" class="close"></ion-icon>
                        <ion-icon name="ellipsis-horizontal-outline" class="submenu"></ion-icon>
                        <div class="submenuC">
                        <div class="opccionesC">
                            <div><ion-icon name="add-circle-outline"></ion-icon>Modificar</div>
                            <div><ion-icon name="trash-outline"></ion-icon>Eliminar</div>
                        </div>
                        </div>
                        <div class="card-header">
                            <img src="${value.imagen}" alt="Profile Image" class="profile-img">
                        </div>
                        <div class="card-body">
                            <p class="name">${value.nombre}</p>
                            <a href="#" class="mail">${value.correo}</a>
                            <div class="content">   
                                <p class="texto"><span class="municipio">${value.localidad}</span></p>
                                <p class="texto"><span class="edad">${value.edad} años</span></p>
                                <p class="texto"><span class="telefono">${value.telefono}</span></p>
                            </div>
                            <p class="saldo">Saldo: ${value.saldo}</p>
                        </div>
                
                        <div class="social-links">
                            <a href="#" class="fas fa-phone-alt social-icon"></a>
                            <a href="#" class="far fa-envelope social-icon"></a>
                            <a href="#" class="fab fa-google social-icon"></a>
                            <a href="#" class="fab fa-facebook social-icon"></a>
                        </div>

                        <div class="card-footer">
                            <p class="count">CLIENTE POLARISS</p>
                        </div>`
                    )
                }
            });
            card.classList.remove('hide');
            profiles.classList.add('show');

            const minimizarP=document.querySelector(".close");
            minimizarP.addEventListener('click',() =>{
            card.classList.add('hide');
            profiles.classList.remove('show');
            })

            //Abrir el submenu de la tarjeta de clientes
            const submenuC=document.querySelector(".submenuCard");
            const submenuC2=document.querySelector(".submenuC");
            submenuC.addEventListener('click',() =>{
                submenuC2.classList.toggle('showC');
            })

        })
    });
}
  
/*
//Mostrar todo en clientes frecuentes
let ban=0
const btnVerTodo=document.querySelector('.btn')
btnVerTodo.addEventListener('click', () =>
{
    btnVerTodo.addEventListener('click',MostrarTodo())
    if(ban==0)
        btnVerTodo.innerHTML="Ver todos"
    else
        btnVerTodo.innerHTML="Ocultar"
})
*/

function MostrarTodo()
{
    const clientesMT=document.querySelector('.TableClientes')
    if(ban==0)
    {
        for (let index = clientes.length-1; index >=0 ; index--) {
            clientesMT.insertAdjacentHTML('beforeend',
            `
                <tr class="toggleC">
                <td>${clientes[index].nombre}</td>
                <td>${clientes[index].telefono}</td>
                <td>${clientes[index].saldo}</td>
                <td>${clientes[index].localidad}</td>
                <td>${clientes[index].edad}</td>
                </tr>
            `)
        }
        ban=1
    }
    else
    {
        for (let index = clientes.length-1; index >=0 ; index--) {
            if(document.querySelector('.toggleC'))
            clientesMT.removeChild(document.querySelector('.toggleC'));
        }
        ban=0
    }
}

//Guardar un cliente en el local storage
function sincronizarLS(){
    localStorage.setItem("ClientesData",JSON.stringify(clientes));
}

//Abrir el calendario
const fechaEdad=document.querySelectorAll(".fecha")
const frameC = document.querySelector('.frameC')
fechaEdad.forEach(element => {
    element.addEventListener('click', () =>{
        frameC.classList.add('showC')
        profiles.classList.add('show')
    })
});

