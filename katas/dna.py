# Codewars kata: https://www.codewars.com/kata/dna-to-rna-conversion/train/python

def DNAtoRNA(dna: str) -> str:

    """ Translate a given Deoxyribonucleic acid (DNA) to Ribonucleic acid (RNA) """
    input = list(dna)
    store = ["U" if x == "T" else x for x in input]
    output = ''.join(store)
    caps = output.upper()
    return caps

DNAtoRNA("Time")
