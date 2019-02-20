from ftplib import FTP
from io import StringIO
import gzip
import os

ftp = FTP("ftp.ncbi.nlm.nih.gov")
ftp.login() # Username: anonymous password: anonymous@

filenames = ftp.nlst("ftp://ftp.ncbi.nlm.nih.go/pubmed/baseline/") # get filenames within the directory
print(filenames)

for filename in filenames:
    local_filename = os.path.join("ftp://ftp.ncbi.nlm.nih.gov", filename)
    file = open(local_filename, 'wb')

    file.close()

ftp.quit()
