import numpy           as     np
import pylab           as     pl
import astropy.io.fits as     fits

from   astropy.table   import Table


dat      = Table(fits.open('tractor-0011m377.fits')[1].data)

type     = dat['type']
types    = set(type)

rmag     = 22.5 - 2.5 * np.log10(np.array(dat['flux_r'].quantity)) 
rfibmag  = 22.5 - 2.5 * np.log10(np.array(dat['fiberflux_r'].quantity))  

for type in types:
  isin   = dat['type'] == type
  pl.plot(rmag[isin], rfibmag[isin], '.', markersize=1)

pl.xlim(21., 25.5)
pl.ylim(21., 25.5)
pl.show()
