import pandas as pd

df = pd.read_excel('data/out.xlsx')

def get_similar(book_name):
    books = (
        df[df['title'].str.lower().str.contains(book_name)]
        .sort_values('rating_cnt', ascending = False)
    )

    author = books.iloc[0,0]
    author_books = (
        df[df['author'] == author]
        .sort_values('rating_avg', ascending = False)[:5]['title']
        .to_list()
    )

    year = books.iloc[0,3]
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