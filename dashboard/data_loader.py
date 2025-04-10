import pandas as pd

class DataLoader:
    def __init__(self, file_path: str):
        """
        Initializes the DataLoader with the specified file path.
        
        Parameters
        -----------
        file_path (str): Path to the CSV file.
        """
        self.file_path = file_path

    def load_data(self) -> pd.DataFrame:
        """
        Loads the data from the CSV file.
        
        Returns
        --------
        pd.DataFrame: The loaded data.
            
        Raises
        --------
        Exception: If the file cannot be read.
        """
        try:
            data = pd.read_csv(self.file_path)
            return data
        except Exception as e:
            raise Exception(f"Error loading data from {self.file_path}: {e}")
