from Bio.Seq import Seq
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import os
from cycler import cycler

direc = os.path.normpath("GbBacv2/")

genSizeList = []
gcList = []

numNGGPamList = []
tmpNGGPamList = []

numNNGRRTPamList = []
tmpNNGRRTPamList = []

numNNAGAAWPamList = []
tmpNNAGAAWPamList = []

numNNNNGATTPamList = []
tmpNNNNGATTPamList = []

acceptBases = "ATCG"

for subdir, dirs, files in os.walk(direc):
	for file in files:
		if file.endswith("genomic.fna"):
			f = open(os.path.join(subdir, file),'r').readlines()[1:]
			f = ''.join(f)
			f = f.replace('\n','').upper()
			seq = ""
			for base in f:
				if base in acceptBases:
					seq += base
			f_revseq = Seq(seq)
			f_rev = str(f_revseq.reverse_complement())

			# calc gen size in Mb
			genSizeAct = len(seq)
			genSizeMb = genSizeAct / 100000
			genSizeList.append(genSizeAct)

			# GC content calc
			GCcount = seq.count("G") + seq.count("C") 
			GC_content = (float(GCcount) / float(genSizeAct)) * 100
			gcList.append(GC_content)

			# calc number of NGG PAMS
			tmpNGGPamList = seq.count("GG") 
			tmpNGGPamList = float(tmpNGGPamList) / 1000
			numNGGPamList.append(tmpNGGPamList)

			# calc number of NNGRRT PAMS (R = A or G)
			tmpNNGRRTPamList = seq.count("GAAT") + seq.count("GAGT") + seq.count("GGAT") + seq.count("GGGT")
			tmpNNGRRTPamList = float(tmpNNGRRTPamList) / 1000
			numNNGRRTPamList.append(tmpNNGRRTPamList)

			# calc number of NNAGAAW PAMS (W = A or T)
			tmpNNAGAAWPamList = seq.count("AGAAA") + seq.count("AGAAT")
			tmpNNAGAAWPamList = float(tmpNNAGAAWPamList) / 1000
			numNNAGAAWPamList.append(tmpNNAGAAWPamList)

			# calc number of NNNNGATT PAMS (W = A or T)
			tmpNNNNGATTPamList = seq.count("GATT")
			tmpNNNNGATTPamList = float(tmpNNNNGATTPamList) / 1000
			numNNNNGATTPamList.append(tmpNNNNGATTPamList)


fig = plt.figure()
ax = plt.axes(projection='3d')

ax.scatter(genSizeList, gcList, numNGGPamList, c='r', marker='o', label='SpCas9 (NGG)')
ax.scatter(genSizeList, gcList, numNNGRRTPamList, c='b', marker='*', label='SaCas9 (NNGRRT)')
ax.scatter(genSizeList, gcList, numNNAGAAWPamList, c='m', marker='v', label='StCas9 (NNAGAAW)')
ax.scatter(genSizeList, gcList, numNNAGAAWPamList, c='c', marker='h', label="NmCas9 (NNNNGATT)")

ax.set_xlabel('Genome size (Mb)')
ax.set_ylabel('GC content (%)')
ax.set_zlabel('Number of PAMs (1000s)')

plt.legend(loc='upper left')
plt.show()
