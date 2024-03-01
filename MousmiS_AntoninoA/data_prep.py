
import os
import sys

class Toolbox:
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = "toolbox"

        # List of tool classes associated with this toolbox
        self.tools = [Tool]

class Tool:
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Tool"
        self.description = "The toolbox will transfer files from GDbs to FDs in UTMZone10"

    def getParameterInfo(self):
        """Define the tool parameters."""
        params = None
        return params

    def isLicensed(self):
        """Set whether the tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter. This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        if len(sys.argv) != 4:
            print('Usage:  data_prep.py <in_gdbs_base_folder> <out_gdb> <out_feature_dataset>')
            return

        in_gdbs_base_folder = sys.argv[1]
        out_gdb = sys.argv[2]
        out_feature_dataset = sys.argv[3]

        if not os.path.exists(in_gdbs_base_folder):
            print(f"{in_gdbs_base_folder} does not exist.")
            return

        # Delayed import for arcpy
        import arcpy
        from arcpy import env

        # Set the workspace using arcpy
        arcpy.env.workspace = None
        arcpy.env.workspace = in_gdbs_base_folder
        arcpy.env.overwriteOutput = True

        out_folder_path = os.path.dirname(out_gdb)
        out_gdb_name = os.path.basename(out_gdb)

        # List of specific geodatabases
        geodatabases = [
            r"..\..\..\..\data\surrey\elementary_school_catchments.gdb",
            r"..\..\..\..\data\surrey\parks.gdb",
            r"..\..\..\..\data\surrey\road_centrelines.gdb",
            r"..\..\..\..\data\surrey\schools.gdb",
            r"..\..\..\..\data\surrey\surrey_city_boundary.gdb"
        ]

        # Loop over the specified geodatabases
        for gdb in geodatabases:
            feature_classes = arcpy.ListFeatureClasses("*", "", gdb)
            
            if not feature_classes:
                print(f"No feature classes found in the GDB: {gdb}")
                continue
            
            first_feature_class = feature_classes[0]
            spatial_reference = arcpy.Describe(os.path.join(gdb, first_feature_class)).spatialReference
            out_gdb_path = os.path.join(out_gdb, out_feature_dataset)
            arcpy.management.CreateFileGDB(out_folder_path=os.path.dirname(out_gdb_path), out_name=os.path.basename(out_gdb_path))
            arcpy.management.CreateFeatureDataset(out_dataset_path=out_gdb_path, out_name=out_feature_dataset, spatial_reference=spatial_reference)

            for feature_class in feature_classes:
                arcpy.conversion.FeatureClassToFeatureClass(in_features=os.path.join(gdb, feature_class),
                                                            out_path=os.path.join(out_gdb_path, out_feature_dataset),
                                                            out_name=feature_class)
            
            print(f"Data preparation completed in {gdb}")

        print("Data preparation completed successfully!")
        return

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return
