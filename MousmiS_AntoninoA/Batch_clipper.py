import sys
import os
# import arcpy

# specifying the absolute path
# in_path = "acgis\gis4207_prog\data\BatchClipData\TargetData\WinterHabitat.shp"
# clip_path = "acgis\gis4207_prog\data\BatchClipData\TargetData\TroutCatchments.shp"
# out_path = "acgis\gis4207_prog\data\BatchClipData\TargetData\WinterHabitat.shp"


def main():
    if len(sys.argv) != 4:
        print('Usage: batch_clipper.py <InWorkspace> <ClipWorkspace> <OutputWorkspace>')
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

    in_fcs = arcpy.ListFeatureClasses()
    # in_feat_list = []
    in_feat_list = [os.path.abspath(os.path.join(in_workspace, in_fc)) for in_fc in in_fcs]
    
    env.workspace = clip_workspace
    clip_fcs = arcpy.ListFeatureClasses()
    clip_feat_list = [os.path.abspath(os.path.join(clip_workspace, clip_fc)) for clip_fc in clip_fcs]
    
    
    for in_fc in in_fcs:
        in_feat_list.append(os.path.abspath(os.path.join(in_workspace, in_fc)))
        # print(in_feat_list)
        # print(in_fc)

    # sys.exit()
    clip_fcs = arcpy.ListFeatureClasses()
    in_clip_list = []
    for clip_fc in clip_fcs:
        in_clip_list.append(os.path.abspath(os.path.join(in_workspace, clip_fc)))
        

    # print (clip_fc)
    
    
    for in_feats in in_feat_list:
        for clip_feats in clip_feat_list:
            out_fc_name = f"{os.path.splitext(os.path.basename(clip_feats))[0]}_{os.path.splitext(os.path.basename(in_feats))[0]}.shp"
            out_fcs = os.path.abspath(os.path.join(output_workspace, out_fc_name))
            
            
            
            arcpy.Clip_analysis(in_feats, clip_feats, out_fcs)
            
            print(in_feats)
            print(clip_feats)
            print(out_fcs)
            print("-")
    
    arcpy.env.overwriteOutput = True         


if __name__ == "__main__":
    main()
