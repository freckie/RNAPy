# Variables
_codon_to_3letter = {
     'UUU': 'Phe', 'UUC': 'Phe', 'UUA': 'Leu', 'UUG': 'Leu',
     'UCU': 'Ser', 'UCC': 'Ser', 'UCA': 'Ser', 'UCG': 'Ser',
     'UAU': 'Tyr', 'UAC': 'Tyr', 'UAA': 'EXIT', 'UAG': 'EXIT',
     'UGU': 'Sys', 'UGC': 'Sys', 'UGA': 'EXIT', 'UGG': 'Trp',
     'CUU': 'Leu', 'CUC': 'Leu', 'CUA': 'Leu', 'CUG': 'Leu',
     'CCU': 'Pro', 'CCC': 'Pro', 'CCA': 'Pro', 'CCG': 'Pro',
     'CAU': 'Hys', 'CAC': 'Hys', 'CAA': 'Gln', 'CAG': 'Gln',
     'CGU': 'Arg', 'CGC': 'Arg', 'CGA': 'Arg', 'CGG': 'Arg',
     'AUU': 'Isr', 'AUC': 'Isr', 'AUA': 'Isr', 'AUG': 'Met',
     'ACU': 'Thr', 'ACC': 'Thr', 'ACA': 'Thr', 'ACG': 'Thr',
     'AAU': 'Asn', 'AAC': 'Asn', 'AAA': 'Lys', 'AAG': 'Lys',
     'AGU': 'Ser', 'AGC': 'Ser', 'AGA': 'Arg', 'AGG': 'Arg',
     'GUU': 'Val', 'GUC': 'Val', 'GUA': 'Val', 'GUG': 'Val',
     'GCU': 'Ala', 'GCC': 'Ala', 'GCA': 'Ala', 'GCG': 'Ala',
     'GAU': 'Asp', 'GAC': 'Asp', 'GAA': 'Glu', 'GAG': 'Glu',
     'GGU': 'Gly', 'GGC': 'Gly', 'GGA': 'Gly', 'GGG': 'Gly'
}
_3letter_to_1letter = {
    'Ala':'A', 'Arg':'R', 'Asn':'N', 'Asp':'D',
    'Cys':'C', 'Glu':'E', 'Gln':'Q', 'Gly':'G',
    'His':'H', 'Ile':'I', 'Leu':'L', 'Lys':'K',
    'Met':'M', 'Phe':'F', 'Pro':'P', 'Ser':'S',
    'Thr':'T', 'Trp':'W', 'Tyr':'Y', 'Val':'V'
}
_3letter_to_name = {
    'Ala':'Alaine', 'Arg':'Arginine', 'Asn':'Asparagine', 'Asp':'Aspartic Acid',
    'Cys':'Cysteine', 'Glu':'Glutamic Acid', 'Gln':'Glutamine', 'Gly':'Glycine',
    'His':'Histidine', 'Ile':'Isoleucine', 'Leu':'Leucine', 'Lys':'Lysine',
    'Met':'Methionine', 'Phe':'Phenylalanine', 'Pro':'Proline', 'Ser':'Serine',
    'Thr':'Threonine', 'Trp':'Tryptophan', 'Tyr':'Tyrosine', 'Val':'Valine'
}


class RNAPy_AA:
    _3letter = ""

    def __init__(self, aa_3let):
        self._3letter = aa_3let

    def __str__(self):
        return self._3letter

    def to_1letter(self):
        return _3letter_to_1letter[self._3letter]

    def to_name(self):
        return _3letter_to_name[self._3letter]


class RNAPy_AA_List:

    _aa_list = []
    _length = 0
    _position = 0

    def __init__(self):
        self._length = 0

    def __len__(self):
        return self._length

    def __iter__(self):
        self._position = 0
        return self

    def __next__(self):
        if self._position >= len(self._aa_list):
            raise StopIteration

        result = self._aa_list[self._position]
        self._position += 1

        return result

    ''' [Protected Function] '''

    # Append AA to List
    def _append(self, aa_3let):
        self._aa_list.append(RNAPy_AA(aa_3let))
        self._length += 1

    ''' [Public Function] '''

    def to_list(self, mode="3letter"):
        _result_list = []

        for aa in self._aa_list:
            if mode == "3letter":
                _result_list.append(aa.__str__())
            elif mode == "1letter":
                _result_list.append(aa.to_1letter())
            elif mode == "name":
                _result_list.append(aa.to_name())
            else:
                raise RuntimeError("RNAPy_AA_List.to_list() : Invalid Parameter 'mode'")

        return _result_list

    def print(self, mode="3letter"):
        if mode == "3letter" or mode == "1letter" or mode == "name":
            print("-".join(self.to_list(mode)))

        else:
            raise RuntimeError("RNAPy_AA_List.print() : Invalid Parameter 'mode'")

    def length(self):
        return self._length




if __name__ == "__main__":
    r = RNAPy_AA_List()
    r._append("Met")
    r._append("Met")
    r._append("Ala")
    for hey in r:
        print(hey)
    r.print()
    hi = r.to_list()
    print(hi)
    print(r)