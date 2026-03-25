# Day-3 Introduction
Today was all about operators in python

# What i have Learnt
there are different types of operators in python (and every other programming language to be fair)
they are:
- Arithmetic Operators
- Assignment Operators
- Comparison Operators
- Logical Operators
- Boolean Operators
- Bitwise Operators

i learnt something new which are the "in, not in, is, is not" which is new to me

# thoughts
- today i was lethargic and didnt really want to do the exercises, but yes i want to keep the streak alive and continue learning python
- although i felt lazy initially, i did start enjoying it later on 

---

# Mistakes
- i did the typecasting from float to string value but didnt store it in a variable
    - so what happens is, python DOES create the string value but immediately discards it
    - thats why we store it in a variable
- again the silly mistake of not putting strings in quotes.

---

# Key takeaways
comparison between strings is done lexographically, for example, if both words are 6 letters, it checks the first letter of each word, which first-letter of both the words comes first in the ASCII format. Upper-case letters come before Lower-case letters
 - thats why 'python' > 'dragon' returns true

Values which are false inherently are called "falsy" values like 0, 0.0, a = [], etc
 - and its opposite is called truthy values

the "and" operator need *not always* return true/false.
 - for example, if all the values are true, it can return the last value
 - if all values are not true, it will definitely return false

Use "==" to compare **values** and "is" to compare the **identity (memory location)**
 - a = 10 and b = 10, if we use ==, the value 10 is being checked, if we use 'is', the memory location of the variables are being checked
    - since integer ranges from -10 to 256, and 10 lies in this range, python points the variables a and b to the same memory location for *efficiency*
    - "is" will return true, and == will also return true
        - but if it was a = 1000 and b = 1000, then == would return true normally **but** "is" would return False.
