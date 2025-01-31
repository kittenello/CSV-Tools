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
            print(f"Папка '{folder}' была создана.")

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
            print(f"Файл '{file_to_compress}' успешно зашифрован и сохранен в '{output_file_path}'. Способ шифрования: {signature}.")
            return True
        except Exception as exception:
            logger.exception(
                "Ошибка при шифровании файла: {}, {}, {}"
                .format(
                    exception.__class__.__module__,
                    exception.__class__.__name__,
                    exception,
                )
            )
            return False
    else:
        print(f"Файл '{file_to_compress}' не найден в папке '{folder}'.")
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
        mode = input("Выбери режим шифрования:\n1. Шифровать по одному файлу\n2. Шифровать сразу все файлы в папке\n3. Вернуться в главное меню\nВведите номер режима: ")
        if mode == "1" or mode == "2":
            print("Выбери метод шифрования:")
            print("1. LZMA")
            print("2. SC")
            print("3. SCLZ")
            print("4. SIG")
            encryption_choice = input("\n\n < Не обязательно вводить номер метода. CSV Tools может выбрать рандомный метод шифрования просто оставьте пустой ответ>\n\nВведи номер метода шифрования: ")

            encryption_methods = {
                "1": Signatures.LZMA,
                "2": Signatures.SC,
                "3": Signatures.SCLZ,
                "4": Signatures.SIG,
            }

            signature = encryption_methods.get(encryption_choice)
            if signature is None:
                signature = random.choice(list(encryption_methods.values()))
                print("Выбран случайный метод шифрования.")
                print(f"DEBUG: choosed {signature} method")

            if mode == "1":
                available_files = [f for f in os.listdir(folder) if f.endswith('.csv')]
                if not available_files:
                    print("Нет доступных файлов для шифрования в папке 'In-Decompressed'.")
                else:
                    print("Доступные файлы для шифрования:")
                    for index, file_name in enumerate(available_files):
                        print(f"{index + 1}. {file_name}")
                    
                    file_choice = int(input("\nВведите номер файла для шифрования: ")) - 1
                    if 0 <= file_choice < len(available_files):
                        file_to_compress = available_files[file_choice]
                        if compress_csv(file_to_compress, folder, folder_export, signature):
                            continue
                    else:
                        print("Неверный номер файла.")
            elif mode == "2":
                compress_all_files(folder, folder_export, signature)
        
        elif mode == "3":
            subprocess.run(["python", os.path.join(main_folder, "main.py")])
            break