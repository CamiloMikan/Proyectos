const apiKey = '4ad9d75578944c2f98e05256232006';

const locacionInput = document.getElementById('locacion');
const btnBuscar = document.getElementById('btn-buscar');
const temperaturaLabel = document.getElementById('temperatura');
const descripcionLabel = document.getElementById('descripcion');
const iconoClima = document.getElementById('icono-clima');

btnBuscar.addEventListener('click', buscarDatosClima);

function buscarDatosClima() {
  const locacion = locacionInput.value;
  // Realiza la solicitud del clima a la API
  fetch(`https://api.weatherapi.com/v1/current.json?key=${apiKey}&lang=es&q=${encodeURIComponent(locacion)}`)
    .then(response => response.json())
    .then(data => {
      const { location, current } = data;
      const temperatura = current.temp_c;
      temperaturaLabel.textContent = `${temperatura} °C`;
      descripcionLabel.textContent = current.condition.text;

      const codigoIcono = current.condition.icon;
      const urlIcono = `https:${codigoIcono}`;
      iconoClima.setAttribute('src', urlIcono);
      iconoClima.setAttribute('alt', current.condition.text);
    })
    .catch(error => {
      console.log('Error al obtener los datos del clima:', error);
    });
}
