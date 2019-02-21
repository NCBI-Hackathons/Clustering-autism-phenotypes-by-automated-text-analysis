from Bio import Entrez
from Bio import SeqIO

# retrieve and display data from PubMed

Entrez.email = "shussainather@gmail.com"
db = "gene"
term = "autism"
h_search = Entrez.esearch(db=db, email=Entrez.email, term=term)
record = Entrez.read(h_search)
res_ids = record["IdList"]
for r_id in res_ids:
    h_summ = Entrez.esummary(db=db, id=r_id, email=Entrez.email) # summary as retrieved by Entrez
    summ = Entrez.read(h_summ) # summary of the text
    print(r_id)
    print(summ)
    print("==============================================")


