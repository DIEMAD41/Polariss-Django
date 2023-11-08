//Animacion de operaciones
let list=document.querySelectorAll(".list");
function ActivarClase(){
    list.forEach((item) =>
        item.classList.remove("active"));
        this.classList.add('active');
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


//Relleanr tabla de reservaciones
let transporte=[]
let vuelo=[]
let paquete=[]
let clientes=[]

transporte=JSON.parse(localStorage.getItem('infoTrans')) || 0
Datos = [JSON.parse(localStorage.getItem("lug"))]
vuelo=JSON.parse(localStorage.getItem("lug"))[Datos.length]
paquete=JSON.parse(localStorage.getItem('infoTrans')) || 0
clientes=JSON.parse(localStorage.getItem('ClientesData')) || 0


RellenarTabla()
function RellenarTabla(){
    let table=document.querySelector('.TableClientes')

    transporte.forEach(element => {
        table.insertAdjacentHTML('beforeend',
        `
        <tr class="cliente-select">
        <td>${clientes[Math.floor((Math.random() * (clientes.length-1)))].nombre}</td>
        <td>${element.fechai}</td>
        <td>${Math.floor((Math.random() * (10000-500))+500)}</td>
        <td>${"Transporte"}</td>
        <td><span class="status apago">${"En pago"}</span></td>
        </tr>
        `)
    }); 
    vuelo.forEach(element => {
        table.insertAdjacentHTML('beforeend',
        `
        <tr class="cliente-select">
        <td>${clientes[Math.floor((Math.random() * (clientes.length-1)))].nombre}</td>
        <td>${vuelo[0].Salida}</td>
        <td>${Math.floor((Math.random() * (10000-500))+500)}</td>
        <td>${"Vuelo"}</td>
        <td><span class="status pago">${"Pago"}</span></td>
        </tr>
        `)
    }); 
}