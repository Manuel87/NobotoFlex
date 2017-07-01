from designSpaceDocument import DesignSpaceDocument, SourceDescriptor, InstanceDescriptor, AxisDescriptor

import os
import sys

sys.dont_write_bytecode = True # prevents writing .pyc files


def init(ThisFileName):
	DesignSpaceSpec = __import__(ThisFileName)
	#import DesignSpaceSpec

	DesignSpaceSpec.init()

	# THIS REASSIGNING IS STUPID :(
	#--------------------------------
	familyName = DesignSpaceSpec.familyName
	path_ufos = DesignSpaceSpec.path_ufos
	familyName = DesignSpaceSpec.familyName
	axes = DesignSpaceSpec.axes
	defaultLocation = DesignSpaceSpec.defaultLocation
	sources = DesignSpaceSpec.sources
	instances = DesignSpaceSpec.instances
	designSpacePath = DesignSpaceSpec.designSpacePath
	#--------------------------------------
	# The solution might be somewhere here :
	#	https://stackoverflow.com/questions/13034496/using-global-variables-between-files
	# or here:
	#	https://stackoverflow.com/questions/2349991/python-how-to-import-other-python-files


	#global path_ufos, familyName, axes, defaultLocation, sources, instances


	try:
		if designSpacePath:
			designSpacePath = designSpacePath
		else:
			designSpacePath = familyName + ".designspace"
	except:
		designSpacePath = familyName + ".designspace"

	# Axes - Fill up with default Settings



	def get_min_max__fromsource(axis_name, min_max):
		axis_value = "nothing applied"

		for name in sources:
			if min_max in name:
				if axis_name in name:
					if axis_name[0:6] in name[0:6]:
						axis_value = sources[name][axis_name]

		if axis_value == "nothing applied":
			axis_value = defaultLocation[axis_name]

		return axis_value






	# basic setup to generate a distinct tag ID
	tags_all = []
	tag_id_array = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
	i = 0


	for elem in axes:
		id = next(iter(elem))
		axis = elem[id]

		axis["name"] = id #axis["labelName_en"].lower().replace(" ", "") # strip off spaces and make lowercase

		axis["default"] = defaultLocation[axis["name"]] # get defaults, only one axis is allowed to differ per master


		try:
			if axis["labelName_en"]:
				axis["labelNames"] = {"en": axis["labelName_en"]}
				pass
		except:
			axis["labelNames"] = {"en": id.replace("_", " ").title()}


		# Default Tags
		if id=="Weight":
			axis["tag"] = "wght"
		if id=="width":
			axis["tag"] = "wdth"
		if id=="optical_size":
			axis["tag"] = "opsz"

		# Generate Custom Tags
		try:
			if axis["tag"]:
				pass
		except:
			axis["tag"] = axis["name"][0:4].upper()

			# check if tag already exists and otherwise swap last letter
			if axis["tag"] in tags_all:
				if axis["tag"][3] == tag_id_array[i]: #if by chance is the same letter
					i = i + 1
				axis["tag"] = axis["tag"][0:3] + tag_id_array[i] #excluding 4th letter
				# for the next ones:
				i = i + 1
				if i >= len(tag_id_array):
					i = 0

		tags_all.append(axis["tag"])

		try:
			if axis["map"]:
				pass
		except:
			axis["map"] = []

		try:
			if axis["max"]:
				if axis["max"] == "default":
					axis["max"] = defaultLocation[axis["name"]]
				if axis["max"] == "source":
					axis["max"] = get_min_max__fromsource(id,"max")
				pass
		except:
			axis["max"] = get_min_max__fromsource(id,"max")
			#axis["max"] = defaultLocation[axis["name"]]

		try:
			if axis["min"]:
				if axis["min"] == "default":
					axis["min"] = defaultLocation[axis["name"]]
				if axis["min"] == "source":
					axis["min"] = get_min_max__fromsource(id,"min")
				pass
		except:
			axis["min"] = get_min_max__fromsource(id,"min")
			#axis["min"] = defaultLocation[axis["name"]]



	# Sources - Fill up with default settings
	"""
	for id in sources:
		source = sources[id]
		name = id
		source["styleName"] = name
		source["location"] = source

		source["path"] = path_ufos
		source["name"] = familyName + "-" + id + ".ufo"

		source["familyName"] = familyName
		source["copyInfo"] = False
		if source["location"] == defaultLocation:
			source["copyInfo"] = True

		if "max" in id:
			source_axis = id.split("-")[0]
			sources[id] = defaultLocation[source_axis]
			print name
			print sources[id]
	"""


	#instances = [
	#	dict(location=dict(Weight=1), styleName="InstanceName", familyName=familyName),
	#]

	#for source in sources:
	#	instances.append(dict(location=source["location"], styleName=source["styleName"], familyName=source["familyName"]))

	###

	doc = DesignSpaceDocument()

	#"Weight-max": {"Weight": 	322 },
	for name in sources:


		location = sources[name]

		s = SourceDescriptor()
		s.name = familyName + "-" + name + ".ufo" #source["name"]
		s.path = path_ufos + s.name #source["path"] + s.name
		s.copyInfo = False
		if location == defaultLocation:
			s.copyInfo = True #s.copyInfo = source["copyInfo"]


		s.location = location #source["location"]
		s.familyName = familyName #source["familyName"]
		s.styleName = name #familyName# source["styleName"]
		doc.addSource(s)

	for elem in instances:
		id = next(iter(elem))
		instance = elem[id]
		i = InstanceDescriptor()
		i.location = instance #instance["location"]
		i.familyName = familyName #instance["familyName"]
		i.styleName = id
		doc.addInstance(i)

	for elem in axes:
		id = next(iter(elem))
		axis = elem[id]

		# Generate axes if they are not there
		axis_max_value = False
		axis_min_value = False
		"""

		for name in sources:
			if "max" in name:
				axis_name = name.split("-")[0]
				print axis_name
				axis_max_value = sources[name][axis_name]
				print axis_max_value
			if "min" in name:
				axis_name = name.split("-")[0]
				print axis_name
				axis_min_value = sources[name][axis_name]
				print axis_min_value
		"""

		a = AxisDescriptor()

		if axis_max_value:
			a.maximum = axis_max_value
		else:
			a.maximum = axis["max"]

		if axis_min_value:
			a.minimum = axis_min_value
		else:
			a.minimum = axis["min"]

		a.default = axis["default"]
		a.name = axis["name"]
		a.tag = axis["tag"]
		for languageCode, labelName in axis["labelNames"].items():
			a.labelNames[languageCode] = labelName
		a.map = axis["map"]
		doc.addAxis(a)

	#doc.checkAxes()

	#doc.checkDefault()

	doc.write(designSpacePath)

	print familyName + ".designspace saved"





