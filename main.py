#Importing essential libraries
import numpy as np
import pandas as pd
from flask import Flask, render_template, request

# libraries for calculating cosine_similarity and count matrix
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# defining a function which creates similarity matrix
def create_sim_mat():
    data = pd.read_csv('data.csv')
    # creating a count matrix
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(data['comb'])
    # creating a similarity score matrix
    sim_mat = cosine_similarity(count_matrix)
    return data,sim_mat


# defining a function that tell us 10 most similar movies
def similarity(m):
    m = m.lower()
    # check if data and sim_mat are already assigned
    try:
        data.head()
        sim_mat.shape
    except:
        data, sim_mat = create_sim_mat()
    # check if the movie is in our database or not
    if m not in data['movie_title'].unique():
        return('Movie not found.\nPlease check if you spelled it correct(or try another name')
    else:
        # getting the index of the movie in the dataframe
        i = data.loc[data['movie_title']==m].index[0]

        # fetching the row containing similarity scores of the movie
        # from similarity matrix and enumerate it
        lst = list(enumerate(sim_mat[i]))

        # sorting this list in decreasing order based on the similarity score
        lst = sorted(lst, key = lambda x:x[1] ,reverse=True)

        # taking top 1- movie scores
        # not taking the first index since it is the same movie
        lst = lst[1:11]

        # making an empty list that will containg all 10 movie recommendations
        l = []
        s= []
        for i in range(len(lst)):
            a = lst[i][0]
            l.append(data['movie_title'][a]+"  , Similarity Score: "+ str((round(lst[i][1],2))*100) + "%")
            s.append(a)
        return l

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/recommend")
def recommend():
    movie = request.args.get('movie')
    r = similarity(movie)
    movie = movie.upper()
    if type(r)==type('string'):
        return render_template('similar.html',movie=movie,r=r,t='s')
    else:
        return render_template('similar.html',movie=movie,r=r,t='l')



if __name__ == '__main__':
    app.run()
