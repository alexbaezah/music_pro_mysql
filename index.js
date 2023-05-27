$(document).ready(function() {
    // Hacer la solicitud AJAX para obtener los instrumentos
    $.ajax({
      url: 'http://127.0.0.1:5000/instrumentos',
      type: 'GET',
      dataType: 'json',
      success: function(data) {
        // Pasar los datos de los instrumentos al método de renderizado
        renderInstrumentos(data);
      },
      error: function(error) {
        console.log('Error:', error);
      }
    });
  
    // Hacer la solicitud AJAX para obtener los accesorios
    $.ajax({
      url: 'http://127.0.0.1:5000/accesorios',
      type: 'GET',
      dataType: 'json',
      success: function(data) {
        // Pasar los datos de los accesorios al método de renderizado
        renderAccesorios(data);
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
        const button = $('<a href="#" class="btn btn-primary">Revisar</a>');
  
        cardBody.append(title, description, button);
        card.append(image, cardBody);
        instrumentosContainer.append(card);
      });
    }
  
    // Función para renderizar los accesorios
    function renderAccesorios(accesorios) {
      const accesoriosContainer = $('#accesorios-container');
  
      accesorios.forEach(accesorio => {
        const card = $('<div class="card" style="width: 18rem;"></div>');
        const image = $(`<img src="${accesorio.foto}" class="card-img-top" alt="Accesorio">`);
        const cardBody = $('<div class="card-body"></div>');
        const title = $(`<h5 class="card-title">${accesorio.nombre}</h5>`);
        const description = $(`<p class="card-text">${accesorio.descripcion}</p>`);
        const button = $('<a href="#" class="btn btn-primary">Revisar</a>');
  
        cardBody.append(title, description, button);
        card.append(image, cardBody);
        accesoriosContainer.append(card);
      });
    }
  });
  