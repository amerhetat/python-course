## numerical variables
a = int
number_a = 10  # integer value assign to variable a
# print(number_a)

number_b = 3.14
# print(number_b)

## string variables
text1 = str()
text1 = 'my instagram account: @moien.salimi'
text2 = "my instagram account: @moien.salimi"
text3 = '''Open a terminal.
Setup the pip package manager.
Install the virtualenv package.
Create the virtual environment.
Activate the virtual environment.
Deactivate the virtual environment.
Optional: Make the virtual environment your default Python.
More: Python virtualenv documentation.'''
# print(text1[2:13:2])
## list variables
ll = list() ## or l1 = []
list1 = [1, 2, 3, 'hamed', 'mitra']
list2 = list1[0:3]
# print(list2, type(list2))
list_names = ['arham', 'mohamad amin', 'mitra', 'hamed']
# print(list_names)
list_names[0] = 'mojgan'
# print(list_names)

## tuple variable

tuple1 = ('arham', 'mohamad amin', 'mitra', 'hamed')
# print(tuple1[0])

## set variable
s = set()
# print(type(s))
set1 = {'arham', 'mohamad amin', 'mitra', 'hamed', 'hamed'}
# print(set1)
list23 = [1,1,2,3]
list24 = list(set(list23))
# print(list24)
## dictionary
d = dict() ## or d = {}
d = {'key1': 'value1',
     'key2': 'value2'}

d2 = {}
d2['key1'] = ['python', 3.14, 'c++']
d2['students'] = {'student1': 'niloofar', 'stydent2': 'mohammad amin'}
# print(d2)
## range
x = range(3,10)
print(x)
for i in x:
     print(i)



## use methods of classes
##numeric
x = 3.14 +5j
y = x.imag
# print(y)
## string
text2 = '''12 Novels {} Considered the “Greatest Book Ever Written”
Anna Karenina. Greta Garbo in Anna Karenina. ...
To Kill a Mockingbird. To Kill a Mockingbird. ...
The Great {} Gatsby. F. ...
One Hundred Years of Solitude. Gabriel García Márquez. ...
A Passage to India. E.M. Forster. ...
Invisible Man. Ralph Ellison. ...
Don Quixote. Don Quixote. ...
Beloved. Toni Morrison.'''

out1 = text2.format('pyhton', 'C++')

# print(out1)
code = '0151010269'
url = 'https://www.amazon.com/1984-Signet-Classics-George-Orwell/dp/{}/ref=sr_1_1?dchild=1&keywords=1984&qid=1629810747&s=books&sr=1-1'.format(code)
# print(url)

txt = "  For only {price:.3f} dollars!   "
text45 = txt.strip()
print(txt)
print(text45)
# print(txt.format(price = 49.9876))

## list

list1 = text2.split()[:5]
list1.append('12')
print(list1)
c = len(list1)
# print(len('moien salimi'))
## dictionary

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({'brand':'bmw'})

print(thisdict)




