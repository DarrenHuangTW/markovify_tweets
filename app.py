# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 14:52:02 2018

@author: Darren Huang
"""

import markovify
 
 
if __name__ == "__main__":
    with open("tweets.csv") as f:
        text = f.read()
    model = markovify.Text(text)
    print(model.make_short_sentence(140))