import  skimage
import  numpy              as  np
import  pylab              as  pl
import  matplotlib.pyplot  as  plt 
import  astropy.io.fits    as  fits

from    scipy                            import ndimage as ndi
from    skimage                          import feature
from    mpl_toolkits.axes_grid1.axes_rgb import RGBAxes                                                                                                             

from    skimage.filters                  import roberts


fig     = plt.figure() 
ax      = RGBAxes(fig, [0.1, 0.1, 0.8, 0.8])                                                                                                                         

dat     = fits.open('cutout_6.9276_22.0952.fits')[0].data

print(max)

r       = dat[2,:,:]                                                                                                                                              
g       = dat[1,:,:]                                                                                                                                              
b       = dat[0,:,:]                                                                                                                                              

g[:,:]  = 0.0
b[:,:]  = 0.0

ax.imshow_rgb(r, g, b)

pl.savefig('edges.pdf')

