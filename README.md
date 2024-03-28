# Movie Recommender System

## Overview
This project is a Movie Recommender System built with Python and Streamlit. It uses BERT embeddings and cosine similarity to recommend movies that are similar to a selected movie.

## Recommender Systems
Recommender systems are tools used in applications to suggest products, movies, music, and more to users based on their past behavior or behavior of similar users. They play a crucial role in the field of personalized content delivery and are widely used in various domains such as e-commerce, entertainment, and social media platforms.

There are primarily three types of recommender systems:

1. **Collaborative Filtering**: This method makes automatic predictions about the interests of a user by collecting preferences from many users. The underlying assumption is that if a user A has the same opinion as a user B on an issue, A is more likely to have B's opinion on a different issue.

2. **Content-Based Filtering**: This method uses only information about the description and attributes of the items users has previously consumed to model user's preferences. In other words, these algorithms try to recommend items that are similar to those that a user liked in the past (or is examining in the present). In particular, various candidate items are compared with items previously rated by the user and the best-matching items are recommended.

3. **Hybrid Systems**: These systems combine collaborative and content-based filtering methods. They can be implemented in several ways: by making content-based and collaborative-based predictions separately and then combining them; by adding content-based capabilities to a collaborative-based approach (and vice versa); or by unifying the approaches into one model.

In this project, we use **Content-Based Filtering**. We first convert the movie titles into BERT embeddings. Then, we compute the cosine similarity between the embeddings to find similar movies. The system recommends the top 5 movies with the highest cosine similarity.

## Methodology
The recommender system is based on BERT embeddings and cosine similarity:

- **BERT Embeddings**: BERT (Bidirectional Encoder Representations from Transformers) is a method for pre-training language representations. It obtains dense vector representations for each word in the movie titles. These representations capture the semantics of the words and their context within the title.

- **Cosine Similarity**: This is a metric used to determine how similar two entities are irrespective of their size. In this case, it is used to find the cosine of the angle between two vectors. The vectors in this context are the BERT embeddings of the movie titles. Cosine similarity ranges from 0 to 1. The closer the cosine value to 1, the more similar the movies are to each other.

The system first converts the movie titles into BERT embeddings. Then, it computes the cosine similarity between the embeddings to find similar movies. The system recommends the top 5 movies with the highest cosine similarity.

The methodology of the system can be broken down into the following steps:

1. **Data Loading**: The system loads the movie data from a pickle file. This data contains the titles of the movies.

2. **BERT Embeddings**: Each movie title is converted into a BERT embedding. This dense vector representation captures the semantics of the words in the title and their context.

3. **Cosine Similarity Calculation**: The cosine similarity between the BERT embeddings of the movie titles is computed. This results in a similarity matrix where the entry at the i-th row and j-th column represents the cosine similarity between the i-th and j-th movie.

4. **Recommendation**: When a movie is selected, the system looks up the corresponding row in the similarity matrix. It then sorts the entries in this row in descending order and selects the top 5 entries. These entries correspond to the movies that are most similar to the selected movie.

## Installation
1. Clone this repository.
2. Install the required packages using pip:
    ```
    pip install -r requirements.txt
    ```

## Usage
To run the Streamlit app, use the following command:
    ```
    streamlit run app.py
    ```

## Files
- `app.py`: This is the main application file where the Streamlit UI is defined.
- `model\\movies.pkl`: This file contains the movie data.
- `model\\similarity_bert.pkl`: This file contains the precomputed cosine similarity matrix.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

