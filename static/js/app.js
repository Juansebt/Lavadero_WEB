function verContrasena(boton){
  var tipo = document.getElementById("txtPassword");
  if(tipo.type == "password"){
      tipo.type = "text";
      boton.innerText="Ocultar contraseña";
  }else{
      tipo.type = "password";
      boton.innerText="Mostrar contraseña";
  }
}