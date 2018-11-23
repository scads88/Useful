# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 17:15:01 2018

@author: john3
"""
import Indigo
indigo=Indigo.indigo.Indigo()

m1=indigo.loadMolecule("CN(C)CCOC1=CC=C(C=C1)C(=C(CCCl)C2=CC=CC=C2)C3=CC=CC=C3")
m2=indigo.loadMolecule("C1=CC=C(C=C1)C(=C(C2=CC=CC=C2)C3=CC=C(C=C3)OCCOCCO)CCCl")
m1.aromatize()
m2.aromatize()

print(m1.countAtoms())
print(m2.countAtoms())

fp1=m1.fingerprint('sim')
fp2=m2.fingerprint('sim')

print("  Tanimoto: %s" % (indigo.similarity(fp1, fp2, "tanimoto")))
#print("  Tanimoto: %s" % (indigo.similarity(fp1, fp2, "tversky")))

#raloxifene smiles
#C1CCN(CC1)CCOC2=CC=C(C=C2)C(=O)C3=C(SC4=C3C=CC(=C4)O)C5=CC=C(C=C5)O

#toremifene smiles
#CN(C)CCOC1=CC=C(C=C1)C(=C(CCCl)C2=CC=CC=C2)C3=CC=CC=C3

#fispemifene smiles
#C1=CC=C(C=C1)C(=C(C2=CC=CC=C2)C3=CC=C(C=C3)OCCOCCO)CCCl

#enclomifene
#CCN(CC)CCOC1=CC=C(C=C1)C(=C(C2=CC=CC=C2)Cl)C3=CC=CC=C3.C(C(=O)O)C(CC(=O)O)(C(=O)O)O
"""
m1=indigo.Indigo().loadMolecule("CC(C)C=CCCCCC(=O)NCc1ccc(c(c1)OC)O")
m2=indigo.Indigo().loadMolecule("COC1=C(C=CC(=C1)C=O)O")
m1.aromatize()
m2.aromatize()

print("Similarity fingerprints:")
fp1 = m1.fingerprint("sim");
fp2 = m2.fingerprint("sim");


#print("  Tanimoto: %s" % (indigo.Indigo.similarity(fp1, fp2, "tanimoto")));
#print("  Tversky: %s" % (indigo.Indigo.similarity(fp1, fp2, "tversky")));

#print("Substructure fingerprints:");
#fp1 = m1.fingerprint("sub");
#fp2 = m2.fingerprint("sub");
 
#print("  Tanimoto: %s" % (indigo.Indigo.similarity(fp1, fp2, "tanimoto")));
#print("  Tversky: %s" % (indigo.Indigo.similarity(fp1, fp2, "tversky")));
"""