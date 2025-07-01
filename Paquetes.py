import subprocess
import sys
import os

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def install_package(package, upgrade=False):
    try:
        command = [sys.executable, "-m", "pip", "install"]
        if upgrade:
            command.append("--upgrade")
        command.append(package)
        
        action = "Actualizando" if upgrade else "Instalando"
        print(f"\n{action} {package}...")
        subprocess.check_call(command)
        print(f"✓ {package} {'actualizado' if upgrade else 'instalado'} correctamente")
        return True
    except subprocess.CalledProcessError:
        print(f"✗ Error al {'actualizar' if upgrade else 'instalar'} {package}")
        return False

def instalar_predeterminados(upgrade=False):
    paquetes = ["pymino", "colorama", "pyfiglet", "tqdm", "requests", "diskcache", "dotenv","uuid","base64"]
    
    action = "ACTUALIZANDO" if upgrade else "INSTALANDO"
    print(f"\n{action} PAQUETES PREDETERMINADOS")
    print("=" * 40)
    
    exitosos = 0
    for paquete in paquetes:
        if install_package(paquete, upgrade):
            exitosos += 1
    
    print(f"\n{exitosos}/{len(paquetes)} paquetes {'actualizados' if upgrade else 'instalados'} correctamente")

def instalacion_personalizada():
    print("\nINSTALACION PERSONALIZADA")
    print("=" * 40)
    print("Escribe 'salir' para volver al menu principal")
    
    while True:
        package = input("\nNombre del paquete: ").strip()
        if package.lower() in ["salir", "exit", "quit"]:
            break
        if not package:
            print("Error. Intenta de nuevo.")
            continue
        install_package(package)

def mostrar_menu():
    """Muestra el menu principal"""
    print("\n" + "=" * 40)
    print("    INSTALADOR DE DEPENDENCIAS")
    print("=" * 40)
    print("1. Instalar predeterminados")
    print("2. Instalacion personalizada")
    print("3. Actualizar pips (1)")
    print("4. Salir")
    print("=" * 40)

def main():
    while True:
        clear_console()
        mostrar_menu()
        
        try:
            opcion = input("\nOpcion: ").strip()
            
            if opcion == "1":
                instalar_predeterminados()
                input("\nPresiona Enter para continuar...")
                
            elif opcion == "2":
                instalacion_personalizada()
                input("\nPresiona Enter para continuar...")
                
            elif opcion == "3":
                instalar_predeterminados(upgrade=True)
                input("\nPresiona Enter para continuar...")
                
            elif opcion == "4":
                print("\nFinalizando el instalador. ¡Hasta luego!")
                break
                
            else:
                print("Opcion invalida. Selecciona 1, 2, 3 o 4")
                input("\nPresiona Enter para continuar...")
                
        except KeyboardInterrupt:
            print("\n\nFinalizando el instalador. ¡Hasta luego!")
            break

if __name__ == "__main__":
    main()