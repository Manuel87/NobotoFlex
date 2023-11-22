# Noboto Flex
- experiment to test the capabilities of the new variable font-format
- work in progress
- based on Roboto

Interactive Preview
![robotoflex preview](README_media/Preview.gif)
External Link: http://manuel.vongebhardi.com/variable-fonts/testing/

## Note on a few unconventional axes (scale + baseline shift)
Especially the scale and the baseline shift axis isn't really anything I would recommend adding to your variable font. I believe that this should actually be an extra feature embedded within any variable font and could be optionally turned on or off in an UI. These two axes are fundamentally important if you want to mix different fonts inline (e.g. upright + italic of a different font) and becomes even more important if you mix fonts accross different scripts. And yes, some applications like Indesign allow for scaling and there are tricks to get the baselines aligned. But this will be never implemented across all software, which makes it almost impossible to mix different fonts for a corporate identity.

## Basic Setup / Install
- To handle complex interpolations in Glyphs: [0-install/Multipolation](0-install/)
- To export Instances as UFOs (to build the variable font): [0-install/Export Instances as UFO](0-install/)
- To build a variable font, some py libraries: [Fonttools](https://github.com/fonttools/fonttools), [Fontmake](https://github.com/googlei18n/fontmake) and [designSpaceDocument](https://github.com/LettError/designSpaceDocument) (move it to your python-packages folder)
- To preview: [Fontview](https://github.com/googlei18n/fontview/releases) or http://axis-praxis.org

.

## Drawing
### Files
- NobotoFlex.glyphs
- NobotoFlex_multipolation-spec.json (custom ‘designspace’ format)
		
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
Direct export from Glyphs is not yet supported, therefore the following short workaround.

### Files
- script_lib_custom/ (no need to touch)
- NobotoFlex_DesignSpace.py
- build.sh
- (rest is generated by the build.sh)

### Build
1. Export UFOs (use the ‘Export_Instances_as_UFO’ script) to ‘2-build/master_ufo/’
2. Edit/update the axis setup in ‘2-build/NobotoFlex_DesignSpace.py’ (if necessary)
3. execute the build.sh file via Terminal ([instructions](https://apple.stackexchange.com/questions/235128/how-do-i-run-a-sh-or-command-file-in-terminal))
4. Cross fingers and enjoy :)

If it did not work have a look over here: https://github.com/scribbletone/i-can-variable-font)

.

## Bugs / Font format issues / ...
### Some features currently missing in the font format
- per-glyph-interpolation axes (the “Height”-subaxes are currently achieved by a workaround)
- hierachies + math for the slider behaviour to increase usability and decrease filesize (at the moment there are way more masters within this font, than actually needed) 
- please remove restricted interpolation-value-bounds (allow extrapolation, and leave it to the designer to decide when it’s good or bad)
- possiblity to add a baseline-shift axis without an aditional master (e.g. adding basic transformations)
- possiblity to add a proportional scale axis without an aditional master (is really difficult to make it work with masters!)

### Bugs / A few known issues
- This is more a demo than a full release, be aware ;)
- There are still quite a few incompatible and therefore missing glyphs 
- Mono-axes does throw an assertion error (why!?) and is therefore exluded for the moment
- Tight spacing is off (maybe a rounding problem?)
- @Glyphs: exported UFOs ignore the instances custom parameters

## License
[Roboto-License](https://github.com/google/roboto), and Additions (C) by Manuel von Gebhardi (CC BY-SA)

## Credits
This project was partially funded by Google Fonts.

## Related
- https://github.com/Manuel87/CrimVarious
- https://github.com/Manuel87/TypeVariables/
- https://github.com/Manuel87/ExperimentalParametricTypeface
- https://github.com/Manuel87/TypeMultiverse
