# Image Tool Box
----
This is a python module to help us to do the tranformations between raw file, csv file, and numpy array.

## Requirements
* python==3.10
* numpy==1.22
* pandas==1.4

you can donload those module for the latest version with the command below

```shell
handsomeguy@supercomputer:~$ pip install numpy
handsomeguy@supercomputer:~$ pip install pandas
```
## Usage example
your structure should look like this below

```
.
+-- yourpythonfile.py
+-- ImgToolBox.py
|
+--src/
   +--catimage.raw
   +--dogimage.csv
|
+--output/
|
```
```python
# yourpythonfile.py

from ImgToolBox import raw2arr, arr2csv, csv2arr

# you should put the path of raw file in the raw2arr fumction and you will get the numpy array from raw file
array = raw2arr('src/catimage.raw')

# now you can get the numpy array from the path of csv file
new_array = csv2arr('src/dogimage.csv')

# aftere doing this, you could get the csv file in the path you want
arr2csv(new_array, 'output/dogimage.csv')

```

## Release History
* 1.0.0 init

## Author
* Vincent Liao
    * LiaoU3@github
* Ian Lin
    * ianlin830410@github

## License
Copyright © 2022, LiaoU3
Copyright © 2022, Ian Lin