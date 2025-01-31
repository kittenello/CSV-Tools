import requests
import os
import zipfile
import shutil

def download_update():
    url = "https://github.com/kittenello/CSV-Tools/archive/refs/heads/main.zip"
    response = requests.get(url)

    if response.status_code == 200:
        with open("update.zip", "wb") as f:
            f.write(response.content)
        print("Обновление загружено.")
    else:
        print("Ошибка при загрузке обновления.")
        exit(1)

def extract_update():
    with zipfile.ZipFile("update.zip", "r") as zip_ref:
        zip_ref.extractall(".")

def replace_files():
    update_folder = "update.zip"
    current_folder = os.getcwd()

    for item in os.listdir(update_folder):
        s = os.path.join(update_folder, item)
        d = os.path.join(current_folder, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            shutil.copy2(s, d)

    shutil.rmtree(update_folder)

if __name__ == "__main__":
    download_update()
    extract_update()
    replace_files()
    os.remove("update.zip")
    print("Обновление завершено. Перезапуск main.py...")
    os.execv("python", ["python", "main.py"])