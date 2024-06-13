# Excel File Splitter

This Python script splits a large Excel file into smaller files with a specified number of rows. It uses the `pandas` library to handle the Excel data and `tkinter` for a simple file selection dialog.

## Requirements

- Python 3.x
- pandas
- openpyxl
- tkinter

You can install the required packages using pip:

```bash
pip install pandas openpyxl tk
```

## Usage

1. Clone this repository or download the script.
2. Run the script. A file dialog will open to allow you to select the Excel file you want to split.
3. The script will split the selected file into chunks of 1000 rows each and save them as `part_1.xlsx`, `part_2.xlsx`, etc.

## Example

Suppose you have an Excel file named `large_file.xlsx` with 5000 rows. Running the script will create the following files:

- `part_1.xlsx` (rows 1 to 1000)
- `part_2.xlsx` (rows 1001 to 2000)
- `part_3.xlsx` (rows 2001 to 3000)
- `part_4.xlsx` (rows 3001 to 4000)
- `part_5.xlsx` (rows 4001 to 5000)

## Notes

- Ensure that the Excel file you select is properly formatted and does not contain any corrupted data.
- The script does not preserve any formulas or formatting from the original Excel file. It only copies the raw data.

## License

This project is licensed under the MIT License.
