import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


import xlwings as xw


def write_to_excel(path):
    # Connect to the open Excel application
    app = xw.App(visible=True)
    # Replace with your actual path
    workbook = app.books.open(path)

    try:
        # Access the active sheet
        sheet = workbook.sheets.active

        # Write data to specific cells
        for i in range(1, 10):  # Update the range as needed
            sheet.range(f'A{i}').value = f'Real-time Updated Data {i}'
            time.sleep(1)
            print(i)

    finally:
        # Save and close the workbook
        workbook.save()
        workbook.close()

        # Quit Excel application
        app.quit()


# class excelRepository:
#     def run(self, pathFolder):
#         # Create a new Excel workbook and select the active sheet
#         pathFile = pathFolder + "\\example.xlsx"
#         workbook = openpyxl.load_workbook(pathFile, read_only=False)
#         sheet = workbook.active

#         # Write data to the Excel sheet
#         for i in range(1, 100):
#             sheet[f"A{i}"] = "Hello"
#             sheet[f"B{i}"] = "World!"
#             time.sleep(1)
#             print(i)

#         # Save the workbook to a file
#         workbook.save(pathFile)

#         print("Excel file created and data written successfully.")
