import RNAPy.RNAPy_AA as aa


class RNA:

    def translate(self, rna_str):
        result = aa.RNAPy_AA_List()
        result._clear()

        rna_str = rna_str.upper()
        start_idx = rna_str.find("AUG")

        # No Start Codon
        if start_idx == -1:
            return None

        triplets = [rna_str[i:i + 3] for i in range(start_idx, len(rna_str), 3)]

        for triplet in triplets:
            if aa._codon_to_3letter.get(triplet, "X") == "EXIT":
                return result
            else:
                result._append(aa.RNAPy_AA(aa._codon_to_3letter[triplet]))

        return result


if __name__ == "__main__":
    #import RNAPy

    print(RNA().translate("GGGGGGGGGGGGGG"))
