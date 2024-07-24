import os
import webbrowser
from colorama import init, Fore, Style

init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_intro():
    intro = """
    ░█████╗░░██████╗██╗███╗░░██╗████████╗  ███╗░░██╗░█████╗░██╗░░░██╗██╗░██████╗░░█████╗░████████╗░█████╗░██████╗░
    ██╔══██╗██╔════╝██║████╗░██║╚══██╔══╝  ████╗░██║██╔══██╗██║░░░██║██║██╔════╝░██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
    ██║░░██║╚█████╗░██║██╔██╗██║░░░██║░░░  ██╔██╗██║███████║╚██╗░██╔╝██║██║░░██╗░███████║░░░██║░░░██║░░██║██████╔╝
    ██║░░██║░╚═══██╗██║██║╚████║░░░██║░░░  ██║╚████║██╔══██║░╚████╔╝░██║██║░░╚██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗
    ╚█████╔╝██████╔╝██║██║░╚███║░░░██║░░░  ██║░╚███║██║░░██║░░╚██╔╝░░██║╚██████╔╝██║░░██║░░░██║░░░╚█████╔╝██║░░██║
    ░╚════╝░╚═════╝░╚═╝╚═╝░░╚══╝░░░╚═╝░░░  ╚═╝░░╚══╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝

                - Appuyer Enter                                         
    """
    print(Fore.BLUE + intro)
    input()

def print_banner():
    clear_screen()
    banner = """
    ░█████╗░░██████╗██╗███╗░░██╗████████╗  ███╗░░██╗░█████╗░██╗░░░██╗██╗░██████╗░░█████╗░████████╗░█████╗░██████╗░
    ██╔══██╗██╔════╝██║████╗░██║╚══██╔══╝  ████╗░██║██╔══██╗██║░░░██║██║██╔════╝░██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
    ██║░░██║╚█████╗░██║██╔██╗██║░░░██║░░░  ██╔██╗██║███████║╚██╗░██╔╝██║██║░░██╗░███████║░░░██║░░░██║░░██║██████╔╝
    ██║░░██║░╚═══██╗██║██║╚████║░░░██║░░░  ██║╚████║██╔══██║░╚████╔╝░██║██║░░╚██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗
    ╚█████╔╝██████╔╝██║██║░╚███║░░░██║░░░  ██║░╚███║██║░░██║░░╚██╔╝░░██║╚██████╔╝██║░░██║░░░██║░░░╚█████╔╝██║░░██║
    ░╚════╝░╚═════╝░╚═╝╚═╝░░╚══╝░░░╚═╝░░░  ╚═╝░░╚══╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
    """
    print(Fore.BLUE + banner)

def show_main_menu():
    print_banner()
    menu = "[01] -> IP                      [02] -> Email                [03] -> Nom prénoms          [04] -> Visage                [05] -> Crédits"
    print(Fore.BLUE + menu)
    option = input(Fore.BLUE + "\nChoisissez une option : ")
    return option

def ip_menu():
    while True:
        print_banner()
        menu = "[01] -> Snusbase                [02] -> Intelx               [03] -> Shodan               [04] -> Retour au menu"
        print(Fore.BLUE + menu)
        ip_option = input(Fore.BLUE + "\nChoisissez une option : ")
        if ip_option == "1":
            webbrowser.open("https://snusbase.com/")
        elif ip_option == "2":
            webbrowser.open("https://intelx.io/")
        elif ip_option == "3":
            webbrowser.open("https://www.shodan.io")
        elif ip_option == "4":
            break
        else:
            print(Fore.BLUE + "Option invalide, veuillez réessayer.")
        input(Fore.BLUE + "\nAppuyez sur Entrée pour continuer...")

