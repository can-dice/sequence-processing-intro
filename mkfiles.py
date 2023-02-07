#making dna files as well as protein files
def mkfiles(filename, Type):
    File=open(filename,"r")
    for line in File:
        f=open(line.strip()+".f"+Type+"a","w")
        f.write(line)
        f.write(File.readline().strip())    
    f.close()
    File.close()

mkfiles("ExampleAlignment.fasta","n")
mkfiles("protein.fasta","a")
