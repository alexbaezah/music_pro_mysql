$(document).ready(function() {
    // Verificar si hay un usuario logueado
    var userEmail = localStorage.getItem('userEmail');
    if (userEmail) {
      // Mostrar el correo electrónico del usuario en el navbar
      $('#username-placeholder').text(userEmail);
    }
  });