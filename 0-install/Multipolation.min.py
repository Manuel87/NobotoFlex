

from Foundation import *
import GlyphsApp
import vanilla
import math
import os.path

import inspect
import copy

import json
from pprint import pprint
import copy

from random import randint
import ast  # string to list


Doc = Glyphs.currentDocument
Font = Glyphs.font  # frontmost font

jsonfilename = "_multipolation-spec.json"

LocalGlyphInterpolations = []
LocalGlyphInterpolations += [""]




def string_to_list(x):
	return ast.literal_eval(x)


def redefinelist(x):
	return string_to_list(str(x))


def map(value, inMin, inMax, outMin, outMax):

	leftSpan = inMax - inMin
	rightSpan = outMax - outMin


	valueScaled = float(value - inMin) / float(leftSpan)


	return outMin + (valueScaled * rightSpan)




def byteify(input):
	if isinstance(input, dict):
		return {byteify(key): byteify(value)
				for key, value in input.iteritems()}
	elif isinstance(input, list):
		return [byteify(element) for element in input]
	elif isinstance(input, unicode):
		return input.encode('utf-8')
	else:
		return input


def func(a, b, c):
	frame = inspect.currentframe()
	args, _, _, values = inspect.getargvalues(frame)

	for i in args:
		print "	%s = %s" % (i, values[i])
	return [(i, values[i]) for i in args]


def AddInstance(myname, myfilters=False):
	newInstance = GSInstance()
	newInstance.active = True  # Activate_New_Instances
	newInstance.name = myname  # prefix + "{0:.0f}".format( thisWeight )
	newInstance.weightValue = 1
	newInstance.widthValue = 1
	newInstance.isItalic = False
	newInstance.isBold = False


	if myfilters:
		AddCustomParameter(newInstance, myfilters)

	Glyphs.font.addInstance_(newInstance)


def AddCustomParameter(myInstance, myfilters=False):
	if myfilters:
		if myfilters[0]:

			tempArray = myfilters[0].split("::")

			myfilters_Count = len(myfilters)

			for k in range(myfilters_Count):
				tempArray = myfilters[k].split("::")

				cp = GSCustomParameter.alloc().init()
				cp = GSCustomParameter(tempArray[0], tempArray[1])
				myInstance.customParameters.append(cp)




def getGSObjectIndex(thisArray, name):
	k = 0
	for child in thisArray:
		if (name == child.name):
			return k
		k += 1


def sumSelDictValues(thisArray, selectionArray, childsvalue):
	sum = [0.0, 0.0]  # xy
	sum_string = ["", ""]

	for selection in selectionArray:
		for k in range(len(sum)):
			sum[k] += thisArray[selection][childsvalue][k]
			sum_string[k] += " + " + str(thisArray[selection][childsvalue][k])






	return sum




def convertmyList2Array(list):
	newarray = []
	for elementstr in list:

		newarray.append(elementstr)
	return newarray


def CheckIfValuesSequel(thisArray):
	for name in thisArray:
		sum += thisArray[selection][childsvalue]
	return sum


def getMasterNames(excludeStr):  # * #excludeStr="whatever"
	MasterNameArray = []
	excludeStr = [excludeStr]
	for k in range(len(Font.masters)):
		name = [byteify(Font.masters[k].name)]
		if (name != excludeStr):
			MasterNameArray += name
	return MasterNameArray


def getInstanceMasterValuesCalcOrder(data):
	MastersWithChilds = getMasterWithChildren(data)
	MastersWithoutChildsArray = getMasterWithOutChildren(data)

	OrderArrayBefore = convertmyList2Array(MastersWithChilds)
	OrderArrayBefore = list(reversed(OrderArrayBefore))
	OrderArrayBeforeStr = str(OrderArrayBefore)
	OrderAsArray = OrderArrayBefore

	k = 0
	NewOrderAsArray = OrderAsArray
	for MasterWithChildsName in MastersWithChilds:
		children = data["MasterSetupMapping"][MasterWithChildsName][2]

		for MasterWithChildsName2 in MastersWithChilds:

			if MasterWithChildsName2 in children:

				OrderAsArray = NewOrderAsArray

				firstIndex = OrderAsArray.index(MasterWithChildsName2)
				secondIndex = OrderAsArray.index(MasterWithChildsName)

				if (firstIndex > secondIndex):

					k += 1


					OrderAsArray.insert(
						firstIndex, OrderAsArray.pop(secondIndex))







					NewOrderAsArray = OrderAsArray








	return MastersWithoutChildsArray + OrderAsArray


