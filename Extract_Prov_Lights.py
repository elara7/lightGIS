import gdal
import numpy as np
import os
Basedir="D:\light_guo\Light_Guo\polygon\Province_rename"
Rasterfilepath='D:\light_guo\Light_Guo\pic\F182013.v4c_web.stable_lights.avg_vis.tif'
for file in os.listdir(Basedir):
     if file.endswith('.shp'):
         shapefile=file
         shpfilepath=os.path.join(Basedir,shapefile)
         Outputraster='F182013.v4c_web.stable_lights.avg_vis_'+file.split('.shp')[0]+'.tif'
         OutputrasterPATH=os.path.join('D:\light_guo\Light_Guo\output\Province',Outputraster)
         #cmd="gdalwarp -dstnodata 254 -of GTiff -cutline "+ shpfilepath+ "  -crop_to_cutline -overwrite "+Rasterfilepath+" "+OutputrasterPATH
         cmd="gdalwarp -of GTiff -cutline "+ shpfilepath+ "  -crop_to_cutline -overwrite "+Rasterfilepath+" "+OutputrasterPATH
         print (cmd)
         
         os.system(cmd)
