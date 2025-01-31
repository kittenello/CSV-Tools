import os
import csv
from colorama import init, Fore

init(autoreset=True)

def read_csv_to_dict(file_path):
    data = {}
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                tid = row[0]
                data[tid] = row
    return data

def write_dict_to_csv(data, file_path):
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for row in data.values():
            writer.writerow(row)

def update_csvs(old_folder, new_folder, result_folder):
    old_files = [f for f in os.listdir(old_folder) if f.endswith('.csv')]
    new_files = [f for f in os.listdir(new_folder) if f.endswith('.csv')]

    if not old_files and not new_files:
        print(f"{Fore.RED}No CSV files found in both 'old' and 'original_new' folders for updating.\n(either you didn't insert all the files or you inserted them in the wrong place.)")
        return

    for old_file in old_files:
        old_file_path = os.path.join(old_folder, old_file)
        new_file_path = os.path.join(new_folder, old_file)

        if not os.path.exists(new_file_path):
            print(f"{Fore.RED}The original {old_file} file is missing!")
            continue

        old_data = read_csv_to_dict(old_file_path)
        new_data = read_csv_to_dict(new_file_path)

        combined_data = old_data.copy()
        added_count = 0

        for tid, new_row in new_data.items():
            if tid not in old_data:
                combined_data[tid] = new_row 
                added_count += 1

        result_file_path = os.path.join(result_folder, old_file)
        write_dict_to_csv(combined_data, result_file_path)

        print(f"\n{Fore.BLUE}Working with file: {Fore.MAGENTA}{old_file}")
        print(f"{added_count} lines changed or added...")
        print(f"{Fore.GREEN}{old_file} saved!")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(os.path.join(__file__, '..')))
    csv_base_path = os.path.join(base_dir, 'CSV')
    updater_folder = os.path.join(csv_base_path, 'Updater')
    old_folder = os.path.join(updater_folder, 'old')
    new_folder = os.path.join(updater_folder, 'original_new')
    result_folder = os.path.join(updater_folder, 'result')

    os.makedirs(updater_folder, exist_ok=True)
    os.makedirs(old_folder, exist_ok=True)
    os.makedirs(new_folder, exist_ok=True)
    os.makedirs(result_folder, exist_ok=True)

    update_csvs(old_folder, new_folder, result_folder)
    input("")