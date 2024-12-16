from funciones import *
from colorama import init, Fore, Back, Style

init()
init(autoreset=True)


def main():
    crear_tabla()
    while True:
        menu_principal()
        opcion_elegida = input(Fore.GREEN + "Elija una opción: ")
        if opcion_elegida == "1":
            insertar_producto()
        elif opcion_elegida == "2":
            ver_lista_completa_productos()
        elif opcion_elegida == "3":
            eliminar_producto()
        elif opcion_elegida == "4":
            buscar_un_producto()
        elif opcion_elegida == "5":
            actualizar_producto()
        elif opcion_elegida == "6":
            mostrar_stock()
        elif opcion_elegida == "7":
            detectar_stock_bajo()
        elif opcion_elegida == "8":
            print(Fore.RED + "\nHASTA PRONTO !!!")
            break
        else:
            print("Elija una opción válida. Debe ser un número del 1 al 8.")


main()
