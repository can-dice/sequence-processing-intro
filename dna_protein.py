#making the protein sequence
import Bio
from Bio.Seq import Seq
from Bio import SeqIO

protein=open("protein.fasta", "w")

for seq_record in SeqIO.parse("ExampleAlignment.fasta","fasta"):
   print(seq_record.id)
   print(repr(seq_record.seq.translate()))
   print(len(seq_record))
   protein.write(">"+seq_record.id + "\n")
   protein.write(str(seq_record.seq.translate())+"\n")
    # protein.write(str(seq_record.seq.translate()))

protein.close()
