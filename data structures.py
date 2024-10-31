#list
employees =['jone','smith','fatuma']
print(employees)
print(employees[0])
print(employees[2])
employees.append('juma')
print(employees)
#employees.insert('jose')
print(employees)
#employees.extend(   'okoth', 'sam' ,'mike')
print(employees)
#tuples


#sets
students = {'john', 'carol', 'shakes'}
if 'john' in students:
    print('john is present in student')
else:
    print('john is not present')
    if 'peter' in students:
        print('peter is present')
    else:
        print('peter is not present')
        students.add('vivian')
#dictionary
books = {
'title': 'The book',
'author': 'wafula',
'publisher':'2002',
'institute':'borabu'
}
print(books)
print(books['publisher'])
books['cover_color']= "blue"
print(books)
if 'title' in books:
    print('title is present')
else:
    print('title not present')

hotel={
'chapati':'70ksh',
'mandazi': '30ksh',
'rice':'100ksh',
'ugali':'300ksh',
'ndengu':'230ksh',
    }
print(hotel)
if 'chapati' in hotel:
    print('@70ksh')
else:
    print('not on the menu')
    if 'mandazi' in hotel:
        print('@30ksh')
    else:
        print('not on the list')
    if 'mandazi' in hotel:
        print('@30ksh')
    else:
        print('not on the list')
        if 'rice' in hotel:
            print('@100')
        else:
            print('not on the list')
            if 'ugali' in hotel:
                print('@300ksh')
            else:
                print('not on the list')
                if 'ndengu' in hotel:
                    print('230ksh')
                else:
                    print('not on the list')

firstnumber = input("Enter your first number ")
secondnumber = input("Enter your second number")
thirdnumber = input("Enter your third number ")
fourthnumber = input("Enter your fourth number")
fifthnumber = input("Enter your fifth number")
if fifthnumber>secondnumber:
    print(firstnumber)
else:
    print(thirdnumber,fourthnumber,fifthnumber)