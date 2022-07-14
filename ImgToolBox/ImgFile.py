from optparse import Option
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple
from typing import Optional

def toArray(filepath: str, shape: Optional[Tuple[int, int]] = None, dtype = '>u2') -> np.ndarray:
    '''
    read a file(csv or raw) and turn it to a numpy array

    Parameters
    ----------
    filepath: str
        Path of the RAW or CSV file
    shape: tuple
        Shape of image array (row, col)

    Returns
    -------
    arr16b: np.array, dtype = np.uint16
        16-bit image array.
    
    Usage
    ------
    >>> arr1 = ITB.toArray('./yourraw.raw', (300, 800))
    >>> arr2 = ITB.toArray('./yourcsv.csv')
    '''
    
    def raw2arr(rawPath: str, shape: Tuple[int, int], dtype = '>u2') -> np.ndarray:
        '''
        read a 16bit raw file as a numpy array

        Parameters
        ----------
        rawPath: str
            Path of the RAW file
        shape : tuple
            Shape of image array (row, col)

        Returns
        -------
        arr16b: np.array, dtype = np.uint16
            16-bit image array.
        '''
        raw = np.fromfile(rawPath, dtype = dtype)
        arr16b = np.reshape(raw, shape)
        return arr16b

    def csv2arr(csv_path_in:str) -> np.ndarray:
        '''
        read a csv file as a numpy array

        Parameters
        ----------
        csv_path_in: str
            Path of input CSV file

        Returns
        ----------
        arr: np.ndarray
            the numpy array of the csv file
        '''
        pd_data = pd.read_csv(csv_path_in,header=None, index_col=None)
        arr = pd_data.values
        return arr

    if filepath[-3:] == 'csv':
        return csv2arr(filepath)
    elif filepath[-3:] == 'raw':
        return raw2arr(filepath, shape, dtype = dtype)

def arr2csv(array: np.ndarray, csv_path_out: str) -> None:
    '''
    output to the csv file from a numpy array

    Parameters
    ----------
    array: array
        A numpy array
    csv_path_out: str
        Path of outuput CSV file

    Returns
    ----------
    None

    Usage
    ---------
    >>> arr = np.array([1, 2, 3])
    >>> ITB.arr2csv(arr, './yourcsv.csv')
    '''
    # Convert a np.array into pd.DataFrame
    df = pd.DataFrame(array)
    # Convert a pd.DataFrame into csv
    df.to_csv(csv_path_out, header=False, index=False)

def imageDiff(img1: np.ndarray, img2: np.ndarray, threshold: int, above_thresh_val: Optional[int] = None, below_thresh_val: Optional[int] = 0) -> np.ndarray:
    '''
    return a dvs img by calculating the difference between img1 and img2

    Parameters
    ----------
    img1: np.ndarray
        first image
    img2: np.ndarray
        secion image
    threshold: int
        the threshold of abs(img1-img2)

    above_thresh_val: Optional[int] = None
        if the value after abs(img1-img2) is bigger than threshold, then set it to above_thresh_val

    Returns
    ----------
    dvs: np.ndarray

    Usage
    ----------
    >>> arr1 = np.array([50, 50, 50]).astype(np.uint8)
    >>> arr2 = np.array([10, 40, 90]).astype(np.uint8)
    >>> ITB.imageDiff(arr1, arr2, 10)
    [255   0 255]
    '''

    if not above_thresh_val:
        above_thresh_val = np.iinfo(img1.dtype).max
    dvs = np.where(img1>img2, img1-img2, img2-img1)

    dvs[dvs > threshold] = above_thresh_val
    dvs[threshold >= dvs] = below_thresh_val
    return dvs

def saveHist(src: np.ndarray, path: str = "output.png", bins: int = 256, title: str = "", xlim: Optional[tuple] = None, ylim: Optional[tuple] = None ) -> None:
    '''
    Save a histogram for the source image

    Parameters
    ----------
    src: np.ndarray
        the source image
    path: str
        the output path of histogram
    bins: int
        the bins of histogram, usually be 256 or 1024
    title: str
        the title of histogram, usually be the image name
    xlim: Optional[tuple]
        the limitation of x
    ylim: Optional[tuple]
        the limitation of y
    Returns
    ----------
    None

    Usage
    ----------
    >>> arr = np.array([50, 50, 50]).astype(np.uint8)
    >>> ITB.saveHist(arr, 'myHistogram.png', bins = 256, title = "arr", xlim=(0, 100), ylim=(0, 1000))
    '''
    plt.hist(src.flatten(), bins)
    plt.title(title)
    plt.xlabel('Intensity')
    plt.ylabel('Count')
    if xlim:
        plt.xlim(xlim)
    if ylim:
        plt.ylim(ylim)
    plt.savefig(path)