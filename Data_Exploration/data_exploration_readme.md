# Data Exploration: Applying Data Processing Techniques on Arabic Corpus

For this assignment, I chose the creative prompt, exploring the corpus Camel Treebank, which includes 13 sub-corpora from a wide range of genres and time periods.

GitHub: https://github.com/Yi-ChyunWong/IDS570_Text_as_Data/tree/main/Data_Exploration

Paper: https://github.com/Yi-ChyunWong/IDS570_Text_as_Data/blob/main/Data_Exploration/data_exploration_final_writeup.pdf

## Corpus Chosen:  [CAMeL Treebank 1.1 by the CAMeL Lab at the New York University Abu Dhabi](https://sites.google.com/nyu.edu/camel-treebank/home?authuser=0)

The Camel Treebank is an open-source dependency treebank of Modern Standard Arabic (MSA) and Classical Arabic (CA) developed by CAMeL Lab. It spans a wide historical range (6th–21st century) and includes 13 sub-corpora covering genres from pre-Islamic poetry and Quranic scripture to novels, Bible translations, news, online commentary, and student essays.

### Documents / Sub-corpora:

Odes
- Variant: Classical Arabic (CA)
- Century: 6th
- Genre: Pre-Islamic Poetry
- Content: The ten celebrated Suspended Odes from pre-Islamic Arabia

Quran
- Variant: CA
- Century: 7th
- Genre: Quranic
- Content: First three and last fourteen surahs of the Quran

Hadith
- Variant: CA
- Century: 7th
- Genre: Prophetic sayings
- Content: First 134 hadith from Sahih Bukhari.

1001 (One Thousand and One Nights)
- Variant: CA
- Century: 12th
- Genre: Stories
- Content: Opening narrative and first eight nights of Arabian Nights

Hayy ibn Yaqdhan (Hayy)
- Variant: CA
- Century: 12th
- Genre: Philosophical novel
- Content: Full allegorical novel by Ibn Tufail

Old Testament (OT)
- Variant: Modern Standard Arabic (MSA)
- Century: 19th
- Genre: Bible translation
- Content: First 20 chapters of Genesis (Arabic translation)

New Testament (NT)
- Variant: MSA
- Century: 19th
- Genre: Bible translation
- Content: First 16 chapters of Matthew (Arabic translation)

Sara (Al-Akkad)
- Variant: MSA
- Century: 20th
- Genre: Novel
- Content: Full 1938 novel Sara by Abbas Mahmoud Al-Akkad

ALC (Arabic Learner Corpus)
- Variant: MSA
- Century: 21st
- Genre: Student essays (L2)
- Content: 20 essays written by second-language learners of Arabic

BTEC (Basic Traveling Expressions Corpus – MSA)
- Variant: MSA
- Century: 21st
- Genre: Phrasebook
- Content: Travel domain expressions translated into MSA

QALB
- Variant: MSA
- Century: 21st
- Genre: Online commentary
- Content: 200 online comments from Qatar Arabic Language Bank.

WikiNews
- Variant: MSA
- Century: 21st
- Genre: News
- Content: 70 Arabic WikiNews articles across multiple domains

ZAEBUC
- Variant: MSA
- Century: 21st
- Genre: Student essays (L1)
- Content: 100 native-speaker undergraduate essays from Zayed University

## Data Normalisation

