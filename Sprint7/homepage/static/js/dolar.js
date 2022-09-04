
//Variables de los elemntos de dolar Oficial
const infoOficial = document.getElementById("infoOficial");
const variacionOficial = document.getElementById("variacionOficial");
//Variables de los elemntos de dolar blue
const infoBlue = document.getElementById("infoBlue");
const variacionBlue = document.getElementById("variacionBlue");
//Variables de los elemntos de dolar Liqui
const infoLiqui = document.getElementById("infoLiqui");
const variacionLiqui = document.getElementById("variacionLiqui");
//Variables de los elemntos de dolar Bolsa
const infoBolsa = document.getElementById("infoBolsa");
const variacionBolsa = document.getElementById("variacionBolsa");
//Variables de los elemntos de dolar Turista
const infoTurista = document.getElementById("infoTurista");
const variacionTurista = document.getElementById("variacionTurista");
//Variables de los elemntos de dolar Promedio
const infoPromedio = document.getElementById("infoPromedio");
const variacionPromedio = document.getElementById("variacionPromedio");
//Variables convertir
const cant = document.getElementById("cant");
const result = document.getElementById("resultado")

function getDolar() {
        const url = "https://www.dolarsi.com/api/api.php?type=valoresprincipales"
        fetch(url)
            .then(function (response) {
                return response.json();})
            .then( function (data) {
                const oficial = [data[0].casa.venta, data[0].casa.compra, data[0].casa.variacion];
                const blue = [data[1].casa.venta, data[1].casa.compra, data[1].casa.variacion];
                const contadoConLiqui = [data[3].casa.venta, data[3].casa.compra, data[3].casa.variacion];
                const bolsa = [data[4].casa.venta, data[4].casa.compra, data[4].casa.variacion];
                const turista = [data[6].casa.venta, data[6].casa.compra, data[6].casa.variacion];
                const promedio = [data[7].casa.venta, data[7].casa.compra];

                infoOficial.innerHTML = crearInfo(oficial[0],oficial[1]);
                variacionOficial.innerHTML = oficial[2] + "%";

                infoBlue.innerHTML = crearInfo(blue[0],blue[1]);
                variacionBlue.innerHTML = blue[2] + "%";

                infoLiqui.innerHTML = crearInfo(contadoConLiqui[0],contadoConLiqui[1]);
                variacionLiqui.innerHTML = contadoConLiqui[2] + "%";

                infoBolsa.innerHTML = crearInfo(bolsa[0],bolsa[1]);
                variacionBolsa.innerHTML = bolsa[2] + "%";

                infoTurista.innerHTML = crearInfo(turista[0],turista[1]);
                variacionTurista.innerHTML = turista[2] + "%";

                infoPromedio.innerHTML = crearInfo(promedio[0],promedio[1]);
                variacionPromedio.innerHTML = "NO DISPONIBLE";
            })
}

function detectDolar(){
        const opciones = [inputOficial, inputBlue, inputLiqui, inputBolsa, inputTurista];
        const returns = [infoOficial.innerHTML.split("$")[1], infoBlue.innerHTML.split("$")[1], infoLiqui.innerHTML.split("$")[1], infoBolsa.innerHTML.split("$")[1], infoTurista.innerHTML.split("$")[1], infoPromedio.innerHTML.split("$")[1]];
        let selected = document.querySelector('input[type=radio][name=flexRadioDefault]:checked');
        return returns[opciones.indexOf(selected)];
}


function calcular(){
    const cantidad = cant.value;
    const dolar = detectDolar();
    const resultado = parseFloat(cantidad) * parseFloat(dolar);
    result.innerHTML = "El resultado es: $"+resultado+" ARS";
    result.classList.remove("d-none")
}

function crearInfo(venta,compra){
    if (venta == "No Cotiza"){
        return "COMPRA: $" + compra;
    }
    else if (compra == "No Cotiza"){
        return "VENTA: $" + venta;
    }
    else{
        return "COMPRA: $" + compra + " VENTA: $" + venta;
    }
}

getDolar();
setInterval(getDolar, 30000);


