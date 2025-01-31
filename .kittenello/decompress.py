import os
from loguru import logger
from sc_compression import decompress
from colorama import init, Fore

init(autoreset=True)

def create_folders_if_not_exist(folder, folder_export):
    for dir_path in [folder, folder_export]:
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            print(f"Folder '{dir_path}' has been created.")

def decompress_csv():
    base_dir = os.path.dirname(os.path.abspath(os.path.join(__file__, '..')))
    folder = os.path.join(base_dir, "CSV/In-Compressed")
    folder_export = os.path.join(base_dir, "CSV/Out-Decompressed")
    
    # Создаем папки, если они не существуют
    create_folders_if_not_exist(folder, folder_export)
    
    if not os.path.exists(folder):
        print(f"The folder '{folder}' was not found.")
        return
    
    csv_files = [file for file in os.listdir(folder) if file.endswith(".csv")]
    if not csv_files:
        print("No available files for decompression.")
        return
    
    mode = input("Choose decompression mode:\n1. Decompress one file\n2. Decompress all files\nEnter mode number: ")
    if mode == "1":
        print("Available files for decompression:")
        for index, file in enumerate(csv_files):
            print(f"{index + 1}. {file}")
        file_choice = input("Enter the file number to decompress: ")
        try:
            file_index = int(file_choice) - 1
            if 0 <= file_index < len(csv_files):
                file_to_decompress = csv_files[file_index]
                process_file(folder, folder_export, file_to_decompress)
            else:
                print("Invalid file number.")
        except ValueError:
            print("Please enter a valid number.")
    elif mode == "2":
        for file in csv_files:
            process_file(folder, folder_export, file)
    else:
        print("Invalid mode.")

def process_file(folder, folder_export, file):
    try:
        with open(os.path.join(folder, file), "rb") as f:
            file_data = f.read()
        decompressed_data = decompress(file_data)[0]
        if decompressed_data:
            with open(os.path.join(folder_export, file), "wb") as f:
                f.write(decompressed_data)
            print(f"The file {file} was successfully decompressed and saved to {folder_export}.")
        else:
            print(f"Error: The data of the file {file} was not decompressed.")
    except Exception as exception:
        logger.exception(f"Error processing file {file}: {exception}")
        print(Fore.RED + f"Error processing file {file}.")

decompress_csv()