The library that I used to preprocess the corpus is the [Stanford Stanza Python NLP Package](https://stanfordnlp.github.io/stanza/), specifically its Arabic toolkit. After downloading the files from a link provided by the CAMeL Lab, I transformed them into .txt files.For the TF-IDF and the Pairwise Pearson Correlation tasks, I lemmatised the text files so that the texts are not simply just tokenised by separating according to white space, but words with proclitics are properly separated, which are often used for prepositions or definite articles. I also removed diacritics used for pronunciations so that the spelling is consistent as the same word with and without diacritics are recognised separately.

Then, I got a list of Arabic stopwords from [NLTK](https://www.nltk.org/), and appended punctuations, including Arabic ones, to the list. I plot the top ten words in terms of frequency for each document with and without stopword removal. See GitHub for the [plots](https://github.com/Yi-ChyunWong/IDS570_Text_as_Data/tree/main/Data_Exploration/images).


## TF-IDF

![Top 10 Most Frequent Terms per Document](analysis_images\rawcount_top10.png)
Above: Top 10 Most Frequent Terms per Document

![Top 10 TF-IDF Terms per Document](analysis_images\tfidf_top10.png)
Above: Top 10 TF-IDF Terms per Document

### Do some documents share distinctive vocabulary?
As one would expect, the word “Allah” appears a lot in some documents, but not the others. The word “Allah” is used a lot in daily expressions, and sometimes the Basmalah is included in the opening of chapters. (“Allah” is represented as a white box in the charts above due to rendering issues) “Allah appeared as the top 10 words in terms of frequency in these documents: 1001, ALC, Hadith, OT, QALB. They continue to appear in 1001, ALC, and QALB. I think this is expected as the word “Allah” is common for religious texts (e.g. Hadith, Old Testament) and daily expressions (e.g. QALB, ALC), but might not be as common in others like novels, news, and traveling expression guides. The interesting case here is 1001, which I believe has a lot of mention of God in the introduction, and therefore has a large word count for “Allah.”

### Are distinctive terms topical, rhetorical, or technical? Are there documents whose distinctiveness” seems driven by noise or formatting rather than content?
Since the corpus is composed of documents of various genres, the distinctive terms are topical. One example that I really found interesting is that the word for “Noah” is number 8 on the TF-IDF score for the Old Testament. However, for other documents, and more so the religious text, I can see that some words that may seem like definite articles or other short stopwords have been kept in the list of lemmas, which made it into the top 10 rankings for their respective documents. I believe this is because the stopword list does not remove the glottal stop letter, which would mean that these would be extra words that should be considered to be removed.

## Pairwise Pearson Correlation

[Document-Feature Matrix](https://github.com/Yi-ChyunWong/IDS570_Text_as_Data/blob/main/Data_Exploration/document_feature_matrix.csv)

![Pairwise Pearson Correlations Between Documents](analysis_images\pearson_heatmap.png)
Above: Pairwise Pearson Correlations Between Documents

### Two most similar document pairs (excluding WikiNews):
NT and OT (score: 0.7): this is expected as the New Testament and the Old Testament share similar themes and the translations were also done at around the same time period.
Quran and Odes (score: 0.65): this is also expected as the Quran and the Odes use classical Arabic and thus the vocabulary used in both documents may be similar.
It is concerning that WikiNews has strong correlation with religious and older texts (NT, Odes, OT, Quran). An explanation for this is that the WikiNews may contain entries related to older Arabic literature, and therefore sharing higher similarities with these documents.


### Dissimilar document pairs:
BTEC vs Quran, OT, Odes, NT, Hadith: we would expect that a traveling expression guide not having much in common with religious texts, which is reflected by the low scores (<=0.03).
ZAEBUC vs Quran, OT, Odes, NT, Hadith: we would also expect academic writing from native speakers to not have much in common with religious texts, and the correlation scores are even lower compared to BTEC’s comparisons (<=0.01).

## Foreign Words

I decided to take a look at the number of foreign words in each document of the corpus using Stanza’s dependency parsing, which also identifies foreign words. This can be used for a baseline measurement for my final project, in which I would also be looking into ways to identify foreign words using the roots of each word (or the lack thereof).

There is less cleanup of the data required in this task as the Stanza tool used for dependency parsing requires context, and therefore stopwords were not removed. I removed the diacritics to keep spelling consistent.

![Top Foreign Words per Document](analysis_images\foreign_words.png)
Above: Top Foreign Words per Document

### Findings
As expected, more modern documents such as WikiNews, BTEC, ALC, and QALB would have foreign words in the text, whereas older documents (except for the Quran), it is expected that they do not have foreign words. In the Quran, the word for Pharaoh is identified by Stanza’s dependency parsing tool as a foreign word. For the other documents, most of the foreign words identified were names of places and people, such as “San Francisco” (in BTEC) and “Michael Jackson” (in WikiNews).

## Synthesis

### Research Question: How could foreign words be identified based on the roots?
For this particular research question, I would want to use the dependency parsing tool to identify foreign words in a document, and use that as a baseline of my method’s performance, and could also serve as an automatic labeling system for supervised training. TF-IDF and Pearson correlation may have an auxiliary role in identifying the genre or the time period of the documents that we examine, which can inform us on how likely they would contain foreign words. For example, given a document without any context, if we find that the document has a high similarity with older texts such as the Quran or the Odes, it is more likely that the document in question would not have foreign words. In other words, while the main detection method for foreign words that we want to develop looks at the roots of the words, the extra context we get using TF-IDF or Pearson correlation may provide useful insight (i.e. some weights in our regression process) that could better predict if a word is foreign.
