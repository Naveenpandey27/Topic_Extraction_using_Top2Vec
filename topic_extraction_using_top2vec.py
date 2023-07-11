# -*- coding: utf-8 -*-
"""Topic_Extraction_using_Top2Vec.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zBrJOXmirDpkDdkMR79Z89uUXCjRYvpy
"""

# Install top2vec package
!pip install top2vec[sentence_encoders]

import numpy as np
import pandas as pd
from top2vec import Top2Vec
from sklearn.datasets import fetch_20newsgroups

# Fetch 20 newsgroups dataset
news_group = fetch_20newsgroups(subset='all', remove=('headers', 'footers', 'quotes'))

# Training a Top2Vec Model
model = Top2Vec(news_group.data, workers=4, embedding_model='universal-sentence-encoder')

# Get the number of topics in the model
model.get_num_topics()

# Get the sizes of each topic
topic_sizes, topic_nums = model.get_topic_sizes()

# Print the sizes of each topic
topic_sizes

# Print the topic numbers
topic_nums

# Get the keywords for each topic
model.topic_words

# Get the topic words, word scores, and topic numbers for a specific topic
topic_words, word_scores, topic_nums = model.get_topics(77)
for words, scores, nums in zip(topic_words, word_scores, topic_nums):
    print('Topic Numbers:', nums)
    print('Words:', words)

# Generate word clouds for specific topics
model.generate_topic_wordcloud(0)
model.generate_topic_wordcloud(5)

# Search for topics related to specific keywords and get the topic words and scores
topic_words, word_scores, topic_scores, topic_nums = model.search_topics(keywords=['Politics'], num_topics=3)
topic_words, topic_scores

# Search documents related to a specific topic and get the document texts, scores, and IDs
documents, document_scores, document_ids = model.search_documents_by_topic(topic_num=0, num_docs=5)
for doc, score, doc_id in zip(documents, document_scores, document_ids):
    print(f"Document: {doc_id}, Score: {score}")
    print("-----------")
    print(doc)
    print("-----------")
    print()

# Perform hierarchical topic reduction and get the reduced topic mapping
topic_mapping = model.hierarchical_topic_reduction(num_topics=20)
topic_mapping[1]

# Get the reduced topic words for a specific topic
model.topic_words_reduced[0]