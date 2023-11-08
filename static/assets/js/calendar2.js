
let calendario2 = document.querySelector('.calendario2')
const meses2 = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

//Determinar si es año bisiesto y determinar el salto de año
vueltaAño = (año) => {
    return (año % 4 === 0 ) || (año % 100 === 0)
}

//Determinar dias de febrero
febDia = (año) => {
    return vueltaAño(año) ? 29 : 28
}

//Generar calendario2 (el mero mero) Rellena los dias dependiendo de los metodos anteriores
generateCalendar2 = (mes, año) => {

    let dias_calendario2 = calendario2.querySelector('.calendario-dias')
    let calendario2_header_año = calendario2.querySelector('#año')

    let dias_mes = [31, febDia(año), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    dias_calendario2.innerHTML = ''

    let fechaActual2 = new Date()
    if(ban==0)
    {
        if(mes===11)
        {
            mes=0
            año=fechaActual.getFullYear() +1
        }
        else{
            mes=fechaActual.getMonth() + 1
            año=fechaActual.getFullYear()
        }   
    }

    let mesActual2 = `${meses2[mes]}`
    mesClick2.innerHTML = mesActual2
    calendario2_header_año.innerHTML = año

    //Consigue el primer dia del mes
    let primer_dia = new Date(año, mes, 1)
    let clickAnt=0
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
                            clickAnt=parseInt(dia.textContent)

                            console.log(parseInt(dia.textContent),mes+1,año_actual.value);

                            const fechaSalida= {
                                dia: parseInt(dia.textContent),
                                mes: mes+1,
                                año: año
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
            if (i - primer_dia.getDay() + 1 === fechaActual2.getDate() && año === fechaActual2.getFullYear() && mes === fechaActual2.getMonth()) {
                dia.classList.add('f-actual')
            }

            let array = JSON.parse(localStorage.getItem('infoTrans'))
            if (array) {
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
        dias_calendario2.appendChild(dia)
    }
}

//Seleccionar un dia



//Agreagr el mes seleccionado a header
let lista_mes2 = calendario2.querySelector('.lista-meses')

meses2.forEach((e, index) => {
    let mes = document.createElement('div')
    mes.innerHTML = `<div data-mes="${index}">${e}</div>`
    mes.querySelector('div').onclick = () => {
        lista_mes2.classList.remove('show')
        mesActual2.value = index
        generateCalendar2(index, año_actual2.value)
    }
    lista_mes2.appendChild(mes)
})

//Desplegar el menu de seleccion de meses2
let mesClick2 = calendario2.querySelector('#mes-picker')

mesClick2.onclick = () => {
    lista_mes2.classList.add('show')
}


let fechaActual2 = new Date()
let mesActual2 = {value: fechaActual2.getMonth()}
let año_actual2 = {value: fechaActual2.getFullYear()}

generateCalendar2(mesActual2.value, año_actual2.value)

function sincronizarLS(){
    localStorage.setItem("FechaSeleccionada",JSON.stringify(fechaS));
}

