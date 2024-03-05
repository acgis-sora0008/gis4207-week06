import os
import sys

def main():
    if len(sys.argv) != 4:
        print("Usage: python script.py <input_folder> <output_gdb> <output_feature_dataset>")
        sys.exit(1)

    input_folder = sys.argv[1]
    output_gdb = sys.argv[2]
    output_feature_dataset = sys.argv[3]

    if not os.path.exists(input_folder):
        print(f"{input_folder} does not exist.")
        sys.exit()

    import arcpy

    copy_feature_classes(input_folder, output_gdb, output_feature_dataset)


def create_gdb(gdb_path):
    import arcpy

    if not arcpy.Exists(gdb_path):
        arcpy.management.CreateFileGDB(os.path.dirname(gdb_path), os.path.basename(gdb_path))
    else:
        print(f"Geodatabase '{gdb_path}' already exists.")

def copy_feature_classes(input_folder, output_gdb, output_feature_dataset):
    import arcpy

    create_gdb(output_gdb)
    arcpy.env.overwriteOutput = True

    feature_dataset_path = os.path.join(output_gdb, output_feature_dataset)
    arcpy.env.workspace = feature_dataset_path

    # Walk through input folder and copy feature classes
    for root, dirs, files in os.walk(input_folder):
        for dir in dirs:
            gdb_path = os.path.join(root, dir)
            arcpy.env.workspace = gdb_path

            feature_classes = arcpy.ListFeatureClasses()

            for fc in feature_classes:
                input_fc = os.path.join(gdb_path, fc)
                output_fc = os.path.join(feature_dataset_path, fc)
                arcpy.management.CopyFeatures(input_fc, output_fc)
                print(f"Copying {fc} from {gdb_path} to {output_gdb}")

    print("Feature classes copied successfully.")

if __name__ == "__main__":
    main()