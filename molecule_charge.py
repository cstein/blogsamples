#!/usr/bin/env python
"""
molecule_charge.py - Determine the charge of a molecule
"""
import sys

if( len(sys.argv) != 2 ):
  print "Usage: molecule_charge <in.pdb>"
  sys.exit()
file_in = sys.argv[1]

import openbabel
obConversion = openbabel.OBConversion()
obConversion.SetInFormat("pdb")

mol = openbabel.OBMol()
obConversion.ReadFile(mol, file_in)

# get the charges of the atoms
charge_model = openbabel.OBChargeModel.FindType("MMFF94")
charge_model.ComputeCharges(mol)
partial_charges = charge_model.GetPartialCharges()

print "%i" % int(sum(partial_charges))
