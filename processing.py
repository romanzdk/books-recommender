import pandas as pd

df = pd.read_csv('data/out.csv', sep=';')

def get_similar(book_name):
    
    author_books = []
    year_books = []

    # get all books with the corresponding name
    books = (
        df[df['title'].str.contains(book_name.lower())]
        .sort_values('rating_cnt', ascending = False)
    )

    if books.shape[0] > 0:
        # get books of the same author
        author = books.iloc[0,0]
        author_books = (
            df[df['author'] == author]
            .sort_values('rating_avg', ascending = False)[:5]['title']
            .to_list()
        )

        # get books within the year range
        year = books.iloc[0,2]
        year_range = 5
        year_books = (
            df[(df['year'] <= (year + year_range)) & (df['year'] >= (year - year_range))]
            .sort_values('rating_avg', ascending = False)[:5]['title']
            .to_list()
        )
    return {
        'Author books':author_books,
        'Year books':year_books
    }