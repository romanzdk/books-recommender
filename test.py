import pandas as pd

df = pd.read_excel('data/out.xlsx')
book_name = 'garfield'

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

print("Author", author)