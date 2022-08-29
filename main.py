
from pathlib import Path

import modules.snowflake as sf
import win32api
import win32com.client
import win32con


def main():
    local_path = str(Path(__file__).resolve().parents[0])
    xlapp = win32com.client.DispatchEx("Excel.Application")

    file_name = 'paid_search.xlsx'

    source_file = f"{local_path}/excel/{file_name}"
    # destination_file = f"{local_path}/excel/{file_name}"

    # Set file attributes to normal (removes read only file attributes)
    win32api.SetFileAttributes(source_file, win32con.FILE_ATTRIBUTE_NORMAL)

    # Open the workbook
    wb = xlapp.workbooks.open(source_file)
    xlapp.DisplayAlerts = False

    # Optional, e.g. if you want to debug
    xlapp.Visible = True

    # Refresh all data connections.
    wb.RefreshAll()
    # try:
    #     wb.RefreshAll()
    # except Exception:
    #     wb.Close(True)
    #     continue

    wb.Save()



if __name__ == "__main__":
    main()
