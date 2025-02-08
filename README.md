## Kaprekar Constant  

📌 Overview  
This Python program demonstrates the fascinating mathematical phenomenon of **Kaprekar's Constant (6174)**.  
By iteratively rearranging and subtracting the digits of any four-digit number (with at least two distinct digits), it always converges to **6174** in at most 7 steps.  

🚀 How It Works  
1. Take any four-digit number with at least two distinct digits.  
2. Arrange the digits in **descending** and **ascending** order to form two numbers.  
3. Subtract the smaller number from the larger one.  
4. Repeat until you reach **6174** (Kaprekar's Constant).  

Example  
text
Input: 3524  
Step 1: 5432 - 2345 = 3087  
Step 2: 8730 - 0378 = 8352  
Step 3: 8532 - 2358 = 6174 (Kaprekar's Constant)
