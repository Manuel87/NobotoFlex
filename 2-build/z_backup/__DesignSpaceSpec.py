
def init():
	global path_ufos, familyName, axes, defaultLocation, sources, instances

	path_ufos = "master_ufo/"
	familyName = "RobotoFlex"

	#designSpacePath = familyName + ".designspace" # This is Optional

	axes = [
		{"Scale" : 				{ 	"min": "source", 	"max":	"source", "labelName_en": "Scale (slightly off)" }},
		{"Baseline_Shift" : 	{ 	"min": "source", 	"max":	"source" }},
		{"Optical_Lineheight" : { 	"min": "source", 	"max":	"source" }},
		{"Weight": { 				"min": "source",	"max":	"source" }},  # registered
		{"Height" : { 				"min": "source", 	"max":	"default"}},
		{"Caps_Height" : { 			"min": "source", 	"max":	"default", "labelName_en": "> Caps Height"  }},
		{"Ascenders_Height" : { 	"min": "source", 	"max":	"source", "labelName_en": "> Ascenders Height" }},
		{"Diacritics_Distance" : { 	"min": "source", 	"max":	"source", "labelName_en": "> Diacritics Distance" }},
		{"Spacing" : 			{ 	"min": "source", 	"max":	"source" }},
		#{"Monospace" : 			{ 	"min": "source", 	"max":	"source" }},
		{"MonoFaux" : 			{ 	"min": "source", 	"max":	"source" }},
		{"Curvature" : 			{ 	"min": "source", 	"max":	"source" }},
		{"n_Width" : 			{ 	"min": "source", 	"max":	"source", "labelName_en": "(should be hidden)" }}
	]

	defaultLocation = {
		"Weight" : 			54, #185,#54,
		"Height": 			456,
		"Caps_Height": 		456,
		"Ascenders_Height": 456,
		"Diacritics_Distance": 	0,
		"Baseline_Shift": 	500, #at 0
		"Spacing": 			100,
		#"Monospace": 		0,
		"MonoFaux": 		0,
		"Curvature": 		0,
		"n_Width":			782,
		"Scale":				100,
		"Optical_Lineheight": 20
	}

	sources = {
		"Default": defaultLocation,

		#"Weight-min": {"Weight": 	54 },
		"Weight-max": {"Weight": 	322 },

		"Height-min": {"Height":  	 165 },

		"Caps_Height-min": {"Caps_Height": 0 },

		"Ascenders_Height-max": {"Ascenders_Height": 1000 },

		"Diacritics_Distance-max": {"Diacritics_Distance": 100 },

		"Baseline_Shift-min": { "Baseline_Shift": 0},
		"Baseline_Shift-max": { "Baseline_Shift": 1000},

		"Spacing-min": { "Spacing": 0},
		"Spacing-max": { "Spacing": 200},

	#	"Monospace-max": { "Monospace": 100},

		"MonoFaux-max": { "MonoFaux": 100},

		"Curvature-max": { "Curvature": 100},

		"n_Width-max": { "n_Width": 882},

		"Scale-min": { "Scale": 50},
		"Scale-max": { "Scale": 200},

		"Optical_Lineheight-min": { "Optical_Lineheight": 0},
		"Optical_Lineheight-max": { "Optical_Lineheight": 100}



	}

	instances = [
		{"Light" : {
			"Weight" : 			54
		}},
		{"Regular" : {
			"Weight" : 			180,
			"Scale":			100
		}},
		{"Bold" : {
			"Weight" : 			322,
			"Height": 			456,
			"Caps_Height": 		456,
			"Ascenders_Height": 456,
			"Diacritics_Distance": 	0
		}}
	]

	#------------------------



# Execution / Calling the writeDesignSpace.py script in the lib folder

import os, sys
sys.dont_write_bytecode = True # prevents writing .pyc files

scriptpath = "script_lib_custom/"
# Add the directory containing your module to the Python path (wants absolute paths)
sys.path.append(os.path.abspath(scriptpath))
# Do the import
import writeDesignSpace


# Execute // No Clue why it gets executed twice

ThisFileName = __file__.split("/")[-1].split(".")[0]
writeDesignSpace.init(ThisFileName)


