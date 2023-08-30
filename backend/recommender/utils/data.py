import pandas as pd
import os
from termcolor import colored
from .params import LOCAL_DATA_PATH


def get_local_data(data_file_name, nrows=None):
  '''
	Method to get data from the local machine

  Args:
    data_file_name (str): Name of the data file to load.
    nrows (int, optional): Number of rows to load from the data file. If set to None, all rows are loaded.
        
  Returns:
    pandas.DataFrame or None: The loaded DataFrame if successful, None if the file is not found.
  '''
  abspath = os.path.join(LOCAL_DATA_PATH, data_file_name)
  try:
    df = pd.read_csv(abspath, nrows=nrows)
    if nrows:
      print(colored(f"{nrows} rows loaded from {LOCAL_DATA_PATH}/{data_file_name}","green"))
    else:
      print(colored(f"data loaded from {LOCAL_DATA_PATH}/{data_file_name}","green"))
      return df
  except FileNotFoundError:
    print(colored(f"{data_file_name} not found in {LOCAL_DATA_PATH}","red"))
    return None
  
if __name__ == '__main__':
  df = get_local_data()
  print(df.head())