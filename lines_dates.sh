#Part One
#find the number of samples and the number of unique sampling dates

#number of samples
grep ">" ExampleAlignment.fasta | wc -l >> log.txt

#number of unique sample dates
grep -o "[0-9]*-\w*" ExampleAlignment.fasta| sort | uniq | wc -l  >> log.txt
