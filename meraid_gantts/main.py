# File: /meraid-gantts/meraid_gantts/main.py

import tkinter as tk
from pathlib import Path
from tkinter import filedialog

from excel_utils import load_data
from export_to_msproject import export_gantt_to_msproject_excel
from markdown_utils import update_markdown


def select_file_dialog(prompt_message, filetypes):
    """
    Open a file dialog for the user to select a file.
    Args:
        prompt_message (str): The message to display in the dialog title.
        filetypes (list): List of (label, pattern) tuples for file types, e.g. [("Excel files", "*.xlsx")]
    Returns:
        Path: The selected file path as a pathlib.Path object, or None if cancelled.
    """
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(title=prompt_message, filetypes=filetypes)
    root.destroy()
    return Path(file_path) if file_path else None


def main():
    print("Welcome to the Mermaid Gantt Chart Creation and Update Tool!")
    print("Options:")
    print("1. Create a new markdown Gantt chart from Excel")
    print("2. Update an existing markdown Gantt chart from Excel")
    print("3. Export an existing markdown Gantt chart to Excel for Microsoft Project import")
    option = input("Please enter 1 to create, 2 to update, or 3 to export: ").strip()

    if option == '1':
        input_excel_file = select_file_dialog(
            "Please select the input Excel file:", [("Excel files", "*.xlsx *.xls")]
        )
        if not input_excel_file:
            print("No Excel file selected. Exiting.")
            return
        markdown_file = select_file_dialog(
            "Please select the markdown file to create the Gantt chart in:", [("Markdown files", "*.md")]
        )
        if not markdown_file:
            print("No markdown file selected. Exiting.")
            return
        data = load_data(str(input_excel_file))
        update_markdown(str(markdown_file), data, create_new=True)
        print("Processing complete. New Gantt chart has been created.")
    elif option == '2':
        input_excel_file = select_file_dialog(
            "Please select the input Excel file:", [("Excel files", "*.xlsx *.xls")]
        )
        if not input_excel_file:
            print("No Excel file selected. Exiting.")
            return
        markdown_file = select_file_dialog(
            "Please select the markdown file to update the Gantt chart in:", [("Markdown files", "*.md")]
        )
        if not markdown_file:
            print("No markdown file selected. Exiting.")
            return
        data = load_data(str(input_excel_file))
        update_markdown(str(markdown_file), data, create_new=False)
        print("Processing complete. Gantt chart has been updated.")
    elif option == '3':
        markdown_file = select_file_dialog(
            "Please select the markdown file containing the Gantt chart:", [("Markdown files", "*.md")]
        )
        if not markdown_file:
            print("No markdown file selected. Exiting.")
            return
        output_excel_file = select_file_dialog(
            "Please select the output Excel file (or enter a new filename):", [("Excel files", "*.xlsx")]
        )
        if not output_excel_file:
            print("No Excel file selected. Exiting.")
            return
        export_gantt_to_msproject_excel(str(markdown_file), str(output_excel_file))
        print("Processing complete. Gantt chart exported for Microsoft Project import.")
    else:
        print("Invalid option. Please run the program again and select 1, 2, or 3.")

if __name__ == "__main__":
    main()