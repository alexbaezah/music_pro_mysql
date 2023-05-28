

$(document).ready(function() {
  // Cargar opciones de región al cargar la página
  
  // ajax para registro
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
            // luego redirige al index.html
            window.location.href = '../index.html';
        },
        error: function(error) {
            console.log('Error:', error);
        }
    });
  });






  $('#login-button').click(function() {
    // Obtener los datos del formulario de inicio de sesión
    var email = $('#inputCorreo').val();
    var contraseniaLogin = $('#inputPassword4').val();

    // Crear objeto de datos a enviar
    var datos = {
      email: email,
      contrasenia: contraseniaLogin
    };

    // Enviar solicitud AJAX al servidor
    $.ajax({
      type: 'POST',
      url: 'http://127.0.0.1:5000/cliente/login', // Ajusta la URL según corresponda
      data: JSON.stringify(datos),
      contentType: 'application/json',
      success: function(response) {
        // Mostrar mensaje de éxito
        localStorage.setItem('userEmail', email);
        alert(response.message);
        // Redirigir al usuario al index.html
        window.location.href = '../index.html';
        
      },
      error: function(error) {
        console.log('Error:', error);
      }
    });
  });
});


