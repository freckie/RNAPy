# RNAPy

RNAPy Supports Translation 'RNA Codon String' to 'Amino Acid List'

<hr />

## 0. Import RNAPy
install /dist/~.whl file with pip.
from RNAPy import RNA

<hr />

## 1. RNAPy

<hr />

### 1.1 RNA Class


* function translate(rna_str) 
	* Translate 'RNA Codon' to 'Amino Acid List'
	* rna_str : string
	* return : RNAPy_AA_List object

<hr />

### 1.2 RNAPy_AA_List Class

List of RNAPy_AA Objects.
This object is iterable object.

* function to_list(mode="3letter")
	* Return a python list.
	* mode : "3letter" or "1letter" or "name"
		* mode="3letter" (default) : ex) ['Met', 'Val', 'Leu', 'Lys']
		* mode="1letter" : ex) ['M', 'V', 'L', 'K']
		* mode="name" : ex) ['Methionine, 'Valine', 'Leucine', 'Lysine']
	* return : list

* function print(mode="3letter")
	* Print Amino-Acid on console. 
	* mode : "3letter" or "1letter" or "name"
		* mode="3letter" (default) : ex) Met-Val-Leu-Lys
		* mode="1letter" : ex) M-V-L-K
		* mode="name" : ex) Methionine-Valine-Leucine-Lysine
	* return : None

* function length()
	* Return length.
	* return : int

* function at(index)
	* Return RNAPy_AA Object of index.
	* index : int
	* return : RNAPy_AA

* function count(aa_3let)
	* Count Amino Acids.
	* aa_3let : Amino Acid(3letter) which you want to count. ex) "Met"
	* return : int

* function find(aa_3let)
	* Find only one Amino Acid, search starts at first.
	* aa_3let : Amino Acid(3letter) which you want to find. ex) "Met"
	* return 
		* int : when AA exists.
		* bool (false) : when AA doesn't exist.

* function find_all(aa_3let)
	* Find Index of Amino Acid.
	* aa_3let : Amino Acid(3letter) which you want to find. ex) "Met"\
	* return : list(int)


<hr />

### 1.3 RNAPy_AA Class

Amino Acid Object.

* function _get_3let()
	* Get 3letter as string.
	* return : string

* function to_1letter()
	* Get 1letter as string.
	* return : string

* functino to_name()
	* Get name as string.
	* return : string

<hr />

## 2. Example

<pre><code>
import RNAPy

codon = "AAAUGAACUUUAGAGGAAUUAUAGAGAGU"

rp = RNAPy.RNA()
print(rp.translate(codon))

---

>> Met-Asn-Phe-Arg-Gly-Isr-Isr-Glu-Ser
</code></pre>

