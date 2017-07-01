# Before use, make sure you have exported all necessary UFOs from GlYPHS (to temp/ufo)

# Generate .designspace file, as writing it by hand is difficult for larger projects
python RobotoFlex-Spacing-only_DesignSpace.py

# Generate separate interpolatable TTFs # VERY SLOW, consider to comment it out, when you dont need
#fontmake -o ttf-interpolatable -m RobotoFlex.designspace --no-production-names --subset --keep-overlaps --keep-direction


# Generate Variable Font
fonttools varLib RobotoFlex.designspace

# Move to main Folder
mv RobotoFlex-VF.ttf RobotoFlex-Spacing.ttf
