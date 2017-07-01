scriptpath = "../../script_lib_custom/"

def init():
	global path_ufos, familyName, axes, defaultLocation, sources, instances, designSpacePath

	path_ufos = "../../master_ufo/"
	familyName = "RobotoFlex"

	designSpacePath = False
	#designSpacePath = familyName + ".designspace" # This is Optional / otherwise saved next to this file

	axes = [
		{"Spacing" : 			{ 	"min": "source", 	"max":	"source" }},
	]

	defaultLocation = {
		"Spacing": 			100,
	}

	sources = {
		"Default": defaultLocation,

		"Spacing-min": { 			"Spacing": 			0},
		"Spacing-max": { 			"Spacing": 			200}

	}

	instances = [
		{"Spacing-min" : {
			"Spacing" : 		0
		}},
		{"Regular" : {
			"Spacing" : 		100
		}},
		{"Spacing-max" : {
			"Spacing" : 		200
		}}
	]

	#------------------------



# Execution / Calling the writeDesignSpace.py script in the lib folder

import os, sys
sys.dont_write_bytecode = True # prevents writing .pyc files



# Add the directory containing your module to the Python path (wants absolute paths)
sys.path.append(os.path.abspath(scriptpath))
# Do the import
import writeDesignSpace


# Execute // No Clue why it gets executed twice

ThisFileName = __file__.split("/")[-1].split(".")[0]
writeDesignSpace.init(ThisFileName)


