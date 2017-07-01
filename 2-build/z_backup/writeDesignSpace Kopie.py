from designSpaceDocument import DesignSpaceDocument, SourceDescriptor, InstanceDescriptor, AxisDescriptor
import os

designSpacePath = "RobotoFlex.designspace"
familyName = "RobotoFlex"

sources = [
	dict(path="master_ufo/RobotoFlex-Default.ufo", name="RobotoFlex-Default.ufo", location=dict(weight=88, width=402, opticalsize=14, xopaque=88, xtransparent=402, yopaque=50, lcytransparent=500, serifheight=18), styleName="Default", familyName=familyName, copyInfo=True),
	# registered
	dict(path="master_ufo/RobotoFlex-wght-min.ufo", name="RobotoFlex-wght-min.ufo", location=dict(weight=38), styleName="wght-min", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/RobotoFlex-wght-max.ufo", name="RobotoFlex-wght-max.ufo", location=dict(weight=250), styleName="wght-max", familyName=familyName, copyInfo=False),

	# dict(path="master_ufo/RobotoFlex-wdth-min.ufo", name="RobotoFlex-wdth-min.ufo", location=dict(width=60), styleName="wdth-min", familyName=familyName, copyInfo=False),

	# dict(path="master_ufo/RobotoFlex-opsz-min.ufo", name="RobotoFlex-opsz-min.ufo", location=dict(opticalsize=10), styleName="opsz-min", familyName=familyName, copyInfo=False),
	# dict(path="master_ufo/RobotoFlex-opsz-max.ufo", name="RobotoFlex-opsz-max.ufo", location=dict(opticalsize=72), styleName="opsz-max", familyName=familyName, copyInfo=False),

	# private
	dict(path="master_ufo/RobotoFlex-XOPQ-min.ufo", name="RobotoFlex-XOPQ-min.ufo", location=dict(xopaque=5), styleName="XOPQ-min", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/RobotoFlex-XOPQ-max.ufo", name="RobotoFlex-XOPQ-max.ufo", location=dict(xopaque=500), styleName="XOPQ-max", familyName=familyName, copyInfo=False),

	dict(path="master_ufo/RobotoFlex-XTRA-min.ufo", name="RobotoFlex-XTRA-min.ufo", location=dict(xtransparent=42), styleName="XTRA-min", familyName=familyName, copyInfo=False),

	dict(path="master_ufo/RobotoFlex-YOPQ-min.ufo", name="RobotoFlex-YOPQ-min.ufo", location=dict(yopaque=4), styleName="YOPQ-min", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/RobotoFlex-YOPQ-max.ufo", name="RobotoFlex-YOPQ-max.ufo", location=dict(yopaque=85), styleName="YOPQ-max", familyName=familyName, copyInfo=False),

	dict(path="master_ufo/RobotoFlex-YTLC-min.ufo", name="RobotoFlex-YTLC-min.ufo", location=dict(lcytransparent=445), styleName="YTLC-min", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/RobotoFlex-YTLC-max.ufo", name="RobotoFlex-YTLC-max.ufo", location=dict(lcytransparent=600), styleName="YTLC-max", familyName=familyName, copyInfo=False),

	dict(path="master_ufo/RobotoFlex-YTSE-min.ufo", name="RobotoFlex-YTSE-min.ufo", location=dict(serifheight=0), styleName="YTSE-min", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/RobotoFlex-YTSE-max.ufo", name="RobotoFlex-YTSE-max.ufo", location=dict(serifheight=48), styleName="YTSE-max", familyName=familyName, copyInfo=False),

	dict(path="master_ufo/RobotoFlex-GRAD-min.ufo", name="RobotoFlex-GRAD-min.ufo", location=dict(grade=25), styleName="GRAD-min", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/RobotoFlex-GRAD-max.ufo", name="RobotoFlex-GRAD-max.ufo", location=dict(grade=250), styleName="GRAD-max", familyName=familyName, copyInfo=False),
]
axes = [
	dict(minimum=38, maximum=250, default=88, name="weight", tag="wght", labelNames={"en": "Weight"}, map=[]),
	dict(minimum=60, maximum=402, default=402, name="width", tag="wdth", labelNames={"en": "Width"}, map=[]),
	dict(minimum=10, maximum=72, default=14, name="opticalsize", tag="opsz", labelNames={"en": "Optical Size"}, map=[]),
	dict(minimum=5, maximum=500, default=88, name="xopaque", tag="XOPQ", labelNames={"en": "x opaque"}, map=[]),
	dict(minimum=42, maximum=402, default=402, name="xtransparent", tag="XTRA", labelNames={"en": "x transparent"}, map=[]),
	dict(minimum=4, maximum=85, default=50, name="yopaque", tag="YOPQ", labelNames={"en": "y opaque"}, map=[]),
	dict(minimum=445, maximum=600, default=500, name="lcytransparent", tag="YTLC", labelNames={"en": "lc y transparent"}, map=[]),
	dict(minimum=0, maximum=48, default=18, name="serifheight", tag="YTSE", labelNames={"en": "Serif height"}, map=[]),
	dict(minimum=25, maximum=250, default=88, name="grade", tag="GRAD", labelNames={"en": "Grade"}, map=[]),
]

instances = [
#	dict(location=dict(weight=1), styleName="InstanceName", familyName=familyName),
]

#for source in sources:
#	instances.append(dict(location=source["location"], styleName=source["styleName"], familyName=source["familyName"]))

###

doc = DesignSpaceDocument()

for source in sources:
	s = SourceDescriptor()
	s.path = source["path"]
	s.name = source["name"]
	s.copyInfo = source["copyInfo"]
	s.location = source["location"]
	s.familyName = source["familyName"]
	s.styleName = source["styleName"]
	doc.addSource(s)

for instance in instances:
	i = InstanceDescriptor()
	i.location = instance["location"]
	i.familyName = instance["familyName"]
	i.styleName = instance["styleName"]
	doc.addInstance(i)

for axis in axes:
	a = AxisDescriptor()
	a.minimum = axis["minimum"]
	a.maximum = axis["maximum"]
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
