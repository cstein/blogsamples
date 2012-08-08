import openbabel

from obutil import OBStructureFromSmiles
from aminoacids import getAminoAcids

if __name__ == '__main__':

  # for now just default to amino acids from the amino acids library
  AA = getAminoAcids(True)
  for k in AA:
    OBStructureFromSmiles(AA[k], k)
