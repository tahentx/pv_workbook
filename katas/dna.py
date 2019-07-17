# Codewars kata: https://www.codewars.com/kata/dna-to-rna-conversion/train/python

def DNAtoRNA(dna: str) -> str:

    """ Translate a given Deoxyribonucleic acid (DNA) to Ribonucleic acid (RNA) """
    input = list(dna)
    for x in input:
        print(x)
        if x == "T":
            print("U")
    # rna = ["U" for i in input if i == "T"]
    # print(rna)
DNAtoRNA("Time")
