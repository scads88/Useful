# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 19:35:43 2018

@author: john3
"""
import indigo

g=indigo.Indigo()


m1=g.loadMolecule("CC(C)C=CCCCCC(=O)NCc1ccc(c(c1)OC)O")
m2=g.loadMolecule("COC1=C(C=CC(=C1)C=O)O")
m1.aromatize()
m2.aromatize()

print(m1.countAtoms())
print(m2.countAtoms())

fp1=m1.fingerprint('sim')
fp2=m2.fingerprint('sim')

print("  Tanimoto: %s" % (g.similarity(fp1, fp2, 
"tanimoto")))