def email_menu():
    while True:
        print_banner()
        menu = "[01] -> Hunter                  [02] -> HaveIBeenPwned       [03] -> Emailrep             [04] -> Epieos                [05] -> Snusbase             [06] -> Retour au menu"
        print(Fore.BLUE + menu)
        email_option = input(Fore.BLUE + "\nChoisissez une option : ")
        if email_option == "1":
            webbrowser.open("https://hunter.io")
        elif email_option == "2":
            webbrowser.open("https://haveibeenpwned.com")
        elif email_option == "3":
            webbrowser.open("https://emailrep.io")
        elif email_option == "4":
            webbrowser.open("https://epieos.com/")
        elif email_option == "5":
            webbrowser.open("https://snusbase.com/")              
        elif email_option == "6":
            break
        else:
            print(Fore.BLUE + "Option invalide, veuillez réessayer.")
        input(Fore.BLUE + "\nAppuyez sur Entrée pour continuer...")

def nom_menu():
    while True:
        print_banner()
        menu = "[01] -> Pipl                   [02] -> Social Searcher      [03] -> BeenVerified         [04] -> Pagesjaunes           [05] -> Retour au menu"
        print(Fore.BLUE + menu)
        nom_option = input(Fore.BLUE + "\nChoisissez une option : ")
        if nom_option == "1":
            webbrowser.open("https://pipl.com")
        elif nom_option == "2":
            webbrowser.open("https://www.social-searcher.com")
        elif nom_option == "3":
            webbrowser.open("https://www.beenverified.com")
        elif nom_option == "4":
            webbrowser.open("https://www.pagesjaunes.fr/pagesblanches")            
        elif nom_option == "5":
            break
        else:
            print(Fore.BLUE + "Option invalide, veuillez réessayer.")
        input(Fore.BLUE + "\nAppuyez sur Entrée pour continuer...")

def visage_menu():
    while True:
        print_banner()
        menu = "[01] -> ClearviewAI            [02] -> PimEyes              [03] -> BetaFace             [04] -> Retour au menu"
        print(Fore.BLUE + menu)
        visage_option = input(Fore.BLUE + "\nChoisissez une option : ")
        if visage_option == "1":
            webbrowser.open("https://clearview.ai")
        elif visage_option == "2":
            webbrowser.open("https://pimeyes.com")
        elif visage_option == "3":
            webbrowser.open("https://www.betafaceapi.com")
        elif visage_option == "4":
            break
        else:
            print(Fore.BLUE + "Option invalide, veuillez réessayer.")
        input(Fore.BLUE + "\nAppuyez sur Entrée pour continuer...")

def additional_tools_menu():
    while True:
        print_banner()
        menu = "[01] -> Discord                [02] -> Devlopper            [03] -> GitHub               [04] -> Voir la version        [05] -> Retour au menu"
        print(Fore.BLUE + menu)
        additional_option = input(Fore.BLUE + "\nChoisissez une option : ")
        if additional_option == "1":
            webbrowser.open("https://discord.gg/YRW2WgcrhR")
        elif additional_option == "2":
            print(Fore.BLUE + "\nDevlopper Tool By Blash")
        elif additional_option == "3":
            webbrowser.open("https://github.com/Blash-Dev")
        elif additional_option == "4":
            show_version()
        elif additional_option == "5":
            break
        else:
            print(Fore.BLUE + "Option invalide, veuillez réessayer.")
        input(Fore.BLUE + "\nAppuyez sur Entrée pour continuer...")

def show_version():
    print_banner()
    print(Fore.BLUE + f"Version du script : 1.2")
    input(Fore.BLUE + "\nAppuyez sur Entrée pour revenir au menu principal...")

def main():
    show_intro()
    while True:
        option = show_main_menu()

        if option == "1":
            ip_menu()
        elif option == "2":
            email_menu()
        elif option == "3":
            nom_menu()
        elif option == "4":
            visage_menu()
        elif option == "5":
            additional_tools_menu()
        else:
            print(Fore.BLUE + "Option invalide, veuillez réessayer.")
        input(Fore.BLUE + "\nAppuyez sur Entrée pour continuer...")

if __name__ == "__main__":
    main()
