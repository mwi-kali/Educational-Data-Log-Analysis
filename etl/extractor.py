import logging

import pandas as pd


class DataExtractor:
    def __init__(self, data_paths: dict):
        """
        Initialize the extractor with a dictionary of file paths.

        Parameters
        -----------
        data_paths (dict): A dictionary with keys as dataset names and values as file paths.
        """
        self.data_paths = data_paths

    def extract(self) -> dict:
        """
        Extract data from the provided CSV file paths.

        Returns
        --------
        data (dict): A dictionary of pandas DataFrames keyed by dataset name.
        """
        data = {}
        try:
            logging.info("Starting extraction of CSV files...")
            for key, path in self.data_paths.items():
                data[key] = pd.read_csv(path)
                logging.info("Extracted '%s' from '%s'.", key, path)
            logging.info("Data extraction completed successfully.")
        except Exception as e:
            logging.error("Error during data extraction: %s", e)
            raise
        return data