def getMasterWithChildren(data):  # previous name: getMasterWithChildren
	MasterWithChildren = {}
	k = 0
	for mastername in data["MasterSetupMapping"]:
		if not mastername.startswith("_"):  # exclude comments, etc.






			if (len(data["MasterSetupMapping"][mastername]) > 2):  # only the ones with children
				children = data["MasterSetupMapping"][mastername][2]



				if (children == "All"):

					children = getMasterNames(mastername)
					data["MasterSetupMapping"][mastername][2] = children



				MasterWithChildren.update({mastername: k})  # k
				k += 1  # initial random order






	return MasterWithChildren


def getMasterWithOutChildren(data):  # previous name: getMasterWithChildren
	MasterWithOutChildrenArray = []
	k = 0
	for mastername in data["MasterSetupMapping"]:
		if not mastername.startswith("_"):  # exclude comments, etc.

			if (not len(data["MasterSetupMapping"][mastername]) > 2):
				MasterWithOutChildrenArray += [str(mastername)]

	return MasterWithOutChildrenArray





def convert2LocalInterpolation(data):




	base_setting = True
	try:
		_base_setting = data["InstancesSetup"]["_base_setting"]
	except:
		try:
			data["InstancesSetup"]["_base_setting"] = data["InstancesSetup"]["_fallback_values"]
		except:
			try:
				data["InstancesSetup"]["_base_setting"] = data["InstancesSetup"]["Default"]
			except:
				try:
					data["InstancesSetup"]["_base_setting"] = data["InstancesSetup"]["Regular"]
				except:
					base_setting = False



	if not ("#All" in data["InstancesSetup"]["_base_setting"]):
		tempdata = copy.deepcopy(data)
		del data["InstancesSetup"]["_base_setting"]
		data["InstancesSetup"]["_base_setting"] = {}
		data["InstancesSetup"]["_base_setting"]["#All"] = tempdata["InstancesSetup"]["_base_setting"]





	for instancename in data["InstancesSetup"]:

		forced_Setup_on_all_Groups = False

		for charGroupName in data["InstancesSetup"][instancename]:
			if charGroupName == "_All_Force":



				forced_Setup_on_all_Groups = tempdata["InstancesSetup"][instancename]["_All_Force"]
				forced_Setup_on_all_Groups = copy.deepcopy(forced_Setup_on_all_Groups)






		if not instancename.startswith("_"):






			if not ("#All" in data["InstancesSetup"][instancename]):

				tempdata = copy.deepcopy(data)
				del data["InstancesSetup"][instancename]
				data["InstancesSetup"][instancename] = {}

				data["InstancesSetup"][instancename]["#All"] = tempdata["InstancesSetup"][instancename]



			if base_setting:
				if not (instancename == "_base_setting"):
					tempdata = copy.deepcopy(data)
					del data["InstancesSetup"][instancename]["#All"]
					data["InstancesSetup"][instancename]["#All"] = {}

					data["InstancesSetup"][instancename]["#All"] = tempdata["InstancesSetup"]["_base_setting"]["#All"]

					for mastername in tempdata["InstancesSetup"][instancename]["#All"]:
						data["InstancesSetup"][instancename]["#All"][mastername] = tempdata["InstancesSetup"][instancename]["#All"][mastername]









			if base_setting:
				for charGroupName in data["InstancesSetup"]["_base_setting"]:
					if not (charGroupName == "#All"):

						tempdata = copy.deepcopy(data)
						try:
							del data["InstancesSetup"][instancename][charGroupName]
							charGroupName_does_exist = True
						except: #does not exist, assign directly
							charGroupName_does_exist = False
							pass
						data["InstancesSetup"][instancename][charGroupName] = {}
						data["InstancesSetup"][instancename][charGroupName] = tempdata["InstancesSetup"]["_base_setting"][charGroupName]



						if charGroupName_does_exist:
							for mastername in data["InstancesSetup"][instancename][charGroupName]:
								data["InstancesSetup"][instancename][charGroupName][mastername] = tempdata["InstancesSetup"][instancename][charGroupName][mastername]


						if forced_Setup_on_all_Groups:
							for mastername in forced_Setup_on_all_Groups:
								data["InstancesSetup"][instancename][charGroupName][mastername] = forced_Setup_on_all_Groups[mastername]




			for charGroupName in data["InstancesSetup"][instancename]:
				if not (charGroupName == "#All"):
					if not (charGroupName == "_All_Force"):
						tempdata = copy.deepcopy(data)
						del data["InstancesSetup"][instancename][charGroupName]
						data["InstancesSetup"][instancename][charGroupName] = {}

						data["InstancesSetup"][instancename][charGroupName] = tempdata[
							"InstancesSetup"][instancename]["#All"]

						for mastername in tempdata["InstancesSetup"][instancename][charGroupName]:
							data["InstancesSetup"][instancename][charGroupName][mastername] = tempdata[
								"InstancesSetup"][instancename][charGroupName][mastername]




