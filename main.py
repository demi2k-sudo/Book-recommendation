import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import nltk
from nltk.stem.porter import PorterStemmer
from sklearn.metrics.pairwise import cosine_similarity

ps = PorterStemmer()
cv = CountVectorizer(max_features = 50000, stop_words = 'english')

def stem(text):
    y=[]
    for i in text.split():
        y.append(ps.stem(i))
    return ' '.join(y)


books_df= pd.read_csv("books.csv")
books_df = books_df[['title','authors','categories','description','thumbnail']]
books_df['authors'] = books_df['authors'].apply(lambda x:str(x))
books_df['authors'] = books_df['authors'].apply(lambda x:x.split())
books_df.dropna(inplace=True)
books_df['description'] = books_df['description'].apply(lambda x:x.split())
books_df['categories'] = books_df['categories'].apply(lambda x:x.split())
books_df['tags'] = books_df['authors']+books_df['categories']+books_df['description']
new_df = books_df[['title','tags','thumbnail','categories']]
new_df['tags']=new_df['tags'].apply(lambda x: ' '.join(x))
new_df['tags'] = new_df['tags'].apply(stem)
vectors = cv.fit_transform(new_df['tags']).toarray()
    
new_df['tags'] = new_df['tags'].apply(stem)
similarity = cosine_similarity(vectors)


def recommend(book,n):
    lst=[]
    book_index =new_df[new_df['title']==book].index[0]
    distances = similarity[book_index]
    book_list = sorted(list(enumerate(distances)),reverse= True,key = lambda x:x[1])[1:n+1]
    result=[]
    link=[]
    genre = new_df.iloc[book_list[0][0]].categories
    for i in book_list:
        a = new_df.iloc[i[0]].title
        link.append(new_df.iloc[i[0]].thumbnail)
        b=0
        if genre[0] in new_df.iloc[i[0]].categories:
            b=1
        lst.append((a,b))
    for i in lst:
        if i[1]==1:
            result.append(i[0])
    for i in lst:
        if i[1]==0:
            result.append(i[0])
        
    return [result,link]

def recom(book_name):
    

    result=recommend(book_name,4)
    
    return result

print(recom("Spider's Web"))