#main script
bash lines_dates.sh
python3 dna_protein.py
python3 varSites.py >> log.txt
python3 mkfiles.py
