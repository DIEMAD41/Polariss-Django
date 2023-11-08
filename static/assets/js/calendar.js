
let fechaS = [
    {dia: 0 ,mes: 0 ,año: 0},{dia: 0, mes: 0, año: 0}
]


let calendario = document.querySelector('.calendario')
const meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
let ban=0, clicks=0
//Determinar si es año bisiesto y determinar el salto de año
vueltaAño = (año) => {
    return (año % 4 === 0 ) || (año % 100 === 0)
}

//Determinar dias de febrero
febDia = (año) => {
    return vueltaAño(año) ? 29 : 28
}

//Generar calendario (el mero mero) Rellena los dias dependiendo de los metodos anteriores
generateCalendar = (mes, año) => {

    let dias_calendario = calendario.querySelector('.calendario-dias')
    let calendario_header_año = calendario.querySelector('#año')
    let dias_mes = [31, febDia(año), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    clicks=0
    dias_calendario.innerHTML = ''

    let fechaActual = new Date()
    if (mes < 0) mes = fechaActual.getMonth()
    if (!año) año = fechaActual.getFullYear()

    let mesActual = `${meses[mes]}`
    mesClick.innerHTML = mesActual
    calendario_header_año.innerHTML = año

    //Consigue el primer dia del mes
    let dias=calendario.querySelector('.calendario-dias')

    let primer_dia = new Date(año, mes, 1)
    let clickAnt=[2]
    for (let i = 0; i <= dias_mes[mes] + primer_dia.getDay() - 1; i++) {
        let dia = document.createElement('div')
        if (i >= primer_dia.getDay()) {
                dia.addEventListener('click', () =>{
                if(!dia.classList.contains('f-select'))
                {
                    if(clicks < 2)
                            {
                            dia.classList.add('f-select')
                            clicks++
                            
                            //Resaltar el rango de dias seleccionados
                          /*   if(clickAnt[0] < clickAnt[1])
                                 clickAnt[0]=parseInt(dia.textContent)
                            
                                 console.log(clickAnt[1]);
                            
                            
                            if(clicks == 2)
                            {
                                for (let index = primer_dia.getDay() - 1 + clickAnt; index < dias.childNodes.length; index++) {
                                    dias.childNodes[index].classList.add('selected')
                                }
                            } */
                            
                            console.log(parseInt(dia.textContent),mes+1,año_actual.value);

                            const fechaSalida= {
                                dia: parseInt(dia.textContent),
                                mes: mes+1,
                                año: año_actual.value
                            }
                            
                            if(clicks==1)
                            fechaS[0]=(fechaSalida)
                            if(clicks==2)
                            fechaS[1]=(fechaSalida)

                            console.log(fechaS);
                            sincronizarLS()
                            }
                }
                else
                {
                    dia.classList.remove('f-select')
                    clicks--
                }
            }) 
            dia.innerHTML = i - primer_dia.getDay() + 1
            //Animacion chingona (pone lineas alrededor del dia en hover)
            dia.innerHTML += `<span></span>
                            <span></span>
                            <span></span>
                            <span></span>`
            if (i - primer_dia.getDay() + 1 === fechaActual.getDate() && año === fechaActual.getFullYear() && mes === fechaActual.getMonth()) {
                dia.classList.add('f-actual')
            }


            let array = JSON.parse(localStorage.getItem('infoTrans'))
            if(array){
            array.forEach(element => {
                    /* console.log(element.fechai.split("/")[0]);
                    console.log(element.fechai.split("/")[1]);
                    console.log(element.fechai.split("/")[2]); */
                let diar= parseInt(element.fechai.split("/")[0])
                let mesr= parseInt(element.fechai.split("/")[1])
                let añor= parseInt(element.fechai.split("/")[2])
                
                if (i - primer_dia.getDay() + 1 === diar && año === añor && mes === mesr-1) {
                    dia.classList.add('f-res')
                }

                let diar2= parseInt(element.fechar.split("/")[0])
                let mesr2= parseInt(element.fechar.split("/")[1])
                let añor2= parseInt(element.fechar.split("/")[2])
                if (i - primer_dia.getDay() + 1 === diar2 && año === añor2 && mes === mesr2-1) {
                    dia.classList.add('f-res')
                }
               
            });
        }




        }
        dias_calendario.appendChild(dia)
    }
}





//Agreagr el mes seleccionado a header
let lista_mes = calendario.querySelector('.lista-meses')

meses.forEach((e, index) => {
    let mes = document.createElement('div')
    mes.innerHTML = `<div data-mes="${index}">${e}</div>`
    mes.querySelector('div').onclick = () => {
        ban++
        lista_mes.classList.remove('show')
        mesActual.value = index
        generateCalendar(index, año_actual.value)
        if(index ==11)
        generateCalendar2(0, año_actual.value + 1)
        else
        generateCalendar2(index + 1, año_actual.value)
       
    }
    lista_mes.appendChild(mes)
})

//Desplegar el menu de seleccion de meses
let mesClick = calendario.querySelector('#mes-picker')

mesClick.onclick = () => {
    lista_mes.classList.add('show')
}


let fechaActual = new Date()
let mesActual = {value: fechaActual.getMonth()}
let año_actual = {value: fechaActual.getFullYear()}

generateCalendar(mesActual.value, año_actual.value)


//Seleccionar el año
document.querySelector('#año-anterior').onclick = () => {
    ban=1
    --año_actual.value
    generateCalendar(mesActual.value, año_actual.value)
    if(mesActual.value === 11)
        {
            generateCalendar2(0, (año_actual.value + 1))
        }
    else
        generateCalendar2(mesActual.value + 1, año_actual.value)

}

document.querySelector('#año-siguiente').onclick = () => {
    ban=1
    ++año_actual.value
    generateCalendar(mesActual.value, año_actual.value)
    if(mesActual.value === 11)
    {
        generateCalendar2(0, (año_actual.value + 1))
    }
else
    generateCalendar2(mesActual.value + 1, año_actual.value)
}


//Modo oscuro/ Modo claro
let dark_mode_toggle = document.querySelector('.dark-mode-switch')

dark_mode_toggle.onclick = () => {
    document.querySelector('body').classList.toggle('light')
    document.querySelector('body').classList.toggle('dark')
}


function sincronizarLS(){
    localStorage.setItem("FechaSeleccionada",JSON.stringify(fechaS));
}


