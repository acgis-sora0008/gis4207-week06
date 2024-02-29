import sys
import os

def main():
    if len(sys.argv) != 4:
        print('Usage:  data_prep.py <in_gdbs_base_folder> <out_gdb> <out_feature_dataset>')
        sys.exit()

    in_gdbs_base_folder = sys.argv[1]
    out_gdb = sys.argv[2]
    out_feature_dataset = sys.argv[3]

    if not os.path.exists(in_gdbs_base_folder):
        print(f"{in_gdbs_base_folder} does not exist.")
        sys.exit()

    import arcpy
    from arcpy import env
    
    env.workspace = None
    env.workspace = in_gdbs_base_folder
    env.overwriteOutput = True

    out_folder_path = os.path.dirname(out_gdb)
    out_gdb_name = os.path.basename(out_gdb)

    gdbs = arcpy.ListWorkspaces("*", "FileGDB")

    if not gdbs:
        print("No File Geodatabases found in the specified base folder.")
        return
    
    first_gdb = gdbs[0]
    print (first_gdb)
    feature_classes = arcpy.ListFeatureClasses("*", "", first_gdb)
    print (feature_classes)

    if not feature_classes:
        print(f"No feature classes found in the GDB: {first_gdb}")
        return
    first_feature_class = feature_classes[0]
    spatial_reference = arcpy.Describe(os.path.join(first_gdb, first_feature_class)).spatialReference
    out_gdb_path = os.path.join(out_gdb, out_feature_dataset)
    arcpy.management.CreateFileGDB(out_folder_path=os.path.dirname(out_gdb_path), out_name=os.path.basename(out_gdb_path))
    arcpy.management.CreateFeatureDataset(out_dataset_path=out_gdb_path, out_name=out_feature_dataset, spatial_reference=spatial_reference)

    for gdb in gdbs:
        feature_classes = arcpy.ListFeatureClasses("*", "", gdb)
        
        for feature_class in feature_classes:
            arcpy.conversion.FeatureClassToFeatureClass(in_features=os.path.join(gdb, feature_class),
                                                        out_path=os.path.join(out_gdb_path, out_feature_dataset),
                                                        out_name=feature_class)
        
        print(f"Data preparation completed in {gdb}")

            





    print("Data preparation completed successfully!")





if __name__ == "__main__":
    main()


