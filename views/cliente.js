$(document).ready(function() {
    // Cargar opciones de región al cargar la página
    cargarRegiones();
    
    $('#registro-form').submit(function(event) {
      event.preventDefault();
  
      // Obtener los datos del formulario
      var rut = $('#inputRut').val();
      var dv = $('#inputDv').val();
      var nombre = $('#inputPrimerNombre').val();
      var apaterno = $('#inputPrimerApellido').val();
      var amaterno = $('#inputSegundoApellido').val();
      var direccion = $('#inputDireccion').val();
      var region = $('#inputRegion').val();
      var comuna = $('#inputComuna').val();
      var telefono = $('#inputTelefono').val();
  
      // Crear objeto de datos a enviar
      var datos = {
        rut: rut,
        dv: dv,
        nombre: nombre,
        apaterno: apaterno,
        amaterno: amaterno,
        direccion: direccion,
        region: region,
        comuna: comuna,
        telefono: telefono
      };
  
      // Enviar solicitud AJAX al servidor
      $.ajax({
        type: 'POST',
        url: 'http://127.0.0.1:5000/registro',
        data: datos,
        dataType: 'json',
        success: function(response) {
          // Mostrar mensaje de éxito
          alert(response.message);
        },
        error: function(error) {
          console.log('Error:', error);
        }
      });
    });
  });
  
  // Función para cargar las opciones de región
  function cargarRegiones() {
    $.ajax({
      url: 'http://127.0.0.1:5000/regiones',
      type: 'GET',
      dataType: 'json',
      success: function(data) {
        // Generar las opciones de región
        var opciones = '';
        data.forEach(function(region) {
          opciones += '<option value="' + region.ID_REGION + '">' + region.NOMBRE_REG + '</option>';
        });
        $('#inputRegion').html(opciones);
      },
      error: function(error) {
        console.log('Error:', error);
      }
    });
  }
  