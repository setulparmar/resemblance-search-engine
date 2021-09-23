**Problem Statement** : Create an ML model that can detect similarities between two products and giving a probability of how much the two products resemble each other. If the value crosses a threshold (which you set), it should tell whether the two are identical or nearly identical. Wrap an accessible front-end around the model, and make it available via an API call.


**Description :**
While searching for a local product on an online retailer, the search usually yields many different recommendations which all resemble each other, making it difficult for the consumers to choose the right product according to their preferences. Machine Learning can help to solve these kinds of problems by detecting similarities between two products and giving a percentage score of how much the products resemble each other.

**We have used Movies name as a product** that needs to be searched in the search box and then it will recommend the top 10 movies along with their percentage similarity score by applying cosine similarity.

# Movie-Resemblance-Engine

We used IMDb 5000 Movie Dataset to built this model from kaggle.

Link to dataset :- https://www.kaggle.com/carolzhangdc/imdb-5000-movie-dataset

Link to the web application :- https://resemblance-search-engine.herokuapp.com/

Keywords : Cosine similarity , flask , machine learning , heroku deployment, movie recommendation , count vectorizer. 

# Files Brief

1)In the preprocessing_dataset.ipynb file, we preprocessed the IMdb data. 

2)In the create.py file ,we created two files for future uses one data.csv and other a numpy matrix.

3)The application is run from the main.py file.

# References 
1) https://www.machinelearningplus.com/nlp/cosine-similarity/
2) https://www.youtube.com/watch?v=XoTwndOgXBM
3) https://github.com/codeheroku/Introduction-to-Machine-Learning/tree/master/Building%20a%20Movie%20Recommendation%20Engine
4) https://medium.com/code-heroku/how-to-turn-your-machine-learning-scripts-into-projects-you-can-demo-cbc5611ca442
5) https://www.youtube.com/watch?v=Li0Abz-KT78
6) https://techblog.commercetools.com/improving-data-quality-with-product-similarity-search-d037c7212071
7) https://www.youtube.com/watch?v=2vASHVT0qKc
