#MenuTitle: Export Instances as UFO
# -*- coding: utf-8 -*-
__doc__="""
Exports all active Instances as UFO.
"""
import GlyphsApp
import commands
from types import *
Font = Glyphs.font



filename  = Font.familyName + '-[instance]'#Font.familyName + ' kerning'  # filename without ending
ending	= 'ufo'	   # ufo|ufo

current_file_path = '/'.join(Font.filepath.split('/')[0:-1]) # Get path of current Glyphs-File
save_path = current_file_path


# Interface
# -------------------
def saveFileDialog(message=None, ProposedFileName=None, filetypes=None):
	if filetypes is None:
		filetypes = []
	Panel = NSSavePanel.savePanel().retain()
	if message is not None:
		Panel.setTitle_(message)
	Panel.setCanChooseFiles_(False)
	Panel.setCanChooseDirectories_(True)
	Panel.setCanCreateDirectories_(True)
	Panel.setExtensionHidden_(False)
	Panel.setAllowedFileTypes_(filetypes)

	pageurl = Foundation.NSURL.URLWithString_(save_path) #convert to NSURL
	#https://stackoverflow.com/questions/15032611/how-to-self-handling-cookies-in-pyobjc
	Panel.setDirectoryURL_(pageurl)

	if ProposedFileName is not None:
		Panel.setNameFieldStringValue_(ProposedFileName)
	pressedButton = Panel.runModalForTypes_(filetypes)
	if pressedButton == 1: # 1=OK, 0=Cancel
		return Panel.filename()
	return None
saveFileDialog

filepath = saveFileDialog( message="Export Instances as UFOs", ProposedFileName=filename, filetypes=["ufo"] )




# Export Script
print(" ")
print("Following instances:")
print("-------------------------")
for i in Font.instances:
	if (i.active):
		file = i.interpolatedFont
		#path = Font.filepath.replace(".glyphs", "-" + i.name + ".ufo")
		path = filepath.replace('[instance]', i.name)
		print(" - " + i.name)
		file.save(path)

print("-------------------------")
print("saved as UFO to: " + filepath)
print(" ")
