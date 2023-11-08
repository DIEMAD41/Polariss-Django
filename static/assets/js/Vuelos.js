const grid = document.querySelector('.grid')
const ViajeR = document.querySelector('.t1')
const ViajeS = document.querySelector('.t2')
const O = document.querySelector('.O')
const D = document.querySelector('.D')
const Fs = document.querySelector('.Fs')
const Fl = document.querySelector('.Fl')
const P = document.querySelector('.P')
const opciones = document.querySelector('.Opciones')
const op = document.querySelector('.Op')
const Button = document.querySelector('.B')

const vacio1 = document.querySelector('.vacio1')
const vacio2 = document.querySelector('.vacio2')

const contA = document.querySelector('.Ad');
const contN = document.querySelector('.Niñ');
const contE = document.querySelector('.Es');
const contM = document.querySelector('.Ma');


var ban = false;
var c;

"Madang Airport","Madang"

const lugares =[
    {Id:1,Air:'Goroka Airport',Name:'Goroka',Icon:'<ion-icon name="earth-outline"></ion-icon>'},
    {Id:2,Air:'Madang Airport',Name:'Madang',Icon:'<ion-icon name="earth-outline"></ion-icon>'},
    {Id:3,Air:'Mount Hagen Kagamuga Airport',Name:'Mount Hagen',Icon:'<ion-icon name="earth-outline"></ion-icon>'},
    {Id:4,Air:'Nadzab Airport',Name:'Nadzab',Icon:'<ion-icon name="earth-outline"></ion-icon>'},
    {Id:5,Air:'Wewak International Airport',Name:'Wewak',Icon:'<ion-icon name="earth-outline"></ion-icon>'},
]

var Datos = [] ;

var Reuzar = 
[
    {Type:'',Origen:'',Destino:'',Salida:'',Regreso:'',Pasajeros:''}
]

BanO = true; 
BanD = true;

Button.addEventListener("click",()=>{
    this.da();
    this.sincronizarLocalStorage();
    console.log(localStorage.getItem("lug"));
    
    //this.CallLocal();
    //console.log(localStorage.getItem("lug").indexOf(","))
});

function da()
{
    if(ViajeR.style.background=="white")
        Reuzar[0].Type = ViajeS.innerHTML
    else
        Reuzar[0].Type = ViajeR.innerHTML
    Reuzar[0].Origen = O.children.item(1).innerHTML
    Reuzar[0].Destino = D.children.item(1).innerHTML
    Reuzar[0].Salida = Fs.children.item(1).innerHTML
    Reuzar[0].Regreso = Fl.children.item(1).innerHTML
    Reuzar[0].Pasajeros = P.children.item(1).innerHTML
    Datos.push(Reuzar);
}

function sincronizarLocalStorage()
{
   localStorage.setItem("lug",JSON.stringify(Datos)); 
}


document.addEventListener('DOMContentLoaded', () => {
    Datos = [JSON.parse(localStorage.getItem("lug"))]
    if(JSON.parse(localStorage.getItem("lug"))[Datos.length] != null)
    Temp = (JSON.parse(localStorage.getItem("lug"))[Datos.length])
    console.log(Temp[0].Origen)
    console.log(Temp[0].Destino)
    console.log(Temp[0].Salida)
    console.log(Temp[0].Regreso)
    console.log(Temp[0].Pasajeros)

    const profiles=document.querySelector(".blur");
    const listoB=document.querySelector('.frameC').contentWindow.document.querySelector('.calendario-footer2')
        listoB.addEventListener('click', () =>{

            const frameC = document.querySelector('.frameC')
            frameC.classList.remove('showC')
            profiles.classList.remove('show')

            let fechas= []
            fechas=JSON.parse(localStorage.getItem('FechaSeleccionada')) || 0


            Fs.children.item(1).textContent=(`${fechas[0].dia}/${fechas[0].mes}/${fechas[0].año}`)
            Fl.children.item(1).textContent=(`${fechas[1].dia}/${fechas[1].mes}/${fechas[1].año}`)
        })
    
        
    if(Datos!=null)
    {
        O.children.item(0).textContent = "";
        O.children.item(1).style.display = "block";
        D.children.item(0).textContent = "";
        D.children.item(1).style.display = "block";
        if(Temp[0].Type == "Viaje Redondo")
        {
            ViajeR.style.background="#F94144";
            ViajeS.style.background="white";
        }
        else
        {
            ViajeS.style.background="#F94144";
            ViajeR.style.background="white";
        }
        O.children.item(1).textContent = Temp[0].Origen
        D.children.item(1).textContent = Temp[0].Destino
        Fs.children.item(1).textContent = Temp[0].Salida
        Fl.children.item(1).textContent = Temp[0].Regreso
        P.children.item(1).innerHTML = Temp[0].Pasajeros

        console.log(O.children.item(1).textContent.length +"/"+D.children.item(1).textContent.length)
        if( O.children.item(1).textContent.length>16 || D.children.item(1).textContent.length>16)
        {
            grid.classList.add("grid2")
            grid.classList.remove("grid")
        }
        else
        {
            grid.classList.add("grid")
            grid.classList.remove("grid2") 
        }  
    }

    let inerant ='';
    inerant += vacio1.innerHTML;
    for(ind=0;ind<lugares.length;ind++)
    {
        inerant += "<div class='Op'>"+ lugares[ind].Icon+"<a>"+lugares[ind].Air+"</a> </div>"
    }
    vacio1.innerHTML = inerant;
    vacio2.innerHTML = inerant;

});


