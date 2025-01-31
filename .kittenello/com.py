import os
import random
import subprocess
from loguru import logger
from sc_compression import compress
from sc_compression.signatures import Signatures

def create_folders():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    main_folder = os.path.dirname(script_dir)
    folders = [os.path.join(main_folder, "CSV", "In-Decompressed"), os.path.join(main_folder, "CSV", "Out-Compressed")]
    
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Folder '{folder}' has been created.")

def compress_csv(file_to_compress, folder, folder_export, signature):
    file_path = os.path.join(folder, file_to_compress)
    if os.path.isfile(file_path):
        try:
            with open(file_path, "rb") as f:
                file_data = f.read()
            compressed_data = compress(file_data, signature)
            output_file_path = os.path.join(folder_export, file_to_compress)
            with open(output_file_path, "wb") as f:
                f.write(compressed_data)
            print(f"File '{file_to_compress}' was successfully encrypted and saved to '{output_file_path}'. Encryption method: {signature}.")
            return True
        except Exception as exception:
            logger.exception(
                "Error during file encryption: {}, {}, {}"
                .format(
                    exception.__class__.__module__,
                    exception.__class__.__name__,
                    exception,
                )
            )
            return False
    else:
        print(f"File '{file_to_compress}' not found in folder '{folder}'.")
        return False

def compress_all_files(folder, folder_export, signature):
    files_to_compress = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    for file_name in files_to_compress:
        compress_csv(file_name, folder, folder_export, signature)

if __name__ == "__main__":
    create_folders()
    script_dir = os.path.dirname(os.path.abspath(__file__))
    main_folder = os.path.dirname(script_dir)
    folder = os.path.join(main_folder, "CSV", "In-Decompressed")
    folder_export = os.path.join(main_folder, "CSV", "Out-Compressed")
    while True:
        mode = input("Choose encryption mode:\n1. Encrypt one file\n2. Encrypt all files in the folder\n3. Return to main menu\nEnter mode number: ")
        if mode == "1" or mode == "2":
            print("Choose encryption method:")
            print("1. LZMA")
            print("2. SC")
            print("3. SCLZ")
            print("4. SIG")
            encryption_choice = input("\n\n < It's optional to enter the encryption method number. CSV Tools can choose a random encryption method by leaving the answer blank>\n\nEnter the encryption method number: ")
            encryption_methods = {
                "1": Signatures.LZMA,
                "2": Signatures.SC,
                "3": Signatures.SCLZ,
                "4": Signatures.SIG,
            }
            signature = encryption_methods.get(encryption_choice)
            if signature is None:
                signature = random.choice(list(encryption_methods.values()))
                print("A random encryption method has been chosen.")
                print(f"DEBUG: choosed {signature} method")
            if mode == "1":
                available_files = [f for f in os.listdir(folder) if f.endswith('.csv')]
                if not available_files:
                    print("No available files for encryption in 'In-Decompressed' folder.")
                else:
                    print("Available files for encryption:")
                    for index, file_name in enumerate(available_files):
                        print(f"{index + 1}. {file_name}")
                    
                    file_choice = int(input("\nEnter the file number for encryption: ")) - 1
                    if 0 <= file_choice < len(available_files):
                        file_to_compress = available_files[file_choice]
                        if compress_csv(file_to_compress, folder, folder_export, signature):
                            continue
                    else:
                        print("Invalid file number.")
            elif mode == "2":
                compress_all_files(folder, folder_export, signature)
        
        elif mode == "3":
            subprocess.run(["python", os.path.join(main_folder, "main.py")])
            break