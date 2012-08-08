def getAminoAcids(include_protonated=False):
  molecules = dict()
  molecules['GLY'] = 'NCC(=O)O'
  molecules['ALA'] = 'NC(C)C(=O)O'
  molecules['SER'] = 'NC(CO)C(=O)O'
  molecules['THR'] = 'NC(C(C)O)C(=O)O'
  molecules['CYS'] = 'NC(CS)C(=O)O'
  molecules['VAL'] = 'NC(C(C)C)C(=O)O'
  molecules['LEU'] = 'NC(CC(C)C)C(=O)O'
  molecules['ILE'] = 'NC(C(C)CC)C(=O)O'
  molecules['MET'] = 'NC(CCSC)C(=O)O'
  molecules['PRO'] = 'N1C(C(=O)O)CCC1'
  molecules['PHE'] = 'NC(Cc1ccccc1)C(=O)O'
  molecules['TYR'] = 'NC(Cc1cc(O)ccc1)C(=O)O'
  molecules['TRP'] = 'NC(Cc1c2ccccc2nc1)C(=O)O'
  molecules['ASP'] = 'NC(CC(=O)O)C(=O)O'
  molecules['GLU'] = 'NC(CCC(=O)O)C(=O)O'
  molecules['ASN'] = 'NC(CC(=O)N)C(=O)O'
  molecules['GLN'] = 'NC(CCC(=O)N)C(=O)O'
  molecules['HIS'] = 'NC(C(=O)O)Cc1cncn1'
  molecules['LYS'] = 'NC(CCCCN)C(=O)O'
  molecules['ARG'] = 'NC(CCCNC(=N)N)C(=O)O'

  if include_protonated is True:
    # add protonated versions of bases
    molecules['HISp'] = 'NC(C(=O)O)Cc1c[nH+]cn1'
    molecules['LYSp'] = 'NC(CCCC[NH3+])C(=O)O'
    molecules['ARGp'] = 'NC(CCCNC(=[NH2+])N)C(=O)O'

    # add deprotonated versions of acids
    molecules['ASPd'] = 'NC(CC(=O)[O-])C(=O)O'
    molecules['GLUd'] = 'NC(CCC(=O)[O-])C(=O)O'

  return molecules
