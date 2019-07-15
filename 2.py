# SOAL 2 - REKOMENDASI BUKU

import pandas as pd

# ============================================= DATAFRAME =================================================================================

dfBooks = pd.read_csv('books.csv')
dfRatings = pd.read_csv('ratings.csv')

def mergeCol(a):
    return str(a['authors'])+' '+str(a['original_title'])+' '+str(a['language_code'])
dfBooks['features'] = dfBooks.apply(mergeCol,axis=1)

# ============================================= COUNT VECTORIZER =================================================================================

from sklearn.feature_extraction.text import CountVectorizer
model = CountVectorizer(tokenizer=lambda i: i.split(' '))
matrixfeatures = model.fit_transform(dfBooks['features'])

features = model.get_feature_names()
jmlfeatures = len(features)

# ============================================= COSINE SIMILARITY =================================================================================

from sklearn.metrics.pairwise import cosine_similarity
skor = cosine_similarity(matrixfeatures)

# NOTE : ONLY INPUTTING BOOK RATING WITH 5 STARS REVIEW
andi1 = dfBooks[dfBooks['original_title']=='The Hunger Games']['book_id'].tolist()[0]-1 
andi2 = dfBooks[dfBooks['original_title']=='Catching Fire']['book_id'].tolist()[0]-1 
andisuka = [andi1,andi2]

budi1 = dfBooks[dfBooks['original_title']=='Harry Potter and the Philosopher\'s Stone']['book_id'].tolist()[0]-1 
budi2 = dfBooks[dfBooks['original_title']=='Harry Potter and the Chamber of Secrets']['book_id'].tolist()[0]-1 
budi3 = dfBooks[dfBooks['original_title']=='Harry Potter and the Prisoner of Azkaban']['book_id'].tolist()[0]-1 
budisuka = [budi1,budi2,budi3]

ciko1 = dfBooks[dfBooks['original_title']=='Robots and Empire']['book_id'].tolist()[0]-1 
cikosuka = [ciko1]

dedi1 = dfBooks[dfBooks['original_title']=='A History of God: The 4,000-Year Quest of Judaism, Christianity, and Islam']['book_id'].tolist()[0]-1 
dedisuka = [dedi1]

ello1 = dfBooks[dfBooks['original_title']=='The Story of Doctor Dolittle']['book_id'].tolist()[0]-1 
ello2 = dfBooks[dfBooks['title']=='Bridget Jones\'s Diary (Bridget Jones, #1)']['book_id'].tolist()[0]-1 
ellosuka = [ello1,ello2]

skorandi1 = list(enumerate(skor[andi1]))
skorandi2 = list(enumerate(skor[andi2]))

skorbudi1 = list(enumerate(skor[budi1]))
skorbudi2 = list(enumerate(skor[budi2]))
skorbudi3 = list(enumerate(skor[budi3]))

skorciko1 = list(enumerate(skor[ciko1]))

skordedi1 = list(enumerate(skor[dedi1]))

skorello1 = list(enumerate(skor[ello1]))
skorello2 = list(enumerate(skor[ello2]))

listskorandi = []
for i in skorandi1:
    listskorandi.append((i[0],(skorandi1[i[0]][1]+skorandi2[i[0]][1])/2))
listskorbudi = []
for i in skorandi1:
    listskorbudi.append((i[0],(skorbudi1[i[0]][1]+skorbudi2[i[0]][1]+skorbudi3[i[0]][1])/3))
listskorello = []
for i in skorandi1:
    listskorello.append((i[0],(skorello1[i[0]][1]+skorello2[i[0]][1])/2))

sortandi = sorted(listskorandi, key=lambda j:j[1], reverse=True)
sortbudi = sorted(listskorbudi, key = lambda j:j[1], reverse = True)
sortciko = sorted(skorciko1, key = lambda j:j[1], reverse = True)
sortdedi = sorted(skordedi1, key = lambda j:j[1], reverse = True)
sortello = sorted(listskorello, key = lambda j:j[1], reverse = True)

# ============================================= TOP 5 RECOMMENDATION =================================================================================

similarandi = []
for i in sortandi:
    if i[1]>0:
        similarandi.append(i)
similarbudi = []
for i in sortbudi:
    if i[1]>0:
        similarbudi.append(i)
similarciko = []
for i in sortciko:
    if i[1]>0:
        similarciko.append(i)
similardedi = []
for i in sortdedi:
    if i[1]>0:
        similardedi.append(i)
similarello = []
for i in sortello:
    if i[1]>0:
        similarello.append(i)

print('Buku bagus untuk Andi:')
for i in range(0,5):
    if similarandi[i][0] not in andisuka:
        print('-',dfBooks['original_title'].iloc[similarandi[i][0]])
    else:
        i+=5
        print('-',dfBooks['original_title'].iloc[similarandi[i][0]])

print('============================================================================')
print('Buku bagus untuk Budi:')
for i in range(0,5):
    if similarbudi[i][0] not in budisuka:
        print('-',dfBooks['original_title'].iloc[similarbudi[i][0]])
    else:
        i+=5
        print('-',dfBooks['original_title'].iloc[similarbudi[i][0]])

print('============================================================================')
print('Buku bagus untuk Ciko:')
for i in range(0,5):
    if similarciko[i][0] not in cikosuka:
        print('-',dfBooks['original_title'].iloc[similarciko[i][0]])
    else:
        i+=5
        print('-',dfBooks['original_title'].iloc[similarciko[i][0]])

print('============================================================================')
print('Buku bagus untuk Dedi:')
for i in range(0,5):
    if similardedi[i][0] not in dedisuka:
        print('-',dfBooks['original_title'].iloc[similardedi[i][0]])
    else:
        i+=5
        print('-',dfBooks['original_title'].iloc[similardedi[i][0]])

print('============================================================================')
print('Buku bagus untuk Ello:')
for i in range(0,5):
    if similarello[i][0] not in ellosuka:
        if str(dfBooks['original_title'].iloc[similarello[i][0]])=='nan':
            print('-',dfBooks['title'].iloc[similarello[i][0]])
        else:
            print('-',dfBooks['original_title'].iloc[similarello[i][0]])  
    else:
        i+=5
        if str(dfBooks['original_title'].iloc[similarello[i][0]])=='nan':
            print('-',dfBooks['title'].iloc[similarello[i][0]])
        else:
            print('-',dfBooks['original_title'].iloc[similarello[i][0]]) 