$(document).ready(function() {
    // Hacer la solicitud AJAX
    $.ajax({
      url: 'http://127.0.0.1:5000/accesorios',
      type: 'GET',
      dataType: 'json',
      success: function(data) {
        // Pasar los datos al método de renderizado
        renderAccesorios(data);
      },
      error: function(error) {
        console.log('Error:', error);
      }
    });
  
    // Función para renderizar los accesorios
    function renderAccesorios(accesorios) {
      const accesoriosContainer = $('#accesorios-container');
  
      accesorios.forEach(acce => {
        const card = $('<div class="card" style="width: 18rem;"></div>');
        const image = $(`<img src="${acce.foto}" class="card-img-top" alt="Accesorio">`);
        const cardBody = $('<div class="card-body"></div>');
        const title = $(`<h5 class="card-title">${acce.nombre}</h5>`);
        const description = $(`<p class="card-text">${acce.descripcion}</p>`);
        const button = $(`<a href="./accesorio.html?id=${acce.id}" class="btn btn-primary">Ver características</a>`);
  
        cardBody.append(title, description, button);
        card.append(image, cardBody);
        accesoriosContainer.append(card);
      });
    }
  });
  
  $(document).ready(function() {
    // Obtener el ID del accesorio de la URL
    const urlParams = new URLSearchParams(window.location.search);
    const accesorioId = urlParams.get('id');
  
    // Hacer la solicitud AJAX para obtener el accesorio específico
    $.ajax({
      url: 'http://127.0.0.1:5000/accesorios/' + accesorioId,
      type: 'GET',
      dataType: 'json',
      success: function(data) {
        // Pasar los datos al método de renderizado de accesorio único
        renderAccesorio(data);
      },
      error: function(error) {
        console.log('Error:', error);
      }
    });
  
    // Función para renderizar un accesorio único
    function renderAccesorio(accesorio) {
      // Renderizar el accesorio en el div proporcionado
      $('#accesorio-imagen').attr('src', accesorio.foto);
      $('#accesorio-titulo').text(accesorio.nombre);
      $('#accesorio-descripcion').text(accesorio.descripcion);
      $('#accesorio-precio').text('$' + accesorio.precio);
      $('#accesorio-stock').text( accesorio.stock);
  
    }
  });
  