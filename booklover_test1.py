# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 11:56:41 2022

@author: ljd3frf
"""

import unittest
import os

print(os.getcwd())

testclass = BookLover('Levi', 'email', 'action')
testclass
class BookLoverTestSuite():
    
    def test_1_add_book(self):
        testclass.add_book('robot', 5)
        self.assertTrue(self.book_list['book_name'].eq('robot')).any()
        