import alignment

for i in range(10000):
    score = alignment.py_local(b"ACTGAGAGATAGAGTCAGCTACGTCGATCGACTAGCTACGATCGACTGAGAGATAGAGTCAGCTACG", 
                            b"ACGCTAGCATCGATCGATCGATCGATCGATCAGTCAGCTACGATCGATCGATCGCTGCTAGCTACGATCGA")
    print(i)
print(score)