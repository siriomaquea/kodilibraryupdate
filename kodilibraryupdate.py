import time
import xbmc
xbmc.executebuiltin( "UpdateLibrary(Video)" )
time.sleep(60)
xbmc.executebuiltin( "CleanLibrary(Video)" )