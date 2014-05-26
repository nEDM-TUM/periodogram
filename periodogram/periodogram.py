#!/usr/bin/python
# coding: utf-8

import numpy
import numpy.fft
import windows

try:
    import pyfftw.interfaces.numpy_fft
    _fft = pyfftw.interfaces.numpy_fft.rfft
    _fft_name = 'pyfftw'
except ImportError:
    _fft = numpy.fft.rfft
    _fft_name = 'numpy'

_fftfreq = numpy.fft.rfftfreq

class Periodogram:
    '''
    Class for calculating periodograms using Welch's method.

    The implementation follows the method described in
    G. Heinzel, A. Rüdiger and R. Schilling – "Spectrum and spectral
    density estimation by the Discrete Fourier Transform (DFT), including
    a comprehensive list of window functions and some new flat-top windows."

    see: http://edoc.mpg.de/395068
    '''
    named_windows = {
            'rect': numpy.ones,
            'HFT116D': windows.HFT116D,
            'FTSRS': windows.FTSRS,
            'hanning': numpy.hanning,
            }

    _ps = None

    def __init__(self, data, samplerate, N, window='hanning', overlap=0.5):
        assert(overlap >= 0)
        assert(overlap < 1)
        assert(N > 0)
        assert(N < len(data))

        self.data = data
        self.samplerate = samplerate
        self.N = N
        self.overlap = overlap

        # calculate window
        if window in self.named_windows:
            window = self.named_windows[window](N)
        elif callable(window):
            window = window(N)
        else:
            assert(len(window) == N or len(window) == 1)

        self.window = window

        # calculate window parameters
        S1 = numpy.sum(window)
        S2 = numpy.sum(window*window)
        self.NENBW = N*S2/(S1*S1)
        self.ENBW = samplerate*S2/(S1*S1)
        self.S1 = S1

    def ps(self):
        if self._ps == None:
            # calculate fft frequencies
            f = _fftfreq(self.N, 1./self.samplerate)

            # calculate number of averages
            dt = int(self.N*(1-self.overlap))
            number_of_averages = (len(self.data)-self.N)//dt

            # cancel offset
            self.data -= numpy.mean(self.data, dtype=self.data.dtype)

            # prepare output array
            ps = numpy.zeros_like(f)

            for i in range(number_of_averages):
                # sum FFTs
                t_start = i*dt
                fft = _fft(self.data[t_start:t_start+self.N]*self.window)
                ps += abs(fft)**2

            # calculate average
            ps = 2.*ps / (self.S1*self.S1*number_of_averages)

            # Save power spectrum
            self._ps = ps
            self.f = f

            # save important parameters
            self.number_of_averages = number_of_averages
            self.fres = f[1] - f[0]

        return self._ps

    def get_parameters(self):
        self.ps()
        return {
                'number_of_averages': self.number_of_averages,
                'ENBW': self.ENBW,
                'NENBW': self.NENBW,
                'fres': self.fres,
                'fmin': self.f[0],
                'fmax': self.f[-1],
                'N': self.N
                }

    def psd(self, *a, **aa):
        return self.ps(*a, **aa)/self.ENBW

    def ls(self, *a, **aa):
        return numpy.sqrt(self.ps(*a, **aa))

    def lsd(self, *a, **aa):
        return numpy.sqrt(self.psd(*a, **aa))

def __run():
    import argparse
    import cPickle

    p = argparse.ArgumentParser(
            description="Save pickeled periodograms")
    p.add_argument('file', nargs='+',
            help="input files")
    p.add_argument('samplerate', type=float,
            help="samplerate of input data")
    p.add_argument('N', type=int,
            help="length of samples that are averaged")
    p.add_argument('--overlap', '-o', type=float,
            help="overlap", default=0.5)
    p.add_argument('--window', '-w', default='hanning',
            help="window function")

    args = p.parse_args()

    for fn in args.file:
        d = numpy.load(fn)
        p = Periodogram(d, args.samplerate, args.N, args.window,
                args.overlap)
        p.ps()

        with open("fft_%s.pickle" % fn, 'wb') as outfile:
            cPickle.dump(p, outfile, 2)

if __name__ == '__main__':
    __run()
