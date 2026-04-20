from pelicula import Pelicula;
from catalogo_peliculas import CatalogoPeliculas;

def mostrar_menu():
    print("\nMenú:");
    print("1. Agregar película");
    print("2. Listar películas");
    print("3. Eliminar archivo");
    print("4. Salir");

while True:
    mostrar_menu();
    opcion = input("Elegir opción: ");

    if opcion == "1":
        nombre = input("Ingrese nombre de la película: ");
        pelicula = Pelicula(nombre);
        CatalogoPeliculas.agregar_pelicula(pelicula);

    elif opcion == "2":
        CatalogoPeliculas.listar_peliculas();

    elif opcion == "3":
        CatalogoPeliculas.eliminar();

    elif opcion == "4":
        print("Saliendo...");
        break;

    else:
        print("Opción inválida.");