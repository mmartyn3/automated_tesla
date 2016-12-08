## Genome information
# PputidaKT2440 (6.1 Mbp) GC content <- 61.5% (GC 0.3075; AT 0.1925)   (http://www.straininfo.net/genomes/267)
# PputidaKT2440 (12452060 bases) GC content <- 61.1% (GC 0.3055; AT 0.1945)   AE015451 + GCcontentCalc.py
# EcoliMG1655 (4.6397 Mbp) GC content <- 50.8%  (GC 0.254; AT 0.246)    (http://www.straininfo.net/genomes/225)
# EcoliMG1655 (9349615 bases) GC content <- 50.4%  (GC 0.252; AT 0.248)   NC_000913 + GCcontentCalc.py 
# EcoliBL21 (4.6 Mbp) GC content <- 50.8%  (GC 0.254; AT 0.246)    (http://www.straininfo.net/genomes/20713)
# EcoliBL21 (9183023 bases) GC content <- 50.5%  (GC 0.2525; AT 0.2475)    AM946981 + GCcontentCalc.py
# Bsubtilis168 (4.1 Mbp) GC content <- 43.5%   (GC 0.2175; AT 0.2825)   (http://www.straininfo.net/genomes/76)
# Bsubtilis168 (8491436 bases) GC content <- 43.2%   (GC 0.216; AT 0.284)   NC_000964 + GCcontentCalc.py
# SpyogenesM1GAS (3731331 bases) GC content <- 38.2% (GC 0.191; AT 0.309)  AE004092 + GCcontentCalc.py

## Assumptions
# Random distribution of bases

## Motif information
# S <- {A,T,C,G}  ## Sample space
# N <- A|T|G|C; R <- A|G
# SpCas9 <- NGG (off-targets inc. NGG & NAG)  ## PAM for Streptococcus pyogenes Cas9
# SaCas9 <- NNGRRT (off-targets inc. NNGRR)  ## PAM for Staphylococcus aureus Cas9 

## Initialisations
p.nucleotide <- vector() ## Initialize a vector to store nucleotide probabilities
p.motif <- vector() ## Initialize a vector to store motif probabilities
M <- "GGGT"  ## Motif
#M = "GG"
k <- nchar(M)  ## Motif length
L <- 6000000 ## Genome length

## Nucleotide frequencies
p.nucleotide["A"] <- 0.3
p.nucleotide["T"] <- 0.3
p.nucleotide["C"] <- 0.2
p.nucleotide["G"] <- 0.2

## calculate P(motif)
p.motif[M] <- 1 # initialize
for (i in 1:nchar(M)) {
  nucleotide <- substr(M,i,i) ## Select the nucleotide at position i of motif M
  p.motif[M] <- p.motif[M]*p.nucleotide[nucleotide] ## update motif probability
}

## Calculate number of positions for a motif of length k in a genome of length L
pos <- L - k + 1

## Expected number of occurrences is the product of the number of possible positions by the probability of occurrence at a given position.
E.occ <- pos*p.motif[M]
print(E.occ)
