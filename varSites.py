#looking for variable sites
def varSite(filename):
    f=open(filename, "r")
    first=f.readline().strip()
    compare=f.readline()
    sites=0

    for line in f:
        if line[0]==">":
            pass
        else:
            for i in range(len(compare)):
                if line[i]!=compare[i]:
                    sites+=1
    f.close()
    return sites

print(varSite("ExampleAlignment.fasta"))
print(varSite("protein.fasta"))
