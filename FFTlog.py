""" Python wrapper for FFTLog
    (c) Prisae
"""

import fftlog



class FFTLog(object):
    
    def __init__(self, logrmin=-4, logrmax=4,
                n=64, mu=0, q=0, kr=1, kropt=1):
        
        self.logrmin = logrmin     # Range of periodic interval
        self.logrmax = logrmax
        
        self.n  = n          # Number of points (Max 4096)
        self.mu = mu           # Order mu of Bessel function
        self.q  = q           # Bias exponent: q = 0 is unbiased
        self.kr = kr           # Sensible approximate choice of k_c r_c
        
        self.kropt = kropt  # Tell fhti to change kr to low-ringing value
                        # WARNING: kropt = 3 will fail, as interaction is not supported

        # Forward transform (changed from dir to tdir, as dir is a python fct)
        self.tdir = 1
        
        # Log-spacing of points
        dlogr = (logrmax - logrmin)/n
        dlnr  = dlogr*np.log(10.0)
        
        kr, wsave, ok = fftlog.fhti(self.n, self.mu, 
                                    dlnr, self.q, self.kr, self.kropt)
        print('fftlog.fhti: ok =', bool(ok), '; New kr = ', kr)