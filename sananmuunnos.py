#!/usr/bin/envpython
#-*- coding: utf-8 -*-

"""
Sananmuunnos: Transforming Finnish spoonerisms made easy (and systematic).
"""

__author__ = "Tuukka Ojala"
__email__ = "tuukka.ojala@gmail.com"
__version__ = "2015.0918"
__license__ = "MIT"

import re

#Regular expressions for detecting different types of sananmuunnoses
#Double vowel: the word begins with a consonant and continues with
#two identical vowels.
_double_vowel = re.compile(r"^[^aeiouyäö]?([aeiouyäö])\1")
#initial vowel: the word begins with a vowel and continues with a letter which
#is not the same as the previous one.
_initial_vowel = re.compile(r"^[aeiouyäö]")
#Initial consonant: The word begins with a consonant and continues with
#two non-identical vowels.
_initial_consonant = re.compile(r"^[^aeiouyäö]([aeiouyäö])[^\1]")
#Matches any vowel.
_vowel = re.compile(r"[aeiouyäö]")

"""The following 3 functions test a pair of words against the regular expressions above. If they match, the words are transformed accordingly. Otherwise the function returns false."""

def _is_double_vowel(word1, word2):
    """Test word1 and word2 against the "double vowel" rule."""
    match = _double_vowel.search(word2)
    if match:
        vowel1 = _vowel.search(word1)
        vowel2 = _vowel.search(word2)
        initial1 = word1[:vowel1.start() +1] + word1[vowel1.start()]
        initial2 = word2[:vowel2.start() +1]
        transformed1 = initial2 +word1[vowel1.end():]
        transformed2 = initial1 + word2[vowel2.end() +1:]
        return (transformed1, transformed2)
    else:
        return False

def _is_initial_vowel(word1, word2):
    """Test word1 and word2 against the "initial vowel" rule."""
    if _initial_vowel.search(word1):
        transformed1 = word2[:2] +word1[1:]
        transformed2 = word1[0] +word2[2:]
        return (transformed1, transformed2)
    else:
        return False

def _is_initial_consonant(word1, word2):
    """Test word1 and word2 against the "initial consonant" rule."""
    if _initial_consonant.search(word1):
        transformed1 = word2[:2] +word1[2:]
        transformed2 = word1[:2] +word2[2:]
        return (transformed1, transformed2)
    else:
        return False

def _vowel_harmony(word):
    """Attempts to make the given word comply with Finnish vowel harmony.
    
    If the first vowel of the word is a front vowel (a, o or u) all the vowels
    get transformed to their equivalent back vowels (ä, ö, y) and vice versa."""
    vowel = _vowel.search(word)
    if vowel and word[vowel.start()] in ["a","o","u"]:
        word = word.replace("ä", "a")
        word = word.replace("ö", "o")
        word = word.replace("y", "u")
    elif vowel and word[vowel.start()] in ["y", "ä", "ö"]:
        word = word.replace("u", "y")
        word = word.replace("a", "ä")
        word = word.replace("o", "ö")
    return word

def _test(transformation, word1, word2):
    """Tries transforming word1 and word2 with the given transform function.
    
    It tries swapping the words if the transformation fails.
    This function returnsthe transformed words or false if
    the transformation failed both ways."""
    result = transformation(word1, word2)
    if not result:
        result = transformation(word2, word1)
        if result:
            return (result[1], result[0])
    return result

def transform(words):
    """Make a sananmuunnos ("word transformation") out of the given words.
    
    This function returns either teh created sananmuunnos or None if the transformation failed."""
    transformed = None
    try:
        word1, word2 = words.split(" ")
    except ValueError:
        return None
    for transformation in _transformations:
        transformed = _test(transformation, word1, word2)
        if transformed:
            break
    word1, word2 = transformed
    word1 = _vowel_harmony(word1)
    word2 = _vowel_harmony(word2)
    return " ".join((word1, word2))

#List of transformations used by the "transform" function.
_transformations = [_is_double_vowel, _is_initial_vowel, _is_initial_consonant]

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) is not 3:
        print("Usage: {} word1 word2".format(sys.argv[0]))
    else:
        print(transform(" ".join(sys.argv[1:])))
