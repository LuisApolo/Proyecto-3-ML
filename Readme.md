# Proyecto-3-ML

Este es el tercer proyecto del curso de aprendizaje de máquina, en el que se desea realizar labores de clasificación para determinar la ubicación
de proteínas según ciertas caracteristicas (ver yeast.names).

Atributos:
1. Sequence Name: Accession number for the SWISS-PROT database
2. mcg: McGeoch's method for signal sequence recognition.
3. gvh: von Heijne's method for signal sequence recognition.
4. alm: Score of the ALOM membrane spanning region prediction program.
5. mit: Score of discriminant analysis of the amino acid content of
	   the N-terminal region (20 residues long) of mitochondrial and 
           non-mitochondrial proteins.
6. erl: Presence of "HDEL" substring (thought to act as a signal for
	   retention in the endoplasmic reticulum lumen). Binary attribute.
7. pox: Peroxisomal targeting signal in the C-terminus.
8. vac: Score of discriminant analysis of the amino acid content of
           vacuolar and extracellular proteins.
9. nuc: Score of discriminant analysis of nuclear localization signals
	   of nuclear and non-nuclear proteins.

Clases:
CYT (cytosolic or cytoskeletal)                    463
NUC (nuclear)                                      429
MIT (mitochondrial)                                244
ME3 (membrane protein, no N-terminal signal)       163
ME2 (membrane protein, uncleaved signal)            51
ME1 (membrane protein, cleaved signal)              44
EXC (extracellular)                                 37
VAC (vacuolar)                                      30
POX (peroxisomal)                                   20
ERL (endoplasmic reticulum lumen)                    5

Dataset disponible en: https://archive.ics.uci.edu/ml/datasets/Yeast

Se recomienda leer la investigación de Paul Horton & Kenta Nakai, 
"A Probablistic Classification System for Predicting the Cellular Localization Sites of Proteins", Intelligent Systems in Molecular Biology, 109-115. St. Louis, USA 1996. 
