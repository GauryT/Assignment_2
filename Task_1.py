# Task 1

import pandas as pd
from zipfile import ZipFile

zip_file_path = '/content/biobert/Assignment 2.zip'

extract_path = '/content/biobert/Assignment 2.zip'
# Unzip the folder containing CSV files
with ZipFile('/content/biobert/Assignment 2.zip', 'r') as zip_ref:
    zip_ref.extractall('unzipped_folder')

# with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
#    zip_ref.extractall(extract_path)
# Function to extract and concatenate text from specified columns in a CSV file
def extract_and_concatenate_text(csv_file_path, column_names):
    try:
        df = pd.read_csv(csv_file_path)
        # Check if all columns exist in the DataFrame
        missing_columns = [col for col in column_names if col not in df.columns]
        if not missing_columns:
            texts = []
            for col in column_names:

                texts.append(' '.join(df[col].astype(str)))
            return ' '.join(texts)
        else:
            print(f"The following columns do not exist in {csv_file_path}: {', '.join(missing_columns)}")
            return ''
    except Exception as e:
        print(f"An error occurred with file {csv_file_path}: {e}")
        return ''

# Dictionary mapping each CSV file to its specific column names
csv_files_columns = {
    'CSV1.csv': ['HADM_ID', 'SHORT-TEXT', 'ICD9_CODE', 'ICD9', 'Label'],  # Replace with actual column names for CSV1
    'CSV2.csv': ['HADM_ID', 'TEXT', 'LABLE', 'entites', 'group'],  # Replace with actual column names for CSV2
    'CSV3.csv': ['HADM_ID', 'TEXT', 'ICD9_CODE', 'Label'],  # Replace with actual column names for CSV3
    'CSV4.csv': ['HADM_ID', 'TEXT', 'LABLE'],  # Replace with actual column names for CSV3
}

# List to store extracted texts
all_texts = []

# Iterate through the dictionary and process each CSV file
for file_name, columns in csv_files_columns.items():
    csv_path = f'unzipped_folder/{file_name}'
    text = extract_and_concatenate_text(csv_path, columns)
    all_texts.append(text)

# Concatenate all texts into a single string
all_texts_combined = ' '.join(all_texts)

# Write the combined text to a .txt file
with open('combined_text.txt', 'w', encoding='utf-8') as txt_file:
    txt_file.write(all_texts_combined)

print("Task 1 Completed: Texts from specified columns in each CSV file have been extracted and stored in combined_text.txt.")
