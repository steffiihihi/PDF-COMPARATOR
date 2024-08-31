import hashlib

def hash_file(fileName1, fileName2): 

    h1 = hashlib.sha1() 
    h2 = hashlib.sha1() 

    with open(fileName1, "rb") as file: 
        chunk = 0
        while chunk != b'': 
            chunk = file.read(1024) 
            h1.update(chunk) 
            
    with open(fileName2, "rb") as file: 
        chunk = 0
        while chunk != b'': 
            chunk = file.read(1024) 
            h2.update(chunk) 

    return h1.hexdigest(), h2.hexdigest() 

# Relative paths to your PDFs
pdf1_path = "PDF-COMPARATOR/utilities/BDT5.pdf"
pdf2_path = "PDF-COMPARATOR/utilities/DBMS2.pdf"

msg1, msg2 = hash_file(pdf1_path, pdf2_path) 

if msg1 != msg2: 
    print("These files are not identical") 
else: 
    print("These files are identical")
