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
      const button = $(`<a href="./instrumento.html?id=${instrumento.id}" class="btn btn-primary">Ver características</a>`);

      cardBody.append(title, description, button);
      card.append(image, cardBody);
      instrumentosContainer.append(card);
    });
  }
});


$(document).ready(function() {
  // Obtener el ID del instrumento de la URL
  const urlParams = new URLSearchParams(window.location.search);
  const instrumentoId = urlParams.get('id');

  // Hacer la solicitud AJAX para obtener el instrumento específico
  $.ajax({
    url: 'http://127.0.0.1:5000/instrumentos/' + instrumentoId,
    type: 'GET',
    dataType: 'json',
    success: function(data) {
      // Pasar los datos al método de renderizado de instrumento único
      renderInstrumento(data);
    },
    error: function(error) {
      console.log('Error:', error);
    }
  });

  // Función para renderizar un instrumento único
  function renderInstrumento(instrumento) {
    // Renderizar el instrumento en el div proporcionado
    $('#instrumento-imagen').attr('src', instrumento.foto);
    $('#instrumento-titulo').text(instrumento.nombre);
    $('#instrumento-descripcion').text(instrumento.descripcion);
    $('#instrumento-precio').text('$' + instrumento.precio);
    $('#instrumento-stock').text('Stock: ' + instrumento.stock);

    // Resto del código para renderizar los demás elementos según tus necesidades
    // ...
  }
});
