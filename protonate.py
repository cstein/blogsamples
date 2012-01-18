import sys
import openbabel
from obutil import *

if __name__ == "__main__":
  if( len(sys.argv) != 3 ):
    print "Usage: protonate <in.pdb> <out.pdb>"
    sys.exit()
  file_in = sys.argv[1]
  file_out = sys.argv[2]

  mol = OBMolFromFilename(file_in)
  for residue in openbabel.OBResidueIter(mol):
    rname = residue.GetName()
    chain = residue.GetChain()
    for atom in openbabel.OBResidueAtomIter(residue):
      if atom.IsCarbon() or atom.IsNitrogen():
        idx = atom.GetIdx()
        imval = atom.GetImplicitValence()
        reval = atom.GetValence()
        if imval != reval:
          print "%5i (%3s %s) %2i %2i" % (idx,rname,chain,imval,reval)
          mol.AddHydrogens(atom)

  OBMolToFilename(mol, file_out)
