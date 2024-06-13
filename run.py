import pandas as pd
import tkinter as tk
from tkinter import filedialog

# Create a Tkinter root window
root = tk.Tk()
root.withdraw()  # Hide the Tkinter window

# File selection dialog
file_path = filedialog.askopenfilename(title="Select an Excel file", filetypes=[("Excel files", "*.xlsx *.xls")])

if file_path:
    # Read the main Excel file
    df = pd.read_excel(file_path)

    # Specify the number of rows per chunk
    chunk_size = 1000

    # Split the file into chunks
    for i in range(0, len(df), chunk_size):
        chunk = df.iloc[i:i + chunk_size]
        chunk_file_path = f'part_{i // chunk_size + 1}.xlsx'
        chunk.to_excel(chunk_file_path, index=False)

        print(f'{chunk_file_path} created.')

    print("File splitting completed.")
else:
    print("No file selected.")
