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
    const instrumentosContainer = $('#instrumentos-container');

    instrumentos.forEach(instrumento => {
      const card = $('<div class="card" style="width: 18rem;"></div>');
      const image = $(`<img src="${instrumento.foto}" class="card-img-top" alt="Instrumento">`);
      const cardBody = $('<div class="card-body"></div>');
      const title = $(`<h5 class="card-title">${instrumento.nombre}</h5>`);
      const description = $(`<p class="card-text">${instrumento.descripcion}</p>`);
      const button = $('<a href="#" class="btn btn-primary">Go somewhere</a>');

      cardBody.append(title, description, button);
      card.append(image, cardBody);
      instrumentosContainer.append(card);
    });
  }
});
