# Assign unnamed pads to GND plugin for KiCAD
# (C) 2022, Dr. Bo Gao
# This work is published to the public domain
# Where public domain is not recognized, this work is licensed under the CC0 license
# This work uses icon designed by Freepik from Flaticon

import pcbnew
import os

class AssignGnd(pcbnew.ActionPlugin):
	def defaults(self):
		self.name="Assign unnamed pads to net GND"
		self.category="Net"
		self.description="Assign unnamed pads to net GND"
		self.show_toolbar_button=True
		self.icon_file_name=os.path.join(os.path.dirname(__file__), "assign_gnd.png")
	
	def Run(self):
		ng=None # Find netcode of GND net
		for nc, n in pcbnew.GetBoard().GetNetsByNetcode().items():
			if n.GetNetname()=="/GND" or n.GetNetname()=="/gnd":
				ng=nc
				break
		if ng==None: return
		# Find unnamed pads and set netcode to GND netcode
		for f in pcbnew.GetBoard().GetFootprints():
			p=f.Pads()
			for pd in iter(p):
				if pd.GetName()=="":
					pd.SetNetCode(ng)
		pcbnew.Refresh()

AssignGnd().register()