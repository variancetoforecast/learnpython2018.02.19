import os

Test = open('/home/d/Desktop/learnpython/cow/file1.txt', 'w')

Test.write('I am now overriding the text \n')

Test.close

Test = open('/home/d/Desktop/learnpython/cow/file1.txt', 'a')

Test.write('I am now appending the text \n')

Test.close

Test2 = open('/home/d/Desktop/learnpython/cow/new2.xls', 'w')
Test2.write('This is a new file \n')
Test2.write('This is a new file')
Test2.close