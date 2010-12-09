#!/usr/bin/env python
"""
residue_charge.py - Determine the charge of residues using openbabel

Copyright (C) 2010 by Casper Steinmann (casper.steinmann@gmail.com)

For more information, see <http://www.caspersteinmann.dk/>

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation version 2 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
"""
import openbabel
obConversion = openbabel.OBConversion()
obConversion.SetInFormat("pdb")

mol = openbabel.OBMol()
obConversion.ReadFile(mol, "1UAO.pdb")

# get the charges of the atoms
charge_model = openbabel.OBChargeModel.FindType("mmff94")
charge_model.ComputeCharges(mol)
partial_charges = charge_model.GetPartialCharges()

# iterate over residues to get atoms in residues and
# in turn get the atom indices so we can map partial
# charges to the residues
for residue in openbabel.OBResidueIter( mol ):
  residue_charge = 0.0
  for atom in openbabel.OBResidueAtomIter( residue ):
    atom_idx = atom.GetIdx()
    # NB! openbabel counts from 1 to N, python does not
    residue_charge += partial_charges[atom_idx - 1]

  # residue complete, print information
  print "name = %5s, charge=%3i" % (residue.GetName(), int(round(residue_charge)))
