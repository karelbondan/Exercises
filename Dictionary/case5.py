def kmer_initialize(DNA, k):
    kmerlist = []
    kmerstr = ''
    index = 0
    for j in range(0, len(DNA)):
        for i in DNA[index:]:
            kmerstr = kmerstr + i
            if len(kmerstr) == k:
                break
        kmerlist.append(kmerstr)
        kmerstr = ''
        index += 1
        for item in kmerlist:
            if len(item) != k:
                kmerlist.remove(item)
    return kmer_count(kmerlist)

def kmer_count(list):
    kcount = {}
    for item in list:
        kcount.setdefault(item, 0)
        kcount[item] = kcount[item] + 1
    return kcount

print(kmer_initialize("GATGAT", 3))
print(kmer_initialize("GTAGAGCTGT", 9))