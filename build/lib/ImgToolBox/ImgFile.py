import pandas as pd
import numpy as np
from typing import Tuple
def raw2arr(rawPath: str, shape: Tuple[int, int]) -> np.ndarray:
    '''
    read a raw file as a numpy array

    Parameters
    ----------
    rawPath : str
        Path of the RAW file
    shape : tuple
        Shape of image array (row, col)

    Returns
    -------
    arr16b : np.array, dtype = np.uint16
        16-bit image array.
    '''
    raw = np.fromfile(rawPath, dtype=np.uint8)
    arr16b = np.reshape((raw[0::2] *256 + raw[1::2]), shape)
    return arr16b

def arr2csv(array: np.ndarray, csv_path_out: str) -> None:
    '''
    output the csv file from a numpy array

    Parameters
    ----------
    array : array
        A numpy array
    csv_path_out : str
        Path of outuput CSV file

    Returns
    ----------
    None
    '''
    # Convert a np.array into pd.DataFrame
    df = pd.DataFrame(array)
    # Convert a pd.DataFrame into csv
    df.to_csv(csv_path_out, header=False, index=False)

def csv2arr(csv_path_in:str) -> np.ndarray:
    '''
    read a csv file as a numpy array

    Parameters
    ----------
    csv_path_in : str
        Path of input CSV file

    Returns
    ----------
    arr : np.ndarray
        the numpy array of the csv file
    '''
    pd_data = pd.read_csv(csv_path_in,header=None, index_col=None)
    arr = pd_data.values
    return arr