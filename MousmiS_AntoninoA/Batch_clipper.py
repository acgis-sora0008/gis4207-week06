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
    for in_fc in in_fcs:
        in_feat_list = []
        in_feat_list.append(os.path.abspath(os.path.join(in_workspace, in_fc)))
        print(in_feat_list)
        # print(in_fc)

    # sys.exit()
    clip_fc = arcpy.ListFeatureClasses()
    # print (clip_fc)
    
    for in_feat in in_feat_list:
        for clip_feat in in_feat_list:
            out_fc_name = f"{os.path.splitext(clip_feat)[0]}_{os.path.splitext(in_feat)[0]}.shp"
            out_fc = os.path.abspath(os.path.join(output_workspace, os.path.basename(out_fc_name)))
            arcpy.Clip_analysis(in_feat, clip_feat, out_fc)
            print(in_feat)
            # print("-")
            print(clip_feat)
            # print("-")
            print(out_fc)
            # print("-")
    
    arcpy.env.overwriteOutput = True         


if __name__ == "__main__":
    main()
