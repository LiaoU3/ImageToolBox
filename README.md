# Image Tool Box
----
This is a python module to help us to do the tranformations between raw file, csv file, and numpy array.

## Requirements
It would be better if you got those version number bigger than these below
* python>=3.9
* numpy>=1.22
* pandas>=1.4

you can download those module for the latest version with the command below

```shell
handsomeguy@supercomputer:~$ pip install ImgToolBox
handsomeguy@supercomputer:~$ pip install numpy
handsomeguy@supercomputer:~$ pip install pandas
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
array = ITB.raw2arr('src/catimage.raw')

# now you can get the numpy array from the path of csv file
new_array = ITB.csv2arr('src/dogimage.csv')

# aftere doing this, you could get the csv file in the path you want
ITB.arr2csv(new_array, 'output/dogimage.csv')

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

## Author
* Vincent Liao
    * LiaoU3@github
* Ian Lin
    * ianlin830410@github

## License
```
MIT License

Copyright (C) 2022 Vincent Liao

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```