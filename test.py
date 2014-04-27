from pylab import *
from periodogram import Periodogram, _fft_name

TWOPI=6.28318530717959

def test_data(fs=10000., f1=1234., amp1=2.82842712474619, f2=2500.2157, amp2=1., ulsb=1e-3, N=1000000):
    t = arange(N) / float(fs)
    u = amp1*sin(TWOPI*f1*t)+amp2*sin(TWOPI*f2*t)
    ur = floor(u/ulsb + 0.5)*ulsb
    return ur

if __name__ == '__main__':
    N = 3328
    d = test_data()
    p = Periodogram(d, 10000., N, window='HFT116D', overlap=0.5)

    print("FFT is " + _fft_name)
    print("Params: " + repr(p.get_parameters()))
    #plot(f, sqrt(ps_to_psd(ps, params_dict)))
    figure()
    title("linear spectrum")
    ylabel("Vrms")
    plot(p.f, p.ls())
    figure()
    title("linear spectral density")
    ylabel("Vrms/sqrt(Hz)")
    plot(p.f, p.lsd())
    yscale('log')
    show()
