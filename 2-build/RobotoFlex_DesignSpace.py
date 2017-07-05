
def init():
	global path_ufos, familyName, axes, defaultLocation, sources, instances, designSpacePath

	path_ufos = "master_ufo/"
	familyName = "RobotoFlex"

	designSpacePath = False
	#designSpacePath = familyName + ".designspace" # This is Optional / otherwise saved next to this file

	axes = [
		{"Scale" : 				{ 	"min": "source", 	"max":	"source", "labelName_en": "Scale (alpha)" }},
		{"Baseline_Shift" : 	{ 	"min": "source", 	"max":	"source", "labelName_en": "Baseline Shift (alpha)" }},
		{"Spacing" : 			{ 	"min": "source", 	"max":	"source" }},

		{"Weight": { 				"min": "source",	"max":	"source" }},  # registered
		{"Optical_Lineheight" : { 	"min": "source", 	"max":	"source", "labelName_en": "Optical Line Height"  }},
		{"Height" : { 				"min": "source", 	"max":	"default"}},
		{"Caps_Initial_Size" : { 	"min": "source", 	"max":	"source", "labelName_en": "> Caps, single"  }},
		{"Caps_Size" : { 			"min": "source", 	"max":	"source", "labelName_en": "> Caps, many"  }},
		{"Caps_smcp_Size" : { 		"min": "source", 	"max":	"source", "labelName_en": "> Smcp"  }},
		{"Ascenders_Height" : { 	"min": "source", 	"max":	"source", "labelName_en": "> Ascenders" }},
		{"Descenders_Height" : { 	"min": "source", 	"max":	"source", "labelName_en": "> Descenders" }},
		{"Diacritics_Distance" : { 	"min": "source", 	"max":	"source", "labelName_en": "> Diacritics Distance" }},
		# no clue why the Monospace is not working anymore
		#{"Monospace" : 			{ 	"min": "source", 	"max":	"source" }},
		{"MonoFaux" : 			{ 	"min": "source", 	"max":	"source" }},
		{"Curvature" : 			{ 	"min": "source", 	"max":	"source" }},
	#	{"n_Width" : 			{ 	"min": "source", 	"max":	"source", "labelName_en": "(should be hidden)" }}
	]

	defaultLocation = {
		# NOTE:
		# min/max +1/-1 values
		# need to differ from min/max otherwise it will not build / fonttools error


		"Scale":			100,
		"Baseline_Shift": 	500, #at 0
		"Spacing": 			100,


		"Weight" : 			185,
		"Height": 			456,
		# "Caps_Size": 		400,
		# "Caps_Initial_Size": 456,
		# "Caps_smcp_Size": 	165,


		"Caps_Size": 		400,
		"Caps_Initial_Size": 455, #max -1
		"Caps_smcp_Size": 	166, #min + 1


		"Ascenders_Height": 456,
		"Descenders_Height": 456,
		"Diacritics_Distance": 	0,
		#"Monospace": 		0,
		"MonoFaux": 		0,
		"Curvature": 		0,
	#	"n_Width":			782,
		"Optical_Lineheight": 20
	}

	sources = {
		"Default": defaultLocation,

		"Scale-min": { 				"Scale": 			50},
		"Scale-max": { 				"Scale": 			200},

		"Baseline_Shift-min": { 	"Baseline_Shift": 	0},
		"Baseline_Shift-max": { 	"Baseline_Shift": 	1000},

		"Spacing-min": { 			"Spacing": 			0},
		"Spacing-max": { 			"Spacing": 			200},


		"Weight-min": {				"Weight": 			54 },
		"Weight-max": {				"Weight": 			322 },

		"Height-min": {				"Height":  	 		165 },

		"Caps_Size-min": {			"Caps_Size": 		165 },
		"Caps_Size-max": {			"Caps_Size": 		656 },

		"Caps_Initial_Size-min": {	"Caps_Initial_Size": 165 },
		"Caps_Initial_Size-max": {	"Caps_Initial_Size": 656 },

		"Caps_smcp_Size-min": {		"Caps_smcp_Size": 	165 },
		"Caps_smcp_Size-max": {		"Caps_smcp_Size": 	656 },

		"Ascenders_Height-max": {	"Ascenders_Height": 1000 },

		"Descenders_Height-max": {	"Descenders_Height": 1000 },

		"Diacritics_Distance-max": {"Diacritics_Distance": 100 },


	#	"Monospace-max": { "Monospace": 100},

		"MonoFaux-max": { 			"MonoFaux":			100},

		"Curvature-max": { 			"Curvature":		100},

	#	"n_Width-max": { 			"n_Width": 			882},


		"Optical_Lineheight-min": { "Optical_Lineheight": 0},
		"Optical_Lineheight-max": { "Optical_Lineheight": 100}

	}

	instances = [
		{"Light" : {
			"Weight" : 			54,
			"Caps_smcp_Size": 	165,
			"Spacing" : 		100
		}},
		{"Regular" : {
			"Weight" : 			180,
			"Scale":			100,
			"Caps_smcp_Size": 	165,
			"Spacing" : 		100
		}},
		{"Bold" : {
			"Weight" : 			322,
			"Height": 			456,
			"Caps_Size": 		456,
			"Ascenders_Height": 456,
			"Diacritics_Distance": 	0,
			"Caps_smcp_Size": 	165,
			"Spacing" : 		100
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


