let imp = function imprimir(mensaje){
    console.log(mensaje);
}

function sumar (op1, op2, functionCallback) {
    let res = op1 + op2;
    functionCallback(`Resultado: ${res}`);
}

sumar(5, 3, imp);

//Llamadas asícncromas con uso de función setTimeout(() => {
    
function miFuncionCallback(){
    console.log('Saludo asincrono después de 3 segundos');
}

setTimeout(miFuncionCallback, 3000);

setTimeout( function(){ console.log('Saludo asincrono 2')}, 4000);

setTimeout( () => console.log('saludo Asincrono 3'), 5000);

let reloj = () => {
    let fecha = new Date();
    console.log(`${fecha.getHours()}:${fecha.getMinutes()}:${fecha.getSeconds()}`);
}

setInterval(reloj, 1000); //cada 1 segundo se ejecuta