ViajeS.addEventListener("click",()=>{
    ViajeS.style.background="#F94144";
    ViajeR.style.background="white";
});

ViajeR.addEventListener("click",()=>{
    ViajeR.style.background="#F94144";
    ViajeS.style.background="white";
});


O.addEventListener("click",()=>{
    if(D.children.item(2).classList.contains("Opciones"))
        D.classList.toggle('active');
    if(P.children.item(3).classList.contains("OpcionesP"))
        P.classList.toggle('active');
    D.children.item(2).classList.remove("Opciones");
    P.children.item(3).classList.remove("OpcionesP");
    if(O.children.item(2).classList.contains("Opciones"))
    {
        O.children.item(2).classList.remove("Opciones");
    }
    else
    {
        O.children.item(2).classList.add("Opciones");
        document.querySelectorAll('.Opciones > .Op').forEach((op) => {
            op.addEventListener('click', (e) => {
                O.children.item(0).textContent = "";
                O.children.item(1).style.display = "block";
                if(op.textContent.length<16)
                {
                    if(op.textContent.substring(0,7).sub(" "))
                    {   
                        if(op.textContent.substring(0,7).sub(" "))
                        {
                            if(BanD)
                            {
                                O.children.item(1).textContent = op.textContent
                                grid.classList.add("grid")
                                grid.classList.remove("grid2")
                            }else
                            {
                                O.children.item(1).textContent = op.textContent
                            }
                            BanO=true;
                        }
                        else
                        {
                            O.children.item(1).textContent = op.textContent
                            grid.classList.add("grid2")
                            grid.classList.remove("grid")
                            BanO=false;
                        }
                    }
                    else
                    {
                        O.children.item(1).textContent = op.textContent
                        grid.classList.add("grid2")
                        grid.classList.remove("grid")
                        BanO=false;
                    }    
                }
                else
                {
                    O.children.item(1).textContent = op.textContent
                    grid.classList.add("grid2")
                    grid.classList.remove("grid")
                    BanO=false;
                }     
            });
        });
    }
    O.classList.toggle('active');

});

D.addEventListener("click",()=>{
    if(O.children.item(2).classList.contains("Opciones"))
        O.classList.toggle('active');
    if(P.children.item(3).classList.contains("OpcionesP"))
        P.classList.toggle('active');
    P.children.item(3).classList.remove("OpcionesP");
    O.children.item(2).classList.remove("Opciones");
    if(D.children.item(2).classList.contains("Opciones"))
    {
        D.children.item(2).classList.remove("Opciones");
    }
    else
    {
        D.children.item(2).classList.add("Opciones");
        document.querySelectorAll('.Opciones > .Op').forEach((op) => {
            op.addEventListener('click', (e) => {
                D.children.item(0).textContent = "";
                D.children.item(1).style.display = "block";
                if(op.textContent.length<16)
                {
                    if(op.textContent.substring(0,7).sub(" "))
                    {   
                        if(op.textContent.substring(0,7).sub(" "))
                        {
                            if(BanO)
                            {
                                D.children.item(1).textContent = op.textContent
                                grid.classList.add("grid")
                                grid.classList.remove("grid2")
                            }
                            else
                            {
                                D.children.item(1).textContent = op.textContent
                            }
                            BanD=true;
                        }
                        else
                        {
                            D.children.item(1).textContent = op.textContent
                            grid.classList.add("grid2")
                            grid.classList.remove("grid")
                            BanD=false;
                        }
                    }
                    else
                    {
                        D.children.item(1).textContent = op.textContent
                        grid.classList.add("grid2")
                        grid.classList.remove("grid")
                        BanD=false;
                    }    
                }
                else
                {
                    D.children.item(1).textContent = op.textContent
                    grid.classList.add("grid2")
                    grid.classList.remove("grid")
                    BanD=false;
                }     
            });
        });
    }
    D.classList.toggle('active');
});


