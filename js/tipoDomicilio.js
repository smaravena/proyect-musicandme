//Obtener referencia a ID radio button div
const casaRadio = document.getElementById('btncasa1');
const departamentoRadio = document.getElementById('btndepo1');
const casaDiv = document.getElementById('casaDiv');
const departamentoDiv = document.getElementById('departamentoDiv');

//Funcion mostrar el div correspondiente segun el radio button seleccionado
function mostrarDiv() {
    if (casaRadio.checked) {
        casaDiv.style.display = 'block';
        departamentoDiv.style.display = 'none';
    } else if (departamentoRadio.checked) {
        casaDiv.style.display = 'none';
        departamentoDiv.style.display = 'block';
    }
}

//Llamar funcion mostrarDiv al principio para que el div inicial visible sea el correcto "()"=ejecutar immediatamente
mostrarDiv();

//event listeners a radio buttons para leer y ejecutar funcion correspondiente
casaRadio.addEventListener('change', mostrarDiv);
departamentoRadio.addEventListener('change', mostrarDiv);
