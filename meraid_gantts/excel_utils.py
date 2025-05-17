# File: /meraid-gantts/meraid_gantts/excel_utils.py

def load_excel_data(file_path):
    """
    Load data from the specified Excel file.

    Args:
        file_path (str): The path to the Excel file.

    Returns:
        DataFrame: A pandas DataFrame containing the loaded data.
    """
    import pandas as pd
    return pd.read_excel(file_path)

def save_excel_data(dataframe, file_path):
    """
    Save the specified DataFrame to an Excel file.

    Args:
        dataframe (DataFrame): The DataFrame to save.
        file_path (str): The path where the Excel file will be saved.
    """
    import pandas as pd
    dataframe.to_excel(file_path, index=False)