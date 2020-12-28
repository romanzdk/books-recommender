import pandas as pd

ratings = pd.read_csv('data/ratings.csv')
books = pd.read_csv('data/books.csv')

def get_similar(book_name):
    
    recommendation = {}
    title = book_name

    # get my book
    b = (
        books[books['Book-Title'].str.contains(book_name.lower())]
        .sort_values('Users_rated', ascending=False)
        )
    
    # book isbn and title
    if b.shape[0] > 0:
        isbn = b.iloc[0,0]
        title = b.iloc[0,2]

        # users who liked my book
        users = ratings.query(f"`ISBN` == '{isbn}' and `Book-Rating` > 8")['User-ID']

        # books the users also liked
        user_books = (
            ratings
            .merge(users, on = 'User-ID')
            .groupby('ISBN')
            .agg({'Book-Rating':'mean', 'Number of book ratings':'min'})
            .sort_values(['Book-Rating', 'Number of book ratings'], ascending=False)
            .reset_index()['ISBN'][:5]
        )

        recommendation = books[books['ISBN'].isin(user_books)][['Book-Title', 'Book-Author']].to_dict('records')
    
    return {title:recommendation}