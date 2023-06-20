function actualizarTiempo(){
    var fecha = new Date();

    var horas = agregarCero(fecha.getHours());
    var minutos = agregarCero(fecha.getMinutes());
    var segundos = agregarCero(fecha.getSeconds());

    var tiempo = horas + ":" + minutos + ":" + segundos;
    document.getElementById('tiempo').textContent = tiempo;
     
}

function agregarCero(numero) {
    if (numero < 10) {
        return "0" + numero;
    }

    return numero;
}


setInterval(actualizarTiempo, 1000)