# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 19:30:42 2018

@author: john3
"""

import Indigo
indigo = Indigo.indigo.Indigo()
m1=indigo .loadMolecule("CC(C)C=CCCCCC(=O)NCc1ccc(c(c1)OC)O")
m2=indigo .loadMolecule("COC1=C(C=CC(=C1)C=O)O")
m1.aromatize()
m2.aromatize()
print(m1.countAtoms())
print(m2.countAtoms())

fp1=m1.fingerprint('sim')
fp2=m1.fingerprint('sim')

print("  Tanimoto: %s" % (indigo .similarity(fp1, fp2, 
"tanimoto")))