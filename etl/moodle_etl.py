import logging

from extractor import DataExtractor
from loader import DataLoader
from transformer import DataTransformer


def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
    data_paths = {
        'activity_counts': '../data/activity_counts.csv',
        'country_gender': '../data/country_gender.csv',
        'dedication_time': '../data/dedication_time.csv',
        'login_counts': '../data/login_counts.csv'
    }

    extractor = DataExtractor(data_paths)
    transformer = DataTransformer()
    loader = DataLoader()

    try:
        data = extractor.extract()
        transformed_df = transformer.transform(data)
        
        output_path = '../data/etl_output.csv'
        loader.load_to_csv(transformed_df, output_path)

        logging.info("ETL process completed successfully.")
    except Exception as e:
        logging.error("ETL process encountered an error: %s", e)

if __name__ == '__main__':
    main()
