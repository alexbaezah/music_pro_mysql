$(document).ready(function() {
  // Cargar opciones de región al cargar la página
  

  $('#registro-form').submit(function(event) {
    event.preventDefault();

    // Obtener los datos del formulario
    var rut = $('#inputRut').val();
    var dv = $('#inputDv').val();
    var nombre = $('#inputPrimerNombre').val();
    var apaterno = $('#inputPrimerApellido').val();
    var amaterno = $('#inputSegundoApellido').val();
    var direccion = $('#inputDireccion').val();
    var email = $('#inputCorreo').val();
    var contrasenia = $('#inputPassword4').val();

    // Crear objeto de datos a enviar
    var datos = {
        rut: rut,
        dv: dv,
        nombre: nombre,
        apaterno: apaterno,
        amaterno: amaterno,
        direccion: direccion,
        email: email,
        contrasenia: contrasenia
    };

    // Enviar solicitud AJAX al servidor
    $.ajax({
        type: 'POST',
        url: 'http://127.0.0.1:5000/cliente', // Ajusta la URL según corresponda
        data: JSON.stringify(datos),
        contentType: 'application/json',
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


 
  // Función para cargar las opciones de comuna
// Función para cargar las opciones de comuna

/*
function cargarComunas() {
  console.log('Ejecutando cargarComunas'); // Agregar este console.log
  
  $.ajax({
    url: 'http://127.0.0.1:5000/comunas',
    type: 'GET',
    dataType: 'json',
    success: function(data) {
      // Generar las opciones de comuna
      var opciones = '';
      data.forEach(function(comuna) {
        opciones += '<option value="' + comuna.ID_COM + '">' + comuna.NOM_COM + '</option>';
      });
      $('#inputComuna').html(opciones);
    },
    error: function(error) {
      console.log('Error:', error);
    }
  });
}
*/

