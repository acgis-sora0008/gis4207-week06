import sys
import os


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

    in_fc = arcpy.ListFeatureClasses("", "", in_workspace)
    print (in_fc)
    clip_fc = arcpy.ListFeatureClasses("", "", clip_workspace)
    print (clip_fc)
    
    for in_feat in in_fc:
        for clip_feat in clip_fc:
            out_fc_name = f"{os.path.splitext(clip_feat)[0]}_{os.path.splitext(in_feat)[0]}.shp"
            out_fc = os.path.join(output_workspace, out_fc_name)
            arcpy.Clip_analysis(in_feat, clip_feat, out_fc)
            print (f'{out_fc} done')


if __name__ == "__main__":
    main()
