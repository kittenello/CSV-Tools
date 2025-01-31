import os
import shutil
from colorama import init, Fore

init(autoreset=True)
base_dir = os.path.dirname(os.path.abspath(os.path.join(__file__, '..')))
total_files_deleted = 0

for i in ["In", "Out"]:
    for k in ["Compressed", "Decompressed"]:
        folder = os.path.join(base_dir, f"CSV/{i}-{k}")
        if os.path.isdir(folder):
            try:
                files_before = len(os.listdir(folder))
                shutil.rmtree(folder)
                os.makedirs(folder, exist_ok=True)
                total_files_deleted += files_before
            except Exception as e:
                print(Fore.RED + f"\nError: '{folder}': {e}\n")

updater_base = os.path.join(base_dir, 'CSV', 'Updater')
for subfolder in ['old', 'original_new', 'result']:
    folder = os.path.join(updater_base, subfolder)
    if os.path.isdir(folder):
        try:
            files_before = len(os.listdir(folder))
            shutil.rmtree(folder)
            os.makedirs(folder, exist_ok=True)
            total_files_deleted += files_before
        except Exception as e:
            print(Fore.RED + f"\nError: '{folder}': {e}\n")

if total_files_deleted > 0:
    print(Fore.GREEN + f"\nAll folders cleared!\nDeleted Files: {total_files_deleted}.\n")
else:
    print(Fore.RED + "\nCan't clear files or there is nothing to delete.\n")