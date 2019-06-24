## NonoPy: Nonogram generator for Python
* Based on Python 3 + Pillow
* Includes [Apache Licensed product](http://www.apache.org/licenses/LICENSE-2.0) , Open Sans.

### Dependencies
* Pillow
* NumPy

### Example
```python
import nonogram

#input filename
n = nonogram.Nonogram('example.png')
#width, height, threshold, output filename
n.convert(32, 32, 550, "example")
```

* Input example

<img src="example.png" width="200" height="200" />

<img src="yeong.jpg" width="200" height="200" />


* Output example

<img src="example_answer.png" width="400" height="400" />

<img src="yeong_answer.png" width="400" height="400" />
