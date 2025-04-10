import logging

import pandas as pd


class DataLoader:
    def __init__(self):
        """
        Initialize the loader.
        """
        pass

    def load_to_csv(self, df: pd.DataFrame, output_path: str) -> None:
        """
        Save the DataFrame to a CSV file.

        Parameters
        -----------
        df (pd.DataFrame): The transformed DataFrame.
        output_path (str): Path to save the CSV file.
        """
        try:
            logging.info("Starting to load data to CSV...")
            df.to_csv(output_path, index=False)
            logging.info("Data successfully saved to '%s'.", output_path)
        except Exception as e:
            logging.error("Error during data loading: %s", e)
            raise
