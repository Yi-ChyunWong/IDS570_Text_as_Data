================================================================

	                  Camel Treebank

                           Release v1.1
                           20 June 2022

=================================================================
Summary
=================================================================

The Camel Treebank (CamelTB) is an open-source dependency treebank of Modern Standard and Classical Arabic. 
CamelTB 1.0 includes 13 sub-corpora (188K words) comprising selections of texts from pre-Islamic poetry to social media online commentaries, and covering a range of genres from religious and philosophical texts to news, novels, and student essays. The texts are all publicly available (out of copyright, creative commons, or under open licenses). The texts were morphologically tokenized and syntactically parsed automatically, and then manually corrected by a team of trained annotators. The annotations follow the guidelines of the Columbia Arabic Treebank (CATiB) dependency representation. We discuss our annotation process and guideline extensions, and we present some initial observations on lexical and syntactic differences among the annotated sub-corpora. This corpus is publicly available to support and encourage research on Arabic NLP in general and on new, previously unexplored genres that are of interest to a wider spectrum of researchers, from historical linguistics and digital humanities to computer-assisted language pedagogy.

More details on this project can be found in Habash et al (2022):
Habash, Nizar, Muhammed AbuOdeh, Dima Taji, Reem Faraj, Jamila El Gizuli, and Omar Kallas. 2022. Camel Treebank: An Open Multi-genre Arabic Dependency Treebank. In Proceedings of the Language Resources and Evaluation Conference (LREC). Marseille, France.


@inproceedings{Habash:2022:cameltb,
    title = "{Camel~Treebank}: An Open Multi-genre {A}rabic Dependency Treebank",
    author = " Nizar Habash and Muhammed AbuOdeh and Dima Taji and Reem Faraj and Jamila El Gizuli and Omar Kallas",
    booktitle = "Proceedings of the Language Resources and Evaluation Conference (LREC)",
    year = "2022", 
    address = "Marseille, France"
}

=================================================================
Description of Data
=================================================================
README.txt  :   This file.

LICENSE.txt :   The license to use this corpus.

LREC2022_CamelTB.pdf :
                A paper describing the creation and use of the corpus.

data :	Contains data from 13 subcorpora, in 3 formats (plus a split file) for each subcorpora:
    annotated:	the CoNLL-X files.
    raw:		the original, unsegmented text files.
    sent:		the manually segmented sentences.
    splits:		tsv files for each subcorpus with recommended splits.


=================================================================
Other notes
=================================================================
The text lines of some subcorpora were whitespace tokenized while others were not. In the paper we report the word count on whitespace tokenization.


================================================================
References
================================================================
Habash, Nizar, Muhammed AbuOdeh, Dima Taji, Reem Faraj, Jamila El Gizuli, and Omar Kallas. 2022. Camel Treebank: An Open Multi-genre Arabic Dependency Treebank. In Proceedings of the Language Resources and Evaluation Conference (LREC). Marseille, France.

================================================================
Copyright (c) 2022 New York University Abu Dhabi. All rights reserved.
================================================================
