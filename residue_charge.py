#!/usr/bin/env python
"""
residue_charge.py - Determine the charge of residues using Open Babel
"""
import sys

if( len(sys.argv) != 2 ):
  print "Usage: residue_charge <in.pdb>"
  sys.exit()
file_in = sys.argv[1]

import openbabel
obConversion = openbabel.OBConversion()
obConversion.SetInFormat("pdb")

mol = openbabel.OBMol()
obConversion.ReadFile(mol, file_in)

# get the charges of the atoms
charge_model = openbabel.OBChargeModel.FindType("mmff94")
charge_model.ComputeCharges(mol)
partial_charges = charge_model.GetPartialCharges()

# iterate over residues to get atoms in residues and
# in turn get the atom indices so we can map partial
# charges to the residues
total_charge = 0.0
for residue in openbabel.OBResidueIter( mol ):
  residue_charge = 0.0
  for atom in openbabel.OBResidueAtomIter( residue ):
    atom_idx = atom.GetIdx()
    # NB! openbabel counts from 1 to N, python does not
    residue_charge += partial_charges[atom_idx - 1]

  total_charge += residue_charge

  # residue complete, print information
  print "name = %5s, charge=%3i" % (residue.GetName(), int(round(residue_charge)))

print "total charge=%3i" % total_charge
print "partial chgs=%f" % sum(partial_charges)
