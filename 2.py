# SOAL 2 - REKOMENDASI BUKU

import numpy as np
import pandas as pd

df = pd.read_csv('books.csv')
df1 = pd.read_csv('ratings.csv')
df = df.rename(columns={'book_id': 'book_id_df'})
df1 = df1.rename(columns={'book_id':'book_id_df1'})

dfAll = pd.concat([df, df1], axis=1)
dfAll = dfAll.dropna(subset = ['book_id_df', 'goodreads_book_id', 'best_book_id', 'work_id',
       'books_count', 'isbn', 'isbn13', 'authors', 'original_publication_year',
       'original_title', 'title', 'language_code', 'average_rating',
       'ratings_count', 'work_ratings_count', 'work_text_reviews_count',
       'ratings_1', 'ratings_2', 'ratings_3', 'ratings_4', 'ratings_5',
       'image_url', 'small_image_url', 'user_id', 'book_id_df1', 'rating'])

# ============================================ DATAFRAME ==========================================================================================

dfBook = dfAll[['user_id', 'original_title', 'rating']]

def mergeCol(a):
    return str(a['original_title']) + ' ' + str(a['rating'])

dfBook['features'] = dfBook.apply(mergeCol, axis = 1)

# ============================================ CONTENT BASED FILTERING: 'RATING' (MULTIPLEFEATURES) ==========================================================================================
from sklearn.feature_extraction.text import CountVectorizer
model = CountVectorizer(
    tokenizer= lambda i: i.split(' '),
    analyzer= 'word'
)

matrixfeatures = model.fit_transform(dfBook['features'])
features = model.get_feature_names()
eventfeature = matrixfeatures.toarray()
jmlfeature = len(features)

# # ===================================================== COSINUS SIMILARITY ==========================================================================================

from sklearn.metrics.pairwise import cosine_similarity

score = cosine_similarity(matrixfeatures)

# # ===================================================== TEST MODEL ==========================================================================================

# # ======================================================== ANDI

# NOTE: HANYA MENGINPUT RATING SALAH SATU BUKU RATING 5 STAR


sukabuku = 'The Hunger Games'
indexsuka = dfBook[dfBook['original_title'] == sukabuku].index.values[0]

allBook = list(enumerate(score[indexsuka]))

bukusama = sorted(
    allBook,
    key = lambda x: x[1],
    reverse = True
)

bukusama60up = []
for x in bukusama:
    if x[1] > 0.6:
        bukusama60up.append(x)

import random
rek = random.choices(bukusama60up, k=5)

print('Buku bagus untuk Andi: ')
for y in rek:
    rekbuku = dfBook.iloc[y[0]].values
    print('-', rekbuku[1])

print('=========================================================================')

# ======================================================== BUDI

# NOTE: HANYA MENGINPUT RATING SALAH SATU BUKU RATING 5 STAR

sukabuku1 = "Harry Potter and the Philosopher's Stone"
indexsuka1 = dfBook[dfBook['original_title'] == sukabuku1].index.values[0]

allBook1 = list(enumerate(score[indexsuka1]))

bukusama1 = sorted(
    allBook1,
    key = lambda x: x[1],
    reverse = True
)

bukusama60up1 = []
for x in bukusama1:
    if x[1] > 0.6:
        bukusama60up1.append(x)

import random
rek1 = random.choices(bukusama60up1, k=5)

print('Buku bagus untuk Budi: ')
for y in rek1:
    rekbuku1 = dfBook.iloc[y[0]].values
    print('-', rekbuku1[1])

print('=========================================================================')

# ======================================================== CIKO

# NOTE: HANYA MENGINPUT RATING SALAH SATU BUKU RATING 5 STAR

sukabuku2 = "Robots and Empire"
indexsuka2 = dfBook[dfBook['original_title'] == sukabuku2].index.values[0]

allBook2 = list(enumerate(score[indexsuka2]))

bukusama2 = sorted(
    allBook2,
    key = lambda x: x[1],
    reverse = True
)

bukusama60up2 = []
for x in bukusama2:
    if x[1] > 0.6:
        bukusama60up2.append(x)

import random
rek2 = random.choices(bukusama60up2, k=5)

print('Buku bagus untuk Ciko: ')
for y in rek2:
    rekbuku2 = dfBook.iloc[y[0]].values
    print('-', rekbuku2[1])

print('=========================================================================')

# ======================================================== DEDI

# NOTE: HANYA MENGINPUT RATING SALAH SATU BUKU RATING 5 STAR

sukabuku3 = "A History of God: The 4,000-Year Quest of Judaism, Christianity, and Islam"
indexsuka3 = dfBook[dfBook['original_title'] == sukabuku3].index.values[0]

allBook3 = list(enumerate(score[indexsuka3]))

bukusama3 = sorted(
    allBook3,
    key = lambda x: x[1],
    reverse = True
)

bukusama60up3 = []
for x in bukusama3:
    if x[1] > 0.6:
        bukusama60up3.append(x)

import random
rek3 = random.choices(bukusama60up3, k=5)

print('Buku bagus untuk Ciko: ')
for y in rek3:
    rekbuku3 = dfBook.iloc[y[0]].values
    print('-', rekbuku3[1])

print('=========================================================================')

# ======================================================== ELLO

# NOTE: HANYA MENGINPUT RATING SALAH SATU BUKU RATING 4 STAR

sukabuku4 = "Doctor Sleep"
indexsuka4 = dfBook[dfBook['original_title'] == sukabuku4].index.values[0]

allBook4 = list(enumerate(score[indexsuka4]))

bukusama4 = sorted(
    allBook4,
    key = lambda x: x[1],
    reverse = True
)

bukusama60up4 = []
for x in bukusama4:
    if x[1] > 0.6:
        bukusama60up4.append(x)

import random
rek4 = random.choices(bukusama60up4, k=5)

print('Buku bagus untuk Ello: ')
for y in rek4:
    rekbuku4 = dfBook.iloc[y[0]].values
    print('-', rekbuku4[1])

print('=========================================================================')

