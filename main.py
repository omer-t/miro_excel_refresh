import os
from datetime import datetime
from pathlib import Path

import win32api
import win32com.client
import win32con

start_time = datetime.now()


def timer():
    elapsed_time = (datetime.now() - start_time).seconds / 60
    return elapsed_time


def get_gdrive_file_stream_path():
    drives = ['E:\\', 'F:\\', 'G:\\', 'H:\\']
    for drive in drives:
        if os.path.exists(f"{drive}Shared drives"):
            return drive


def handle_backup_file(file_path: str):
    backup_path = str(file_path).replace(".xlsb", "_old_to_delete.xlsb")
    if os.path.exists(backup_path):
        os.remove(backup_path)
    if os.path.exists(file_path):
        os.rename(file_path, backup_path)


def refresh_excel_file():
    local_path = str(Path(__file__).resolve().parents[0])
    xlapp = win32com.client.DispatchEx("Excel.Application")

    file_name = 'paid_search.xlsb'

    # source_path = f"{local_path}/excel/{file_name}"
    # output_path = f"{local_path}/excel/{file_name}"
    gdrive_path = get_gdrive_file_stream_path()
    folder_path = f"{gdrive_path}\\Shared drives\\Performance Marketing Drive\\Reports\\Development"
    source_path = f"{folder_path}\\source\\{file_name}"
    output_path = f"{folder_path}\\output\\{file_name}"

    # Set file attributes to normal (removes read only file attributes)
    win32api.SetFileAttributes(source_path, win32con.FILE_ATTRIBUTE_NORMAL)

    # Open the workbook
    wb = xlapp.workbooks.open(source_path)
    xlapp.DisplayAlerts = False

    # Refresh all data connections.
    wb.RefreshAll()

    handle_backup_file(output_path)

    wb.Save()


def main():
    pass


if __name__ == "__main__":
    main()
