import sys
import os





def main():
    if len(sys.argv) !=4:
        print('Usage:  batch_clipper.py <InWorkspace> <ClipWorkspace> <OutputWorkspace>')
        sys.exit()
    
    in_workspace = sys.argv[1]
    clip_workspace = sys.argv[2]
    output_workspace = sys.argv[3]

    if not os.path.exists(in_workspace):
        print(f"{in_workspace} does not exist.")
        sys.exit()

    if not os.path.exists(clip_workspace):
        print(f"{clip_workspace} does not exist.")
        sys.exit()

    if not os.path.exists(output_workspace):
        print(f"{output_workspace} does not exist.")
        sys.exit()

    import arcpy
    from arcpy import env

    env.workspace = in_workspace
    env.overwriteOutput = True

    in_fc = arcpy.ListFeatureClasses("","",in_workspace)
    clip_fc = arcpy.ListFeatureClasses("","",clip_workspace)



    #if clip_Feat not exist (WS)

    # if out_feat not esist  (WS)

    batch_clipper(in_fc,clip_fc,output_workspace)
    print ('not done')












def batch_clipper(in_features, clip_features, out_feature_class):
    for in_feat in in_features:
        for clip_feat in clip_features:
            out_fc_name = "{}_{}.shp".format(os.path.splitext(clip_feat)[0], os.path.splitext(in_feat)[0])
            out_fc = os.path.join(out_feature_class,out_fc_name)
            arcpy.Clip_analysis(in_feat, clip_feat, out_fc)



if __name__ == "__main__":
    main()
