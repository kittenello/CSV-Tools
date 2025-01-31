import os
import pystyle
from pystyle import Colorate, Colors
import subprocess
from colorama import init, Fore

init(autoreset=True)

print(Colorate.Horizontal(Colors.blue_to_white, (""" 
 ________  ________  ___      ___            _________  ________  ________  ___       ________      
|\   ____\|\   ____\|\  \    /  /|          |\___   ___\\   __  \|\   __  \|\  \     |\   ____\     
\ \  \___|\ \  \___|\ \  \  /  / /__________\|___ \  \_\ \  \|\  \ \  \|\  \ \  \    \ \  \___|_    
 \ \  \    \ \_____  \ \  \/  / /\____________\  \ \  \ \ \  \\\  \ \  \\\  \ \  \    \ \_____  \   
  \ \  \____\|____|\  \ \    / /\|____________|   \ \  \ \ \  \\\  \ \  \\\  \ \  \____\|____|\  \  
   \ \_______\____\_\  \ \__/ /                    \ \__\ \ \_______\ \_______\ \_______\____\_\  \ 
    \|_______|\_________\|__|/                      \|__|  \|_______|\|_______|\|_______|\_________\                                                               
                                                                                                                  
                      ╔═════════════════════════════════════════════════════════════════════════════╗
                      ║ [1] - Updater                  ║ [4] - How to Use                           ║
                      ║ [2] - Compress                 ║ [5] - Check Update                         ║
                      ║ [3] - Decompress               ║ [6] - Exit                                 ║
                      ║                          [7] - Clear Folders                                ║
                      ║                          [111] - Author                                     ║
                      ╚═════════════════════════════════════════════════════════════════════════════╝
""").strip()))

while True:
    bs = input(Colorate.Horizontal(Colors.blue_to_white, ("\n[#] -> Choose: ").strip()))

    if bs == "111":
        print(Colorate.Horizontal(Colors.blue_to_white, (f"\n\nAuthor: kittenello\nCompressor & Decompressor by XCoder(Danila-Schelkov). Updater was maded by kittenello.").strip()))
    elif bs == "1":
        current_dir = os.path.dirname(os.path.abspath(__file__))
        kittenello_dir = os.path.join(current_dir, ".kittenello")
        script_path = os.path.join(kittenello_dir, "updater.py")
        if os.path.isdir(kittenello_dir) and os.path.isfile(script_path):
            subprocess.run(["python", script_path])
        else:
            print("Error")
    elif bs == "2":
        current_dir = os.path.dirname(os.path.abspath(__file__))
        kittenello_dir = os.path.join(current_dir, ".kittenello")
        script_path = os.path.join(kittenello_dir, "compress.py")
        if os.path.isdir(kittenello_dir) and os.path.isfile(script_path):
            subprocess.run(["python", script_path])
        else:
            print("error")
    elif bs == "3":
        current_dir = os.path.dirname(os.path.abspath(__file__))
        kittenello_dir = os.path.join(current_dir, ".kittenello")
        script_path = os.path.join(kittenello_dir, "decompress.py")
        if os.path.isdir(kittenello_dir) and os.path.isfile(script_path):
            subprocess.run(["python", script_path])
        else:
            print("Error")
    elif bs == "4":
        while True:
            print(Colorate.Horizontal(Colors.blue_to_white, ("""
            [1] - Decompress                                                    
            [2] - Compress                                                      
            [3] - Updater                                                       
            [4] - Exit to Main Menu                                             
            """).strip()))
        
            tool_choice = input(Colorate.Horizontal(Colors.blue_to_white, ("\n[#] -> Choose: ").strip()))
        
            if tool_choice == "1":
                print("Decompress tutorial:")
                print("Paste your compressed csv into the 'In-Compressed' folder. Run Decompress tool and Ready! Your decompressed files will be in folder 'Out-Decompressed")
                input("Press Enter to return to the previous menu.")
            elif tool_choice == "2":
                print("Compress tutorial:")
                print("Paste your decompressed csv into the 'In-Decompressed' folder. Run Decompress tool and Ready! Your decompressed files will be in folder 'Out-Compressed")
                input("Press Enter to return to the previous menu.")
            elif tool_choice == "3":
                print("Updater tutorial:")
                print("Paste your old modified CSV into the 'old' folder, then paste the new clean csv into the original_new folder.\nReady! You can run them, but the most important thing is that they have the same name, otherwise it won't be updated. \nThe result of the updated csv will be in the result folder. \nUpdater does not work well with some csv because it was created manually, but it will improve")
                input("Press Enter to return to the previous menu.")
            elif tool_choice == "4":
                break
            else:
                print(Fore.RED + "Error. Please choose the a right number.")
    elif bs == "5":
        print("Soon will be released")
#updater_path = os.path.join(os.path.dirname(__file__), ".kittenello", "github.py")
#subprocess.run(["python", updater_path])
    elif bs == "6":
        break
    elif bs == "7":
        current_dir = os.path.dirname(os.path.abspath(__file__))
        kittenello_dir = os.path.join(current_dir, ".kittenello")
        script_path = os.path.join(kittenello_dir, "directories.py")
        if os.path.isdir(kittenello_dir) and os.path.isfile(script_path):
            subprocess.run(["python", script_path])
        else:
            print("Error")
    else:
        print(Fore.RED + "Error. Please choose a right number.")