# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: Radmer van der Heyde
"""

# you may find it useful to import these variables (although you are not required to use them)
from amino_acids import aa, codons
from load import load_seq
dna = load_seq("./data/X73525.fa")

def collapse(L):
    """ Converts a list of strings to a string by concatenating all elements of the list """
    output = ""
    for s in L:
        output = output + s
    return output


def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment
    """
    amin =''
    for i in range(0,len(dna),3):
        cods = dna[i:i+3]
        
        for j in range(len(codons)):
            if cods in codons[j]:
                amin += aa[j]
    return amin
        
        
    # YOUR IMPLEMENTATION HERE

def coding_strand_to_AA_unit_tests():
    """ Unit tests for the coding_strand_to_AA function """
    inp = 'ATGCCCGCT'
    output = 'MPA'
    amin = coding_strand_to_AA(inp)
    print 'input:', inp,'expected ouput:',output, 'actual output:', amin 
    # YOUR IMPLEMENTATION HERE


def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    """
    string = ''
    for i in dna[::-1]:
        if i == 'A':
            string += 'T'
        elif i == 'T':
            string += 'A'
        elif i == 'C':
            string += 'G'
        elif i == 'G':
            string += 'C'
    return string
    # YOUR IMPLEMENTATION HERE
    
def get_reverse_complement_unit_tests():
    """ Unit tests for the get_complement function """
    inp = 'ATGCCCGCTTT'
    output = 'AAAGCGGGCAT'
    string = get_reverse_complement(inp)
    print 'input:', inp,'expected ouput:',output, 'actual output:', string
    # YOUR IMPLEMENTATION HERE    


def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string
    """
    codo = ''
    for i in range(0,len(dna),3):
        codo += dna[i:i+3]
        if codo[i:i+3] == 'TAG' or codo[i:i+3] == 'TAA' or codo[i:i+3] == 'TGA':
            return codo[:i]
    return codo
    # YOUR IMPLEMENTATION HERE

def rest_of_ORF_unit_tests():
    """ Unit tests for the rest_of_ORF function """
    inp = 'ATGAGATAGG'
    output = 'ATGAGA'
    codo = rest_of_ORF(inp)
    print 'input:', inp,'expected ouput:',output, 'actual output:', codo    
    # YOUR IMPLEMENTATION HERE
def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    i = 0
    ORFs = []
    while i < len(dna):
        if dna[i:i+3] == 'ATG': 
            n = rest_of_ORF(dna[i:])
            ORFs.append(n)
        i = i+3
    return ORFs
    # YOUR IMPLEMENTATION HERE        
     
def find_all_ORFs_oneframe_unit_tests():
    """ Unit tests for the find_all_ORFs_oneframe function """
    inp = 'ATGAGATAGGAAATGTTTTAG'
    output = 'ATGAGA','ATGTTT'
    codo = find_all_ORFs_oneframe(inp)
    print 'input:', inp,'expected ouput:',output, 'actual output:', codo
    # YOUR IMPLEMENTATION HERE

def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    ORF = []
    for i in range(3): 
        ORF.extend(find_all_ORFs_oneframe(dna[i:]))
    # YOUR IMPLEMENTATION HERE
    return ORF
def find_all_ORFs_unit_tests():
    """ Unit tests for the find_all_ORFs function """
    inp = 'ATGAATGAGATAGG'
    output = 'ATGATAAGA'
    codo = find_all_ORFs(inp)
    print 'input:', inp,'expected ouput:',output, 'actual output:', codo   
    # YOUR IMPLEMENTATION HERE

def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    ORF = []
    ORF.extend(find_all_ORFs(dna))
    rev = get_reverse_complement(dna)
    ORF.extend(find_all_ORFs(rev))
    return ORF
    # YOUR IMPLEMENTATION HERE

def find_all_ORFs_both_strands_unit_tests():
    """ Unit tests for the find_all_ORFs_both_strands function """
    inp = 'ATGAGATAGGCAT'
    output = ''
    codo = find_all_ORFs_both_strands(inp)
    print 'input:', inp,'expected ouput:',output, 'actual output:', codo
    # YOUR IMPLEMENTATION HERE


def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string"""
    ORF = find_all_ORFs_both_strands(dna)
    ORF.sort()
    return ORF[-1]
        
    # YOUR IMPLEMENTATION HERE

def longest_ORF_unit_tests():
    """ Unit tests for the longest_ORF function """
    inp = 'ATGAGATAGGCAT'
    output = ''
    codo = longest_ORF(inp)
    print 'input:', inp,'expected ouput:',output, 'actual output:', codo
    # YOUR IMPLEMENTATION HERE

def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """
    from random import shuffle
    ORF = []
    i = 0
    while i < num_trials:
        #print i, type(dna)
        dna = list(dna)
        shuffle(dna)
        dna = collapse(dna)
        f = longest_ORF(dna)
        ORF.append(f)
        i+=1
    print ORF
    ORF.sort()
    return ORF[-1]
    # YOUR IMPLEMENTATION HERE

def gene_finder(dna, threshold):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.
    """
    DNA = []
    PRO = []
    ORF = find_all_ORFs_both_strands(dna)
    for i in range(len(ORF)):
        if len(ORF[i]) > threshold:
            DNA.append(ORF[i])
    for i in range(len(DNA)):
        pro = coding_strand_to_AA(DNA[i])
        PRO.append(pro)
    return PRO

if __name__ =='__main__':
    threshold = longest_ORF_noncoding(dna,1500)
    t = len(threshold)
    pro = gene_finder(dna,t)
    print pro
    # YOUR IMPLEMENTATION HERE