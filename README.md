# RobotoFlex
- experiment to test the capabilities of the new variable font-format
- work in progress

Preview in [Fontview](https://github.com/googlei18n/fontview/releases):
![robotoflex preview](README_media/Preview.gif)

### Features currently missing in the font format (for this project)
- per-glyph-interpolation axes (the “Height”-subaxes are currently achieved by a workaround)
- hierachies + math for the slider behaviour to increase usability (e.g. to make the faux-mono-axis a child of the mono-axis, to prevent strange results if both are applied) 
- unrestricted interpolation-value-bounds (allow extrapolation, and leave it to the designer to decide when it’s good or bad)
- possiblity to add a baseline-shift axis without an aditional master
- possiblity to add a proportional scale axis without an aditional master

.

## Basic Setup / Install
- To handle complex interpolations in Glyphs: [0-install/Multipolation](0-install/)
- To export Instances as UFOs (to build the variable font): [0-install/Export Instances as UFO](0-install/)
- To preview: [Fontview](https://github.com/googlei18n/fontview/releases) or http://axis-praxis.org

.

## Drawing
### Files
- RobotoFlex.glyphs
- RobotoFlex_multipolation-spec.json (own designspace format)
		
### Multipolation-Space (Design-Space)
**Master-Setup**
- setting up relations and custom scales (also allows different x/y-values)
![robotoflex preview](README_media/Multipolation-JSON_MasterSetupMapping.png)
("MasterName": [origin-value, master-value, ["Children"]])

**Instance-Setup**
- specifying Instances
- set up different values for SmallCaps, ...  (“local interpolations”)
![robotoflex preview](README_media/Multipolation-JSON_GlyphSpecificInterpolations.png)

**How to create/update instances in Glyphs**
- Execute the [Multipolation](0-install/) script (Glyphs > Script > Multipolation).

.

## Building Variable Font
Direct export from Glyphs is not yet supported, therefore the following workaround.

### Files
- RobotoFlex.designspace
- build.sh

### Build
1. Export UFOs (use the ‘Export_Instances_as_UFO’ script)
2. Update the axis setup in ‘build/RobotoFlex_DesignSpace.py’ (if necessary)
3. Install some python font libraries
	- [Fontmake](https://github.com/googlei18n/fontmake) (if not already installed)
	- [designSpaceDocument](https://github.com/LettError/designSpaceDocument) (move the it to your python-packages folder)
4. execute the build.sh file via Terminal ([instructions](https://apple.stackexchange.com/questions/235128/how-do-i-run-a-sh-or-command-file-in-terminal))
5. Cross fingers and enjoy :)

If it did not work have a look over here: https://github.com/scribbletone/i-can-variable-font)
