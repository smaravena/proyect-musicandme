//iframeResizer
iFrameResize({ log: false }, "#masterNavbar");

//iframeResizer
iFrameResize({ log: false }, "#masterFooter");

//TODO validaciones formulario carro
function validaciones() {
  //CODIGO
}

//TODO implementar api
function api_insturmento() {
  //CODIGO
}

//TODO agregar algo extra
function cosa() {
  //CODIGO
  alert("test alert");
}

function validarPass(){
  var password=$('#idpass').val();

  if (password.length==0){
    return false;

  } else {
    return true;
  }
}


function inicosesion(event){
  event.preventDefault();
  var messageError = document.getElementById('diverrorid');
  var valido = true;
  var errores='';

  if (!validarPass()){
    errores = errores + ' algo invalido\n';
    valido=false;

    
  }
  if(!valido){
    messageError.style.display='block';
    messageError.innerHTML=errores;
  }
  //HAY QUE METER CLASE EN DIV DE BLOQUE DE ERROR
  //HAY QUE METER ID EN CAMPO DE FORM
}

const APIController = (function() {
    
  const clientId = 'ee9ebbd6aac24ccca4d935b3845fb6d7';
  const clientSecret = 'eac099fbca0a4b9b870c7105a3cf6d7b';

  // private methods
  const _getToken = async () => {

      const result = await fetch('https://accounts.spotify.com/api/token', {
          method: 'POST',
          headers: {
              'Content-Type' : 'application/x-www-form-urlencoded', 
              'Authorization' : 'Basic ' + btoa(clientId + ':' + clientSecret)
          },
          body: 'grant_type=client_credentials'
      });

      const data = await result.json();
      return data.access_token;
  }
});