def convertNormal2XYinterpolation(data):

	childs = False

	for mastername in data["MasterSetupMapping"]:


		if not mastername.startswith("_"):
			values = data["MasterSetupMapping"][mastername]
			if (len(values) > 2):  # gets childs
				childs = values.pop(-1)

			else:
				childs = False

			interpolrange = values


			if not (type(interpolrange[0]) == list):
				newvalues = [interpolrange, interpolrange]

			else:
				newvalues = interpolrange

			if (childs):
				newvalues.append(childs)

			data["MasterSetupMapping"][mastername] = newvalues

	for instancename in data["InstancesSetup"]:

		if not instancename.startswith("_"):


			for charGroupName in data["InstancesSetup"][instancename]:



				if not charGroupName.startswith("_"):

					for mastername in data["InstancesSetup"][instancename][charGroupName]:

						if not mastername.startswith("_"):




							interpolvals = data["InstancesSetup"][
								instancename][charGroupName][mastername]



							if not (type(interpolvals) == list):
								valuestr = str(interpolvals)
								tempMin = str(data["MasterSetupMapping"][
											  mastername][0][0])
								tempMax = str(data["MasterSetupMapping"][
											  mastername][0][1])
								tempHalf = str(
									map(0.5, 0, 1, eval(tempMin), eval(tempMax)))





								valuetemp = valuestr.replace("parent", tempMin)
								valuestr = str(valuetemp)
								valuetemp = valuestr.replace("none", tempMin)
								valuestr = str(valuetemp)
								valuetemp = valuestr.replace("min", tempMin)
								valuestr = str(valuetemp)

								valuetemp = valuestr.replace("half", tempHalf)


								valuestr = str(valuetemp)

								valuetemp = valuestr.replace("full", tempMax)
								valuestr = str(valuetemp)
								valuetemp = valuestr.replace("max", tempMax)
								valuestr = str(valuetemp)

								valuestr = valuetemp

								interpolval = eval(valuestr)

								data["InstancesSetup"][instancename][charGroupName][
									mastername] = [interpolval, interpolval]
							else:


								new_interpolvals = []
								for k in range(len(interpolvals)):

									valuestr = str(interpolvals[k])
									tempMin = str(data["MasterSetupMapping"][
												  mastername][k][0])
									tempMax = str(data["MasterSetupMapping"][
												  mastername][k][1])
									tempHalf = str(
										map(0.5, 0, 1, eval(tempMin), eval(tempMax)))

									tempDouble = str(
										map(2, 0, 1, eval(tempMin), eval(tempMax)))







									valuetemp = valuestr.replace(
										"parent", tempMin)
									valuestr = str(valuetemp)
									valuetemp = valuestr.replace(
										"none", tempMin)
									valuestr = str(valuetemp)
									valuetemp = valuestr.replace(
										"min", tempMin)
									valuestr = str(valuetemp)

									valuetemp = valuestr.replace(
										"half", tempHalf)
									valuestr = str(valuetemp)

									valuetemp = valuestr.replace(
										"double", tempDouble)
									valuestr = str(valuetemp)

									valuetemp = valuestr.replace(
										"full", tempMax)
									valuestr = str(valuetemp)
									valuestr = valuetemp
									valuetemp = valuestr.replace(
										"max", tempMax)
									valuestr = str(valuetemp)
									valuestr = valuetemp

									interpolval = eval(valuestr)
									new_interpolvals += [interpolval]


								data["InstancesSetup"][instancename][charGroupName][
									mastername] = [new_interpolvals[0], new_interpolvals[1]]














