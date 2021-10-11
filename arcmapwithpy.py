#Assigning variables(replace path with the actual path on your computer)
count = arcpy.management.GetCount ("C:/PythonStart/ambulances.shp")

print (count)

count = arcpy.management.GetCount("ambulances")

print(count)


#Point to the feature class on disk by specifying the full path.
count = arcpy.management.GetCount("C:/PythonStart/ambulances.shp")

print(count)

#Setting the workspace

arcpy.env.workspace = "C:/PythonStart"

count = arcpy.management.GetCount("ambulances.shp")

print(count)

#Create a list of shapefiles in the workspace and run the Get Count tool on every element of this list

fc_list = arcpy.ListFeatureClasses()

print(fc_list)

The result is:

['ambulances.shp', 'boundary.shp', 'fire_stations.shp', 'fire_zones.shp', 'voting_divisions.shp', 'voting_sites.shp']

#create a for loop to iterate over the elements in the list.
for fc in fc_list:

count = arcpy.management.GetCount(fc)

#The result prints the number of features for each of the shapefiles in the workspaces.
print(count)




