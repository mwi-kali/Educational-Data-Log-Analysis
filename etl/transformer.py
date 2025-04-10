import logging

import numpy as np
import pandas as pd


class DataTransformer:
    def __init__(self):
        self.transformed_df = None

    def merge_datasets(self, data: dict) -> pd.DataFrame:
        """
        Merge the datasets on 'user_id'.

        Parameters
        -----------
        data (dict): A dictionary of pandas DataFrames with keys.

        Returns
        --------
        pd.DataFrame: The merged DataFrame.
        """
        try:
            logging.info("Starting dataset merge...")
            df = pd.merge(data['activity_counts'], data['country_gender'], on='user_id', how='left')
            logging.info("Merged activity_counts with country_gender.")
            df = pd.merge(df, data['dedication_time'], on='user_id', how='left')
            logging.info("Merged with dedication_time.")
            df = pd.merge(df, data['login_counts'], on='user_id', how='left')
            logging.info("Merged with login_counts.")
        except Exception as e:
            logging.error("Error during merging: %s", e)
            raise
        return df

    def compute_metrics(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Compute additional metrics including average_activity and performance_bracket.

        Parameters
        -----------
        df (pd.DataFrame): The merged DataFrame.

        Returns
        --------
        pd.DataFrame: DataFrame with new metrics.
        """
        try:
            logging.info("Computing average_activity metric...")
            df['average_activity'] = df['activity_count'] / df['login_count'].replace(0, np.nan)

            logging.info("Creating performance_bracket using quantiles...")
            df['performance_bracket'] = pd.qcut(
                df['activity_count'],
                q=[0, 0.01, 0.05, 0.10, 0.25, 1.0],
                labels=['top 1%', 'top 5%', 'top 10%', 'top 25%', 'others']
            )
            logging.info("Metrics computed successfully.")
        except Exception as e:
            logging.error("Error during metric computation: %s", e)
            raise
        return df

    def transform(self, data: dict) -> pd.DataFrame:
        """
        Perform the full transformation process: merge datasets and compute derived metrics.

        Parameters
        -----------
        data (dict): Dictionary of extracted DataFrames.

        Returns
        --------
        pd.DataFrame: The fully transformed DataFrame.
        """
        try:
            merged_df = self.merge_datasets(data)
            self.transformed_df = self.compute_metrics(merged_df)
            logging.info("Data transformation completed successfully.")
        except Exception as e:
            logging.error("Error in transformation process: %s", e)
            raise
        return self.transformed_df
