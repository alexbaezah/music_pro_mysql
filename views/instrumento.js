$(document).ready(function() {
    // Hacer la solicitud AJAX
    $.ajax({
      url: 'http://127.0.0.1:5000/instrumentos',
      type: 'GET',
      dataType: 'json',
      success: function(data) {
        // Pasar los datos al método de renderizado
        renderInstrumentos(data);
      },
      error: function(error) {
        console.log('Error:', error);
      }
    });
  
    // Función para renderizar los instrumentos
    function renderInstrumentos(instrumentos) {
      const container = $('#instrumentos-container');
  
      // Crear elementos HTML para cada instrumento y agregarlos al contenedor
      instrumentos.forEach(instrumento => {
        const instrumentoElement = $('<div></div>');
        instrumentoElement.text(`${instrumento.nombre}: Precio ${instrumento.precio}, Stock ${instrumento.stock}`);
        container.append(instrumentoElement);
      });
    }
  });
  