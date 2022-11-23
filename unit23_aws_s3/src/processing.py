import pandas as pd

from unit23_aws_s3.configs.logging_setup import logger_p


def process_data(input_path: str, output_path: str) -> None:
    """Accepts a .xlsx file, processes it and saves it as .xlsx file.

    :param input_path: Path to the file to be processed
    :type input_path: str
    :param output_path: Path to the filtered file
    :type output_path: str
    """

    try:
        logger_p.info('Initializing data processing...')

        medals_df = pd.read_excel(input_path)
    except FileNotFoundError:
        logger_p.error('File not found')
    except Exception as e:
        logger_p.error('Error, something went wrong', e)
    else:
        # Filters information considering columns: Sport, Event gender and
        # Medal
        medals_filtered_df = medals_df[(medals_df['Sport'] == 'Skating') &
                                       (medals_df['Event gender'] == 'W') &
                                       (medals_df['Medal'] == 'Silver')]

        medals_filtered_df.to_excel(output_path, index=False)

        logger_p.info('Data processing finished')
