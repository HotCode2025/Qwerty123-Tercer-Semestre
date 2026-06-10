const seccion = document.querySelector('section'); // ← apunta a section
const cantidadSquares =7;//La cantidad de cajas
const cantidadCircles =9;//La cantidad de circulos



for (let i = 0; i < cantidadSquares; i++) {
    const square = document.createElement('div');//Creamos directamente el div desde aca
    square.classList.add('square');//Clase para el style
    square.style.setProperty('--i', i);//Variable

    //Tamaño de las cajas
    const size = Math.floor(Math.random() * 80 + 40);
    square.style.width  = size + 'px';
    square.style.height = size + 'px';

    //Posicionamiento de las cajas
    square.style.top  = Math.floor(Math.random() * window.innerHeight) + 'px';
    square.style.left = Math.floor(Math.random() * window.innerWidth)  + 'px';

    seccion.appendChild(square);//Lo agregamos a la pag.
}

for (let j = 0; j < cantidadCircles; j++) {
    const circle = document.createElement('div');
    circle.classList.add('circle');
    circle.style.setProperty('--j', j);

    const size = Math.floor(Math.random() * 80 + 40);
    circle.style.width  = size + 'px';
    circle.style.height = size + 'px';

    circle.style.top  = Math.floor(Math.random() * window.innerHeight) + 'px';
    circle.style.left = Math.floor(Math.random() * window.innerWidth)  + 'px';

    seccion.appendChild(circle);
}