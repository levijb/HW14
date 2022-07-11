# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 10:50:27 2022

@author: ljd3frf
"""
import pandas as pd

class BookLover:
    
    num_books = 0
    book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})
    
    def __init__(self, name, email, fav_genre):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        
        
    def add_book(self, book_name, book_rating):
        if not (self.book_list['book_name'].eq(book_name)).any():
            new_book = pd.DataFrame({
                'book_name': [book_name], 
                'book_rating': [book_rating]
                            })
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1
        else:
            return 'Book already added to list'
            
            
            
    def has_read(self, book_name):
        if (self.book_list['book_name'].eq(book_name)).any():
            return True
        else:
            return False
        
        
    def num_books_read(self):
        print(len(self.book_list))
        
        
    def fav_books(self):
        pd_fav = self.book_list[self.book_list['book_rating'] > 3]
        print(pd_fav)
    
    
cla = BookLover('Levi', 'ljdfrf','smut' )
print(cla.name)
print(cla.email)
print(cla.fav_genre)

print(cla.num_books)

cla.add_book('robot', 5)
cla.add_book('robot', 5)

cla.add_book('acdc', 4)
cla.add_book('trump', 2)
print(cla.book_list)
print(cla.num_books)

print(cla.has_read('robot'))
cla.num_books_read()
cla.fav_books()