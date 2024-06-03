const SpotifyAPIController = (function () {
    // Cliente ID y Cliente Secret ID
    const clientId = "cliente_id";
    const clientSecret = "cliente_secret_id_app";
  
    // Métodos privados
    const obtenerToken = async () => {
      const result = await fetch('https://accounts.spotify.com/api/token', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
          'Authorization': 'Basic ' + btoa(clientId + ':' + clientSecret)
        },
        body: 'grant_type=client_credentials'
      });
  
      const data = await result.json();
      return data.access_token;
    }
  
    const obtenerPista = async (token, endPointPista) => {
      const result = await fetch(`${endPointPista}`, {
        method: 'GET',
        headers: { 'Authorization': 'Bearer ' + token }
      });
      console.log('TOKENSITO: '+token);
      const data = await result.json();
      return data;
    }
  
    return {
      obtenerToken() {
        return obtenerToken();
      },
      obtenerPista(token, endPointPista) {
        return obtenerPista(token, endPointPista);
      }
    }
  })();
  
  // Módulo de Interfaz de Usuario
  const SpotifyUIController = (function () {
    // Objeto para mantener referencias a los selectores HTML
    const elementosDOM = {
      divDetalleCancion: '#song-detail',
      hfToken: '#hidden_token'
    }
  
    // Métodos públicos
    return {
      // Método para crear detalle de la canción
      crearDetalleCancion(img, titulo, artista) {
        const detalleDiv = document.querySelector(elementosDOM.divDetalleCancion);
        detalleDiv.innerHTML = '';
  
        const html = `
          <div class="row col-sm-12 px-0">
              <img src="${img}" alt="">        
          </div>
          <div class="row col-sm-12 px-0">
              <label for="titulo" class="form-label col-sm-12">${titulo}:</label>
          </div>
          <div class="row col-sm-12 px-0">
              <label for="artista" class="form-label col-sm-12">Por ${artista}:</label>
          </div> 
        `;
  
        detalleDiv.insertAdjacentHTML('beforeend', html)
      },
  
      // Método para almacenar el token
      almacenarToken(valor) {
        document.querySelector(elementosDOM.hfToken).value = valor;
      },
  
      // Método para obtener el token almacenado
      obtenerTokenAlmacenado() {
        return {
          token: document.querySelector(elementosDOM.hfToken).value
        }
      }
    }
  })();
  
  const SpotifyAppController = (function (UIController, APIController) {
    const cargarCancionEspecifica = async () => {
      const token = await APIController.obtenerToken();
      UIController.almacenarToken(token);
  
      const cancion = await APIController.obtenerPista(token, 'https://api.spotify.com/v1/tracks/3S2R0EVwBSAVMd5UMgKTL0');
      UIController.crearDetalleCancion(cancion.album.images[0].url, cancion.name, cancion.artists[0].name);
    }
  
    return {
      init() {
        console.log('SPOTIFY.JS');
        cargarCancionEspecifica();
      }
    }
  
  })(SpotifyUIController, SpotifyAPIController);
  
  // Llamar a un método para cargar la canción específica al cargar la página
  SpotifyAppController.init();
  