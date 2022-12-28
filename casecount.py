# -*- coding: utf-8 -*-
"""caseCount.ipynb

def case_func(s):
  u=0
  l=0
  for i in s:
      if i>='a' and i<='z':
       l+=1

      if i >='A' and i<='Z':
       u+=1

  print("LowerCase letter in the String",l)
  print("UpperCase letter in the String",u)
s = case_func(str(input("Enter a String to count lower and Upper Case: ")))

