import os
from colorama import init, Fore
import time
import ctypes
import webbrowser
from ctypes import wintypes
import shutil




def afficher_entete():
    """
    Affiche l'entête du terminal.
    """
    os.system('cls' if os.name == 'nt' else 'clear')  # Efface l'écran
    init(autoreset=True)  # Réinitialise les couleurs après chaque utilisation
    print(Fore.YELLOW + r'''
          
   ______  __                                       
 .' ___  |[  |                                      
/ .'   \_| | | .---.  ,--.   _ .--.  .---.  _ .--.  
| |        | |/ /__\\`'_\ : [ `.-. |/ /__\\[ `/'`\] 
\ `.___.'\ | || \__.,// | |, | | | || \__., | |     
 `.____ .'[___]'.__.'\'-;__/[___||__]'.__.'[___] 

          By AzA                                                               
''')
    
#Folder FiveM

#Command for clean Trash
shell32 = ctypes.WinDLL('shell32')
SHEmptyRecycleBin = shell32.SHEmptyRecycleBinW



def trash():
 
 result = SHEmptyRecycleBin(0, None, 0x00000001 | 0x00000002 | 0x00000004)


def Cache_delet():

    user_profile = os.environ['USERPROFILE']
         
    folders_to_delete = [
        os.path.join(user_profile,"AppData", "Local", "FiveM","Fivem.app","data","cache" ),
        
    ]

    for folder in folders_to_delete:
        if os.path.exists(folder):
            try:
                shutil.rmtree(folder)
                print(f"✅ {folder} was successfully deleted")
            except Exception as e:
                print(f"{folder} error while deleting : {e}")
        else:
            print(f"ℹ️ {folder} Not find or already deleted .")


 
    
    

def cleaner():
     
    user_profile = os.environ['USERPROFILE']

    
    folders_to_delete = [
        os.path.join(user_profile, "AppData", "Local", "D3DSCache"),
        os.path.join(user_profile, "AppData", "Local", "DigitalEntitlements")
    ]

    for folder in folders_to_delete:
        if os.path.exists(folder):
            try:
                shutil.rmtree(folder)
                print(f"✅ {folder} was successfully deleted")
            except Exception as e:
                print(f"{folder} error while deleting : {e}")
        else:
            print(f"ℹ️ {folder} Not find or already deleted .")

     
    

def main():
   while True:
        afficher_entete()
        
        choix = input(" 1- Clean FiveM \n 2- Clean Trash \n 3- My Discord \n 4- Error With FiveM Code Error --> 1000.104 \n Press Q for leave Error ")


        if choix.lower() == "q" or choix == "Q":
            print("Close in 5 sec")
            time.sleep(5)
            break
        
        elif choix == "1":
            cleaner()

            time.sleep(5)
            print("successful clean, Lunch FiveM")
        
        elif choix == "2":
            trash()
            print("Trash is clean")

        elif choix == "3":
           webbrowser.open("https://discord.gg/JDUEcPmBVt")
        
        elif choix == "4":
            Cache_delet()
            time.sleep(5)
            print("Your lunch is fixed, Lunch FiveM")
        
        else:
            print("❌ Choix invalide")

        input("\nAppuie sur Entrée pour continuer...")



if __name__ == "__main__":
    main()