#Read in Libraries and Texts----
library(tibble)
library(dplyr)
library(readr)
library(ggplot2)
library(quanteda)
library(quanteda.textstats)
library(tidyr)
library(stringr)
library(tidytext)
library(forcats)

txt_circle    <- read_file("texts/A07594__Circle_of_Commerce.txt")
txt_free      <- read_file("texts/B14801__Free_Trade.txt")

texts <- tibble(
  doc_title = c("Circle of Commerce", "Free Trade"),
  text = c(txt_circle, txt_free)
)
#Step 1: Tokenize and Clean Text----
#Week3 Normalisation
texts <- texts %>%
  mutate(
    text_norm = text %>%
      str_replace_all("ſ", "s") %>%   # long s as above
      str_replace_all("\\s+", " ") %>% # collapse whitespace
      str_to_lower()
  )
texts

#Week4 Stopwords
# Start with tidytext's built-in stopword list
data("stop_words")

# Add our own project-specific stopwords (you can, and will, expand this list later)
custom_stopwords <- tibble(
  word = c(
    "vnto","haue","doo","hath","bee","ye","thee","hee","shall","hast","doe",
    "beene","thereof","thus"
  )
)

all_stopwords <- bind_rows(stop_words, custom_stopwords) %>%
  distinct(word)

# Word count across documents
word_counts <- texts %>%
  unnest_tokens(word, text_norm) %>%
  mutate(word = str_to_lower(word)) %>%
  anti_join(all_stopwords, by = "word") %>%
  count(doc_title, word, sort = TRUE)

word_counts

# Word count after stopword removal
doc_lengths <- word_counts %>%
  group_by(doc_title) %>%
  summarise(total_words = sum(n))

doc_lengths

#Step 2: Join Tokens to the Bing Sentiment Dictionary----
bing <- get_sentiments("bing")
sent_tokens <- word_counts %>%
  inner_join(bing, by = "word")

sent_tokens

#Step 3: Compute Raw Sentiment Totals----
raw_sent <- sent_tokens %>%
  pivot_wider(names_from = sentiment, values_from = n, values_fill = 0) %>%
  group_by(doc_title) %>%
  summarise(
    total_positive = sum(positive),
    total_negative = sum(negative),
    total_net_sentiment = total_positive-total_negative
  )

raw_sent

#Step 4: Compute TF-IDF for Words in Each Document----
tf_idf <- word_counts %>%
  bind_tf_idf(term = word, document = doc_title, n = n)

tf_idf

#Step 5: Keep Only Sentiment-bearing Words----
tf_idf_sent_tokens <- tf_idf %>%
  inner_join(bing, by = "word")
tf_idf_sent_tokens

#Step 6: Compute TF-IDF–weighted Sentiment Totals----
tf_idf_sent <- tf_idf_sent_tokens %>%
  group_by(doc_title) %>%
  summarise(
    tfidf_positive = sum(tf_idf[sentiment == "positive"], na.rm = TRUE),
    tfidf_negative = sum(tf_idf[sentiment == "negative"], na.rm = TRUE),
    .groups = "drop"
  ) %>%
  mutate(
    net_sentiment_tfidf = tfidf_positive - tfidf_negative
  )
tf_idf_sent

#Step 7: Compare Raw vs. TF-IDF Sentiment
raw_vs_tf_idf <- raw_sent %>%
  left_join(tf_idf_sent)
raw_vs_tf_idf
write.csv(raw_vs_tf_idf, "tables/raw_vs_tf_idf.csv")

#Rank TF_IDF Influences
tf_free_neg <- tf_idf_sent_tokens %>%
  filter(doc_title == "Free Trade",
         sentiment == "negative") %>%
  arrange(desc(tf_idf))
tf_free_neg

tf_free_pos <- tf_idf_sent_tokens %>%
  filter(doc_title == "Free Trade",
         sentiment == "positive") %>%
  arrange(desc(tf_idf))
tf_free_pos

tf_circle_neg <- tf_idf_sent_tokens %>%
  filter(doc_title == "Circle of Commerce",
         sentiment == "negative") %>%
  arrange(desc(tf_idf))
tf_circle_neg

tf_circle_pos <- tf_idf_sent_tokens %>%
  filter(doc_title == "Circle of Commerce",
         sentiment == "positive") %>%
  arrange(desc(tf_idf))
tf_circle_pos
