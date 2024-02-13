import sys
import os
import arcpy
from arcpy import env



def main():
    # if name in_feat not exist (WS)


    #if clip_Feat not exist (WS)

    # if out_feat not esist  (WS)

    import arcpy

    print ('not done')












def batch_clipper(in_features, clip_features, out_feature_class):
    for in_fc in in_features:
        for clip_fc in clip_features:
            out_fc_name = "{}_{}.shp".format(os.path.splitext(clip_fc)[0], os.path.splitext(in_fc)[0])
            out_fc = os.path.join(out_feature_class,out_fc_name)
            arcpy.Clip_analysis(in_fc, clip_fc, out_fc)
            arcpy.env.overwriteOutput = True


    
if __name__ == "__main__":
    main()