class Multipolation(object):

	def __init__(self):
		print "\n\n#0 Init Multipolation"
		print "----------------------------------------------------------------------"
		print "----------------------------------------------------------------------"
		jsonpath = Font.filepath.replace(".glyphs", jsonfilename)

		self.LoadSpecification(jsonpath)

	def LoadSpecification(self, jsonpath):

		print "\n\n#1 Load Specification"
		print "----------------------------------------------------------------------"

		print "  Spec Filename = ", jsonpath.split("/")[-1]


		with open(jsonpath) as data_file:
			data = json.load(data_file)

			data = byteify(data)  # convert unicode


		self.SliderInterface(data)

	def SliderInterface(self, data):
		print "\n\n#2 Init Interface"
		print "----------------------------------------------------------------------"
		print "  There are no sliders, nor a basic interface yet. Please edit the .json"

		self.Interpolation(data)

	def Interpolation(self, data):
		print "\n\n#3 Interpolate"
		print "----------------------------------------------------------------------"




		Activate_New_Instances = True
		Activate_Last_Filter = False
		Add_Masters_as_Instances = False



		try:
			General_Custom_Parameter_Before = data["GeneralSetup"]["Filters_general_before"]
		except:
			General_Custom_Parameter_Before = data["GeneralSetup"]["Custom_Parameter_before"]


		try:
			General_Custom_Parameter_After = data["GeneralSetup"]["Filters_general_after"]
		except:
			General_Custom_Parameter_After = data["GeneralSetup"]["Custom_Parameter_after"]










		convert2LocalInterpolation(data)


		convertNormal2XYinterpolation(data)



		Instances_reset_all = data["GeneralSetup"][
			"Instances_reset_all"]  # False

		Add_Custom_Parameter = len(General_Custom_Parameter_Before) or len(General_Custom_Parameter_After)  # True #eg Filters





		interpol_array = []
		Instances = Font.instances
		Masters = Font.masters
		Master_Count = len(Masters)
		Instances_Count = len(Instances)
		print "	- Mastercount: ", Master_Count




		Instance_reset_Values = []

		for k in range(0, Master_Count - 1, 1):
			Instance_reset_Values = Instance_reset_Values + \
				[0.0]  # .append(0.0)






		if(Add_Masters_as_Instances):

			interpol_array.append(
				Instance_reset_Values + ["0 - Root-Master"] + [General_Custom_Parameter_Before])



			for j in range(1, Master_Count, 1):  # 0, Master_Count-1, 1)
				interpol_array.append(Instance_reset_Values[
									  :])  # use as a copy
				interpol_array[-1][j - 1] = 1.0

				interpol_array[-1].append(Masters[j].name)
				interpol_array[-1].append(General_Custom_Parameter_Before)




		def process(interpol_array):  # slider,




			interpol_array = []
			InstancesNames = []
			Instances_Count = len(Instances)

			sinnlosboldvalue = []
			sinnlosboldvalue_str = ""
			interpolcalcvalue_new = [0.0, 0.0]
			interpolcalcvalue = [0.0, 0.0]




			MasterNamesCalcOrderArray = getInstanceMasterValuesCalcOrder(
				data)  # format is: {"Name of Master":1}
			print "	- MasterNames", MasterNamesCalcOrderArray








			Interpol_Count = len(data["InstancesSetup"]) - 1

			print "	-", Interpol_Count, "Setups for Interpolation (", Instances_Count, " current Instances )"
			print " "



			if(Instances_reset_all):


				Font.instances = ()





				Instances_added = ""
				for instancename in data["InstancesSetup"]:
					if not instancename.startswith("_"):


						AddInstance(instancename, General_Custom_Parameter_Before)
						Instances_added += instancename + ", "
				print ""
				print ">> Instances removed and added: "
				print ""
				print Instances_added
				print "----------------------------------------------------------------------\n"

			else:
				if(Instances_Count != Interpol_Count):
					raise Exception(
						'Check Instances in the info panel (Names and Count) or activate "Instances_reset_all" in the Multipolation Spec File')

			multiplemode = 1



			finaloverallcalcsum = [0.0, 0.0]
			interpolmapvalue = [0.0, 0.0]
			interpol_child_sum = [0.0, 0.0]
			interpol_child_calc = [0.0, 0.0]
			interpolcalcvalue = [0.0, 0.0]



			for instancename in data["InstancesSetup"]:

				if not instancename.startswith("_"):

					for charGroupName in data["InstancesSetup"][instancename]:
						if not charGroupName.startswith("_"):





							instanceindex = getGSObjectIndex(
								Instances, instancename)
							Instance = Font.instances[instanceindex]


							Instance.setManualInterpolation_(True)



							if not instancename.startswith("_"):

								InstanceName = instancename  # Todo clean up

								finaloverallcalcsum = [0.0, 0.0]
								interpol_sum = [0.0, 0.0]  # clear to zero



								for mastername in data["InstancesSetup"][instancename][charGroupName]:
									if mastername.startswith("_"):
										if mastername.startswith("_Custom_Parameter"):
											Instance_Custom_Parameter = data["InstancesSetup"][instancename][charGroupName][mastername]
										if mastername.startswith("_Active"):
											if data["InstancesSetup"][instancename]["#All"][mastername] == False:
												Instance.active = False



									if not mastername.startswith("_"):



										value_original_readable = [0.0, 0.0]
										interpolmapvalue_new = [0.0, 0.0]




										test = data["InstancesSetup"][
											instancename][charGroupName][mastername]
										if (type(test) == dict):
											data["InstancesSetup"][instancename][charGroupName][mastername] = data[
												"InstancesSetup"][instancename][charGroupName][mastername]["read"]

										for k in range(len(data["InstancesSetup"][instancename][charGroupName][mastername])):

											value_original_readable[k] = data["InstancesSetup"][
												instancename][charGroupName][mastername][k]
											masterMin = data["MasterSetupMapping"][
												mastername][k][0]
											masterMax = data["MasterSetupMapping"][
												mastername][k][1]






											interpolmapvalue_new[k] = map(value_original_readable[
																		  k], masterMin, masterMax, 0, 1)


											interpol_sum[
												k] += interpolmapvalue_new[k]


										readablevalue = value_original_readable




										data["InstancesSetup"][instancename][charGroupName].update(
											{mastername: {"read": value_original_readable, "map": interpolmapvalue_new, "calc": [0, 0], "childsum": [0, 0]}})











							Instance.setManualInterpolation_(True)


							LocalGlyphInterpolations[0] = ""


							for mastername in MasterNamesCalcOrderArray:



								if not mastername.startswith("_"):




									interpolmapvalue = data["InstancesSetup"][instancename][charGroupName][mastername]["map"]





									if (len(data["MasterSetupMapping"][mastername]) > 2):







										children = data["MasterSetupMapping"][
											mastername][-1]


										if (children == "All"):


											children = getMasterNames(
												mastername)

											data["MasterSetupMapping"][
												mastername][-1] = children





										masterNameArray = getMasterNames("")
										masterselection = children







										interpol_child_sum = sumSelDictValues(data["InstancesSetup"][instancename][
																			  charGroupName], masterselection, "calc")

										data["InstancesSetup"][instancename][charGroupName][
											mastername]["childsum"] = redefinelist(interpol_child_sum)




										for k in range(len(interpolcalcvalue)):
											interpolcalcvalue_new[k] = interpolmapvalue[
												k] - interpol_child_sum[k]




									else:
										for k in range(len(interpolcalcvalue)):
											interpolcalcvalue_new[
												k] = interpolmapvalue[k]

										children = False






									data["InstancesSetup"][instancename][
										charGroupName][mastername]["calc"] = ""

									data["InstancesSetup"][instancename][charGroupName][
										mastername]["calc"] = redefinelist(interpolcalcvalue_new)


									shit = data["InstancesSetup"][instancename][
										charGroupName][mastername]["calc"]






									interpolcalcvalue = interpolcalcvalue_new
									interpol_child_sum = data["InstancesSetup"][
										instancename][charGroupName][mastername]["childsum"]

									readablevalue = data["InstancesSetup"][
										instancename][charGroupName][mastername]["read"]
									readablevaluespan = [data["MasterSetupMapping"][mastername][
										0], data["MasterSetupMapping"][mastername][1]]

















									for k in range(len(finaloverallcalcsum)):
										finaloverallcalcsum[
											k] += interpolcalcvalue[k]





									masterindex = getGSObjectIndex(
										Masters, mastername)

									if (charGroupName == "#All"):
										interpolcalcvalue_x = interpolcalcvalue[
											0]
										interpolcalcvalue_y = interpolcalcvalue[
											1]
										xy_interpolation = NSValue.valueWithPoint_(
											(interpolcalcvalue_x, interpolcalcvalue_y))

										Instance.instanceInterpolations[
											Masters[masterindex].id] = xy_interpolation












							if not (charGroupName == "#All"):
								for k in range(len(Font.masters)):
									mastername = byteify(Font.masters[k].name)




									interpolcalcvaluesStr = str(data["InstancesSetup"][instancename][charGroupName][
																mastername]["calc"]).replace("[", "{").replace("]", "}")






									LocalGlyphInterpolations[0] += interpolcalcvaluesStr + ";"









								scope = str(data["InstancesSetup"][instancename][charGroupName]["_Scope"])  # "include:H"
								LocalGlyphInterpolations[0] = "Local Interpolation::=;" + LocalGlyphInterpolations[0] + scope


								AddCustomParameter(Instance, LocalGlyphInterpolations)






					try:
						if Instance_Custom_Parameter:
							AddCustomParameter(Instance, Instance_Custom_Parameter)
					except:
						pass



					AddCustomParameter(Instance, General_Custom_Parameter_After)

					if ([1.0, 1.0] == finaloverallcalcsum):
						print "- Instance successful created: ", InstanceName







		process(interpol_array)


Multipolation()




