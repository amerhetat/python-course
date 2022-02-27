




from finction_files_word_counter import wcounter, ccounter, text_extractor

import  requests
from bs4 import BeautifulSoup
## program inputs
url = 'https://www.wikihow.com/Find-the-Surface-Area-of-Cylinders#:~:text=To%20get%20the%20circumference%2C%20simply,18.84%20centimeter%20(7.4%20in).&text=Multiply%20the%20circumference%20of%20the%20circle%20by%20the%20height%20of%20the%20cylinder.'
css = '#mf-section-0 p'
##

text1 = text_extractor(url, css) # step 1
words_number = wcounter(text1) # step 2
charecters_number = ccounter(text1) # step 3
print('Your input text has %i words and %i charecters' %(words_number, charecters_number))