P.addEventListener("click",()=>{
    if(D.children.item(2).classList.contains("Opciones"))
        D.classList.toggle('active');
    if(O.children.item(2).classList.contains("Opciones"))
        O.classList.toggle('active');
    D.children.item(2).classList.remove("Opciones");
    O.children.item(2).classList.remove("Opciones");
    if(P.children.item(3).classList.contains("OpcionesP"))
    {
        P.children.item(3).classList.remove("OpcionesP");
    }
    else
    {
        P.children.item(3).classList.add("OpcionesP");
    }
    P.classList.toggle('active');
});

function cont()
{
    c="";
    if(parseInt(contA.children.item(1).children.item(1).innerHTML)>0)
        c += parseInt(contA.children.item(1).children.item(1).innerHTML)+" Adultos <br>";
    if(parseInt(contN.children.item(1).children.item(1).innerHTML)>0)
        c += parseInt(contN.children.item(1).children.item(1).innerHTML)+" Niños <br>";
    if(parseInt(contE.children.item(1).children.item(1).innerHTML)>0)
        c += parseInt(contE.children.item(1).children.item(1).innerHTML)+" Estudiantes <br>";
    if(parseInt(contM.children.item(1).children.item(1).innerHTML)>0)
        c += parseInt(contM.children.item(1).children.item(1).innerHTML)+" Mascotas <br>";
        P.children.item(1).innerHTML =c;
}


contA.children.item(1).children.item(0).addEventListener("click",()=>{
    if(parseInt(contA.children.item(1).children.item(1).innerHTML)>0)
    {
        contA.children.item(1).children.item(1).innerHTML = parseInt(contA.children.item(1).children.item(1).innerHTML)-1; 
        this.cont();   
    }
});
contA.children.item(1).children.item(2).addEventListener("click",()=>{
    if(parseInt(contA.children.item(1).children.item(1).innerHTML)>=0)
    {
        contA.children.item(1).children.item(1).innerHTML = parseInt(contA.children.item(1).children.item(1).innerHTML)+1;
        this.cont();
    }
});

contN.children.item(1).children.item(0).addEventListener("click",()=>{
    if(parseInt(contN.children.item(1).children.item(1).innerHTML)>0)
    {
        contN.children.item(1).children.item(1).innerHTML = parseInt(contN.children.item(1).children.item(1).innerHTML)-1;
        this.cont();  
    }
});
contN.children.item(1).children.item(2).addEventListener("click",()=>{
    if(parseInt(contN.children.item(1).children.item(1).innerHTML)>=0)
    {
        contN.children.item(1).children.item(1).innerHTML = parseInt(contN.children.item(1).children.item(1).innerHTML)+1;
        this.cont();
    }
});

contE.children.item(1).children.item(0).addEventListener("click",()=>{
    if(parseInt(contE.children.item(1).children.item(1).innerHTML)>0)
    {
        contE.children.item(1).children.item(1).innerHTML = parseInt(contE.children.item(1).children.item(1).innerHTML)-1;
        this.cont();  
    }
});

contE.children.item(1).children.item(2).addEventListener("click",()=>{
    if(parseInt(contE.children.item(1).children.item(1).innerHTML)>=0)
    {
        contE.children.item(1).children.item(1).innerHTML = parseInt(contE.children.item(1).children.item(1).innerHTML)+1; 
        this.cont();
    }   
});

contM.children.item(1).children.item(0).addEventListener("click",()=>{
    if(parseInt(contM.children.item(1).children.item(1).innerHTML)>0)
    {
        contM.children.item(1).children.item(1).innerHTML = parseInt(contM.children.item(1).children.item(1).innerHTML)-1;  
        this.cont(); 
    }   
});
contM.children.item(1).children.item(2).addEventListener("click",()=>{
    if(parseInt(contM.children.item(1).children.item(1).innerHTML)>=0)
    {
        contM.children.item(1).children.item(1).innerHTML = parseInt(contM.children.item(1).children.item(1).innerHTML)+1;  
        this.cont();
    }
});



/*document.querySelector('.')
console.log(O.children.item(2).children.item(0));*/


//Agregar el calendario
const fechaS = document.querySelector('.Fs')
const fechaR = document.querySelector('.Fl')
const frameC = document.querySelector('.frameC')
const blur = document.querySelector('.blur')
fechaS.addEventListener('click', () => {
    frameC.classList.add('showC')
    blur.classList.add('show')
})
fechaR.addEventListener('click', () => {
    frameC.classList.add('showC')
    blur.classList.add('show')
})
blur.addEventListener('click', () => {
    frameC.classList.remove('showC')
    blur.classList.remove('show')
})

