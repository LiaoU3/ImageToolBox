# Image Tool Box

This is a python module to help us to do the tranformations between raw file, csv file, and numpy array.

## Requirements
It would be better if you got those version number bigger than these below
* python >= 3.9
* numpy >= 1.22
* pandas >= 1.4
* matplotlib >= 3.4.3
  
you can download those module for the latest version with the command below

```shell
handsomeguy@supercomputer:~$ pip install ImgToolBox
handsomeguy@supercomputer:~$ pip install numpy
handsomeguy@supercomputer:~$ pip install pandas
handsomeguy@supercomputer:~$ pip install matplotlib
```
## Usage example
your structure could probably look like this below

```
.
+-- yourpythonfile.py
|
+--src/
   +--catimage.raw
   +--dogimage.csv
|
+--output/
|
```
```python
# @yourpythonfile.py

import ImgToolBox.ImgFile as ITB

# you should put the path of raw file in the raw2arr fumction and you will get the numpy array from raw file
array = ITB.toArray('src/catimage.raw', (300, 800), dtype = '>u2')

# you can get the numpy array from the path of csv file
new_array = ITB.toArray('src/dogimage.csv')

# aftere doing this, you could get the csv file in the path you want
ITB.arr2csv(new_array, 'output/dogimage.csv')

# you can create a frame difference image by doing this
arr1 = np.array([50, 50, 50]).astype(np.uint8)
arr2 = np.array([10, 40, 90]).astype(np.uint8)
arr3 = ITB.imageDiff(arr1, arr2, 10)
# arr3 = [255   0 255]

# you can easily transform image array to histogram
ITB.saveHist(array, 'myHistogram.png', bins = 1024, title = "arr", xlim=(0, 1024), ylim=(0, 10000))
```

## Release History
* 1.0.0 init
* 1.1.0 package as class
* 1.2.0 fix some bugs
* 1.2.1 fix some bugs
* 1.2.2 fix some bugs
* 1.2.3 fix some bugs
* 1.2.4 fix some bugs
* 1.2.5 fix some bugs
* 1.2.6 Official version
* 1.2.7 update README.md
* 1.2.8 update the type hint of raw2arr
* 1.3.1 replace function csv2arr and raw2arr with toArray
* 1.4.1 merge **raw2arr()** and **csv2arr()** to **toArray()**, add **createDVS()**
and fix some type hint
* 1.5.1 modify **raw2arr()**, rename **createDVS()** with **imageDiff()** 
* 1.6.0 Add **saveHist()** which can easily transform image array to histogram and fix some hint
* 1.6.1 Modify **saveHist()** : fixed the bug that plot on the same figure

## Author
* Vincent Liao
    * LiaoU3@github
* Ian Lin
    * ianlin830410@github
* Kevin Kuo
    * Kuo-TingKai@github
## License
```
MIT License

Copyright (C) 2022 Vincent Liao

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```
