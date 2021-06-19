# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 07:48:29 2021

@author: JOHN
"""

# Song attributes dictionary
song = {
    "title": "We Are the Champions",
    "album": "News of the World",
    "artist": "Queen",
    "genre": "Arena rock",
    "release year": "1977",
    "length": "2.59",
    "length (seconds)": "179",
    "songwriter": "Freddie Mercury",
    "producers": "Queen, Mike \"Clay\" Stone"
}

# Print the info aboute song
for key in song:
    print("{0:s}: \"{1:s}\"".format(key.capitalize(), song[key]))


def guess(key, val):
    str = input("guess the value of a song:")
    if str == key:
            print("you are correct")
    else:
        print("better luck next time")
    return key in song and song[key] == val
























