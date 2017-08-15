# Before use, make sure you have exported all necessary UFOs from GlYPHS (to temp/ufo)

# Generate .designspace file, as writing it by hand is difficult for larger projects
python NobotoFlex_DesignSpace.py

# Generate separate interpolatable TTFs # VERY SLOW, consider to comment it out, when you dont need
#fontmake -o ttf-interpolatable -m RobotoFlex.designspace --no-production-names --subset --keep-overlaps --keep-direction


# Generate Variable Font
fonttools varLib NobotoFlex.designspace

# Move to main Folder
mv NobotoFlex-VF.ttf ../NobotoFlex-VF.ttf
