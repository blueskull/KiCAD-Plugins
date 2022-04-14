# Align all footprints to the nearest 0.025mm plugin for KiCAD
# (C) 2022, Dr. Bo Gao
# This work is published to the public domain
# Where public domain is not recognized, this work is licensed under the CC0 license
# This work uses icon designed by Ilham Fitrotul Hayat from Flaticon

import pcbnew
import os

class AlignToGrid(pcbnew.ActionPlugin):
	def defaults(self):
		self.name="Align all components to grid"
		self.category="Placement"
		self.description="Align all components to grid"
		self.show_toolbar_button=True
		self.icon_file_name=os.path.join(os.path.dirname(__file__), "align_to_grid.png")
	
	def Run(self):
		# Go through all footprints
		for f in pcbnew.GetBoard().GetFootprints():
			# Round to the nearest 0.025mm
			x=round(f.GetX()/25000)*25000
			y=round(f.GetY()/25000)*25000
			f.SetX(x)
			f.SetY(y)
		pcbnew.Refresh()

AlignToGrid().register()