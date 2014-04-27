Periodogram
===========

Summary
-------

This is a simple python library for getting power spectra right. It is based on
the report "Spectrum and spectral density estimation by the Discrete Fourier
transform (DFT), including a comprehensive list of window functions and some
new at-top windows" by Gerhard Heinzel, Albrecht Rüdiger and Roland Schilling.
The report can be obtained at http://edoc.mpg.de/395068.

It supports the built-in numpy FFT functions as well as pyFFTW. Take a look at
the paper mentioned above for the right window function. The library is tested
with Python 2.7 and Python 3.3.

License
-------

::

  Copyright (c) 2014 Roman Thiele <r.thiele@tum.de>

  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to deal
  in the Software without restriction, including without limitation the rights
  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
  copies of the Software, and to permit persons to whom the Software is
  furnished to do so, subject to the following conditions:

  The above copyright notice and this permission notice shall be included in
  all copies or substantial portions of the Software.

  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
  THE SOFTWARE.
