# print('Hello world')
#
# for i in range(5):
#     print('holy shit' + str(i))
#     counts
#     from
#
#     0
#
# for i in range(5):
#     print('holy shit' + str(i + 1))
#     counts
#     from
#
#     1
#
# total = 0
# for num in range(101):
#     total = total + num
# print(total)
#
# print('holy shit i am')
# for i in range(5):
#     print('stoned' + str(i))
#
# print('holy shit i am')
# for i in range(12, 16):
#     print('stoned' + str(i))
#
# print('holy shit i am')
# for i in range(0, 10, 2):
#     print('stoned' + str(i))
#
# print('holy shit i am')
# for i in range(0, 10, -2):
#     print('stoned' + str(i))
#
# import sys
#
# print('hello')
# sys.exit()
# print('goodbye')
#
# import pyperclip
#
#
# def hello():
#     print('howdy!')
#     print('howdy!!!!')
#     print('Hello there.')
#
#
# hello()
# hello()
# hello()
#
#
# def hello(name):
#     print('Hello ' + name)
#
#
# hello('alice')
# hello('bob')
#
#
# def plusone(number):
#     return number + 1
#
#
# new_number = plusone(5)
# print(new_number)
#
# print('Hello has ' + str(len('hello')) + ' letters int it.')
#
# print('Hello ', end='')
# print('world')
#
#
# def div42by(divideby):
#     try:
#         return 42 / divideby
#     except ZeroDivisionError:
#         print('error: you tride too divide by zero.')
#
#
# print(div42by(2))
# print(div42by(12))
# print(div42by(0))
# print(div42by(1))
#
# print('how many cats do you have')
# numcats = input()
# try:
#     if int(numcats) >= 4:
#         print('That is a lot of cats')
#     else:
#         print('That is not that many cats.')
# except ValueError:
#     print('you did not enter a number')
#
# print('how many cats do you have')
# numcats = input()
# try:
#     if int(numcats) >= 4:
#         print('That is a lot of cats')
#     elif int(numcats) <= 0:
#         print('Please enter a Positive number')
#     else:
#         print('That is not that many cats.')
# except ValueError:
#     print('you did not enter a number')
#
# """
#
# while True:
#     print('How many cats do you have?')
#     numCats = input()
#     try:
#         if int(numCats) >= 4:
#             print('That is a lot of cats.')
#             break
#         elif int(numCats) < 0:
#             print('you cant have negative cats shit lord this isn\'t a death counter ')
#
#         else:
#             print('That is not that many cats')
#             break
#     except ValueError:
#         print('Thats not even a number asshole')
#
#
#
# class ass_hole:
#
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def full_name(self):
#         return f'{self.first_name} {self.last_name}'
#
#
# me = ass_hole('Jacob', 'Henson')
# gavin = ass_hole('Gavin', 'Springsteen')
# brandon = ass_hole('Brandon', 'Rollins')
# trey = ass_hole('Trey', 'Cooper')
#
#
# print(me.full_name())
# print(gavin.full_name())
# print(brandon.full_name())
# print(trey.full_name())
#
#
# import sys
# sysversion_info
# print(f'hello from python{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}!')
#
#
# my_age = 24
# user_age = int(input('how old are you'))
#
#
# def difference(user_age):
#     if user_age <= my_age:
#         return my_age - user_age
#     else:
#         return (user_age - my_age) * 2
#
#
# print(difference(user_age))
# print(difference(user_age))
#
# num = 8
#
# To take the input from the user
# num = int(input('Enter a number: '))
#
# num_sqrt = num ** .5
# print(f'The square root of {num} is {num_sqrt}')
# print('The square root of %0.3f is %0.3f'%(num ,num_sqrt))
#
#
# num = int(input('enter a number'))
# remainder = num % 2
#
#
# def even_odd():
#     if remainder == 0:
#         print('even')
#     else:
#         print('odd')
#
#
# even_odd()
# print(remainder)
#
# num = None
# remainder = None
#
#
# def even_odd():
#     if remainder == 0:
#         print('even')
#     else:
#         print('odd')
#
#
# while num != 0:
#     num = int(input('enter a number'))
#     remainder = num % 2
#     even_odd()
#     print(remainder)
#
# even_odd()
# print(remainder)
#
# print ('Enter Your Name')
# name = input ()
#
# print ('Enter Your age')
# age = int(input ())
#
# if name == 'Alice':
#     print('Hi, Alice.')
# elif age < 12:
#     print('You are not Alice, kiddo.')
# elif age > 2000:
#     print('Unlike you, Alice is not an undead, immortal vampire.')
# elif age > 100:
#     print('You are not Alice, grannie.')
#
#
# print ('Enter Your Name')
# name = input ()
#
# print ('Enter Your age')
# age = int(input ())
#
# if name == 'Alice':
#     print('Hi, Alice.')
# elif age < 12:
#     print('You are not Alice, kiddo.')
# elif age > 2000:
#     print('Unlike you, Alice is not an undead, immortal vampire.')
# elif age > 100:
#     print('You are not Alice, grannie.')
#
# x = input()
# print (x)
#
# import utill
#
# utill.print_header('...Testing...')
# enumerate()
# .isupper()
# in "ABCD..XYZ"
#
#
# def capital_indexes(dex):
#     for elm in dex:
#         if elm.isupper():
#             print(range())
#
# capital_indexes('HeLlO')
#
# for i in list_str:
#     if (i.isupper()):
#       count = count + 1
#
# def capital_indexes(dex):
#     for letter in dex:
#         if letter.isupper():
#             print(list(dex))
#
#
# capital_indexes('HeLlO')
#
#
# def string_test(dex):
#     d = {"UPPER_CASE": 0, "LOWER_CASE": 0}
#     for c in dex:
#         if c.isupper():
#             d["UPPER_CASE"] += 1
#         elif c.islower():
#             d["LOWER_CASE"] += 1
#         else:
#             pass
#     print("Original String : ", dex)
#     print("No. of Upper case characters : ", d["UPPER_CASE"])
#     print("No. of Lower case Characters : ", d["LOWER_CASE"])
#
#
# string_test('The quick Brown Fox')
#
# numbers = [7, 8, 9]
# first_number = numbers[0]
# numbers[2] = 11
# if 11 in numbers:
#     print("11 is in the list!")
# for n in numbers:
#     print(n)
#
#
#  string formating pm
#
# user_name = input('enter username')
# print(user_name.lower())
# print(user_name.upper())
# print(user_name.title())
#
# print(f"hello, {user_name.title()} how are you?")
#
#
# import utill
#
# import os
#
# utill.print_header(code_name='File Fuckery')
#
#  print(os.environ.get('USERPROFILE'))
#
# os.chdir('C:\\Users\\gamme')
#
# print(os.getcwd())   gets the current working directory / folder
#
#
# for dirpath, dirnames, filenames in os.walk('C:\\Users\\gamme'):
#     print('current path: ', dirpath)
#     print('Dir: ', dirnames)
#     print('files', filenames)
#     print()
#
#
# print(os.path.isdir('C:\\Users\\gamme\\file_fuckery'))    prints false since there is no fsdf folder
# print(os.path.isfile('D:\\fsdf'))    prints false since there is no fsdf file
# print(os.path.splitext('D:\\tmp\\test.txt'))    splits the file type off ie.
#  ('D:\\tmp\\test', '.txt')
#
# file_fuck_path = os.path.isdir('C:\\Users\\gamme\\file_fuckery')
#
# while file_fuck_path is False:
#     os.mkdir('file_fuckery')
#     os.chdir('C:\\Users\\gamme\\file_fuckery')
#     os.makedirs('demo_1')
#     break
#
# print(os.getcwd())
#
# file_fuck_path = os.path.isdir('C:\\Users\\gamme\\file_fuckery')
#
# print(os.getcwd())
#
# while file_fuck_path is True:
#     os.chdir('C:\\Users\\gamme\\file_fuckery\\demo_1')
#
# print(os.getcwd())
#
#
#      os.chdir('C:\\Users\\gamme\\file_fuckery')
#      os.makedirs('demo_1')
#     os.chdir('C:\\Users\\gamme\\file_fuckery\\demo_1')
#
# print(os.getcwd())
#
#
# import utill
#
# utill.print_header(code_name='FIZZ BUZZ')
#
# for x in range(1,101):
#     if x % 3 == 0 and x % 5 == 0:
#         print('fizz buzz')
#     elif x % 3 == 0:
#         print('fizz')
#     elif x % 5 == 0:
#         print('buzz')
#     else:
#         print(x)
#
# import utill
#
# import os
#
# import datetime
#
# utill.print_header(code_name='os module things')
# utill.new_new()
#
# print(dir(utill))   lists all the dot things i can use ie utill.print_header()
# print(dir(os))   lists all the dot things i can use ie os.path
#
# print(os.getcwd())
#
#  os.chdir('D:\\codeing\\projects')
#
#  os.chdir('D:\\codeing\\projects\\fucking _with_file_IO_for_untitled')   changes working dir to another dir
# two \\ are being used because other wise it wont work
# print(os.getcwd())   gets the current working directory / folder
# print(os.listdir())   list all the sub-dir in the current working dir
# print(os.getcwd())
#
# os.mkdir('os_Demo_1')   can only make one folder
# os.makedirs('os_Demo_2\\Demo_2_sub_folder')   can make several folders nested
#
# print(os.listdir())
#
# os.rmdir('os_Demo_1')   removes only the one dir just like os.mkdir but not
# os.removedirs('os_Demo_2\\Demo_2_sub_folder')   removes all just like os.makedirs but not
#
# print(os.listdir())   nothing to list i just deleted it
#
# os.mkdir('os_Demo_1')
# os.makedirs('os_Demo_2\\Demo_2_sub_folder')
#
# print(os.listdir())
#
# os.rename('os_Demo_1', 'os_rename_1')   renames the thing in the first spot with the second
# os.rename('os_Demo_2', 'os_rename_2')
#
# os.chdir('D:\\codeing\\projects\\fucking _with_file_IO_for_untitled\\os_rename_1')
# print(os.listdir())
#
# print(os.stat('Demo.txt'))   gives in about the thing ie Demo.txt
# print(os.stat('Demo.txt').st_size)   size of file in bytes
# print(os.stat('Demo.txt').st_mtime)   last mod time not very human readable
#
# mod_time = os.stat('Demo.txt').st_mtime
#
# print(datetime.date.fromtimestamp(mod_time))   now you can read it
#
# os.chdir('C:\\Users\\gamme\\Desktop')
#
# print(os.getcwd())
#
# for dirpath, dirnames, filenames in os.walk('D:\\codeing\\projects'):
#     print('current path: ', dirpath)
#     print('Dir: ', dirnames)
#     print('files', filenames)
#     print()
#
# print(os.environ.get('USERPROFILE'))
#
# file_path = os.path.join(os.environ.get('USERPROFILE'), 'test.txt')   USERPROFILE instead of home makes it work
# print(file_path)
#
# with open(file_path, 'w') as f:
#     f.write()
#
# os.chdir('D:\\codeing\\projects\\fucking _with_file_IO_for_untitled')
# print(os.path.isdir('D:\\fsdf'))    prints false since there is no fsdf folder
# print(os.path.isfile('D:\\fsdf'))    prints false since there is no fsdf file
# print(os.path.splitext('D:\\tmp\\test.txt'))    splits the file type off ie.
# ('D:\\tmp\\test', '.txt')
# print(dir(os.path))   prints all the things you an do
#
# os.chdir('D:\\codeing\\projects\\fucking _with_file_IO_for_untitled')
# print(os.listdir())
# os.makedirs('test_folder')    can make several folders nested
#  os.rename()   renames the thing in the first spot with the second
# os.rmdir()   removes only the one dir just like os.mkdir but not
# os.removedirs()   removes all just like os.makedirs but not
# os.chdir('D:\\codeing\\projects\\fucking _with_file_IO_for_untitled\\test_folder')
# print(os.listdir())
#  thires a better method but you can do this
#
# f = open('crap.txt', 'r')
# print(f.name)  prints name of file
# print(f.mode)  prints the read state ie r w r+ read write and both
# f.close()
#
#
# os.chdir('D:\\codeing\\projects\\fucking _with_file_IO_for_untitled\\test_folder')
# print(os.listdir())
#
# with open('crap.txt', 'r') as f:
#
#     f_contents = f.read()
#     print(f_contents, end='')
#
#
#
# def student_info(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
# student_info('math', 'art', name='john', age=22)
#
# def student_info(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
# courses = ['Math', 'Art']
# info = {'name': 'john', 'age': 22}
# student_info(*courses, **info)
#
# os.chdir('D:\\codeing\\projects\\fucking _with_file_IO_for_untitled\\test_folder')
# print(os.listdir())
#
# with open('crap.txt', 'r') as f:
#     size_to_read = 10
#     f_contents = f.read(size_to_read)
#     while len(f_contents) > 0:
#         print(f_contents, end='*')
#         f_contents = f.read(size_to_read)
#
# os.chdir('D:\\codeing\\projects\\fucking _with_file_IO_for_untitled\\test_folder')
# print(os.listdir())
#
# with open('crap.txt', 'r') as f:
#
#     for line in f:
#         print(line, end='')
#
# os.chdir('D:\\codeing\\projects\\fucking _with_file_IO_for_untitled\\test_folder')
# print(os.listdir())
#
# with open('crap.txt', 'r') as f:
#
#     size_to_read = 10
#
#     f_contents = f.read(size_to_read)
#     print(f_contents, end='')
#     f.seek(0)
#     f_contents = f.read(size_to_read)
#     print(f_contents)
#     while len(f_contents) > 0:
#         print(f_contents, end='*')
#         f_contents = f.read(size_to_read)
#
#     os.chdir('D:\\codeing\\projects\\fucking _with_file_IO_for_untitled\\test_folder')
#     print(os.listdir())
#
#     with open('also_crap.txt', 'w') as f:
#         f.write('Test')
#
# os.chdir('D:\\codeing\\projects\\fucking _with_file_IO_for_untitled\\test_folder')
# print(os.listdir())
#
# with open('shit_pic.jpg', 'rb') as rf:   must add the b ie 'rb'
#       means biany makes work with other file types
#     with open('copy_shit_pic.jpg', 'wb') as wf:   must add the b ie 'wb'
#           means biany makes work with other file types
#         for line in rf:
#             wf.write(line)
#
# os.chdir('D:\\codeing\\projects\\fucking _with_file_IO_for_untitled\\test_folder')
# print(os.listdir())
#
# with open('shit_pic.jpg', 'rb') as rf:
#     with open('copy_shit_pic.jpg', 'wb') as wf:
#         chunk_size = 4096
#         rf_chunk = rf.read(chunk_size)
#         while len(rf_chunk) > 0:
#             wf.write(rf_chunk)
#             rf_chunk = rf.read(chunk_size)
# user_input_main_loop = input('\n[L]ist entries, [A]dd an entry, E[x]it: \n')
# user_input_main_loop = user_input_main_loop.lower().strip()
# Invite some people to dinner.
# guests = ['guido van rossum', 'bitch', 'deadpool']
# mess = ' please come to dinner.'
# greet = name + mess
# no_room = "there's no room at the table."
# sorry = 'Sorry,'
#
# def
#
# name = guests[0].title()
# print(greet)
#
# name = guests[1].title()
# print(greet)
#
# name = guests[2].title()
# print(greet)
#
# name = guests[1].title()
# print(f"\nSorry, {name} can't make it to dinner.")
# Jack can't make it! Let's invite Gary instead.
# del(guests[1])
# guests.insert(1, 'gary snyder')
#
#  Print the invitations again.
# name = guests[0].title()
# print(greet)
#
# name = guests[1].title()
# print(greet)
#
# name = guests[2].title()
# print(greet)
#
# We got a bigger table, so let's add some more people to the list.
# print("\nWe got a bigger table!")
# guests.insert(0, 'frida kahlo')
# guests.insert(2, 'reinhold messner')
# guests.append('elizabeth peratrovich')
# name = guests[0].title()
# print(greet)
# name = guests[1].title()
# print(greet)
# name = guests[2].title()
# print(greet)
# name = guests[3].title()
# print(greet)
# name = guests[4].title()
# print(greet)
# name = guests[5].title()
# print(greet)
#  Oh no, the table won't arrive on time!
# print("\nSorry, we can only invite two people to dinner.")
#
# name = guests.pop()
# print(f"Sorry, {name.title()} {no_room}")
#
# name = guests.pop()
# print(f"Sorry, {name.title()} there's no room at the table.")
#
# name = guests.pop()
# print(f"{sorry} {name.title()} there's no room at the table.")
#
# name = guests.pop()
# print(f"{sorry} {name.title()} {no_room}")
#
# There should be two people left. Let's invite them.
# name = guests[0].title()
# print(f"{name}, please come to dinner.")
#
# name = guests[1].title()
# print(f"{name}, please come to dinner.")
#
# Empty out the list.
# del(guests[0])
# del(guests[0])
#
# Prove the list is empty.
# print(guests)
# Hint: Don't forget the 4 leading spaces to
# indicate your code is within the function.
#
# Hint: Don't forget the 4 leading spaces to
# indicate your code is within the function.
# a = 10
# b = 5
#
#
# def multiply_numbers():
#     return a * b
#
#
# def enter_name():
#     username = input('enter your name')
#     return
#
# Enter your code within the following function
# def get_username():
#     while True:
#         username = input("Please type in the name 'PyBites':")
#         if username == 'PyBites':
#             break
#         else:
#             print('Invalid username.')
# The dictionary you'll iterate over to print keys and values
# my_cars = {'Nissan': 2004, 'Jeep': 2013, 'Mazda': 2016, 'Toyota': 2015}
#
#
# Write your for loop within this function
# def print_cars():
#   for x, y in print_cars.items():
#     print(x, y)
#
# a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
# d_items = a_dict.items()
# print(d_items)   Here d_items is a view of items
#
# dict_items([('color', 'blue'), ('fruit', 'apple'), ('pet', 'dog')])
#
# The dictionary you'll iterate over to print keys and values
# my_cars = {'Nissan': 2004, 'Jeep': 2013, 'Mazda': 2016, 'Toyota': 2015}
# for x, y in my_cars.items():
#      print(x, y)
#
# Write your for loop within this function
#
#
# def print_cars(my_cars):
#     for make, year in my_cars.items():
#         print(f"{make}: {year}")
#
#
# def print_cars():
#     for x, y in my_cars.items():
#         print(f"{x}: {y}")
#
# print_cars()
#
#  The list you're going to use to create your tuple
# car_brands = ['Mazda', 'McLaren', 'Opel', 'Toyota', 'Honda']
#
#
#  Write your tuple creation code in this function
# def convert_to_tuple(car_brands):
#     static_cars = tuple(car_brands)
#     return static_cars
#
#
#  convert_to_tuple(car_brands)
# convert_to_tuple()
#
# car_brands = ['Mazda', 'McLaren', 'Opel', 'Toyota', 'Honda']
# static_cars = None
#
#
# def convert_to_tuple(car_brands):
#     static_cars = tuple(car_brands)
#     return static_cars
#
#
# def print_tuples():
#     static_cars = convert_to_tuple(car_brands)
#     print(static_cars)
#
# print_tuples()
# static_cars = convert_to_tuple(car_brands)
#
# print_tuples(static_cars)
#
#
# Complete this function such that it prints the return value from the convert_to_tuple function
# def print_tuples():
#     convert_to_tuple(car_brands)
#     print(static_cars)
#
# print_tuples()
# convert_to_tuple(car_brands,static_cars)
# print_tuples(car_brands,static_cars)
# print(static_cars)
#
#
# VALID_COLORS = ['blue', 'yellow', 'red']
#
#
# def print_colors(VALID_COLORS):
#     """
# In
# the
# while loop ask the user to enter a color,
# lowercase
# it and store
# it in a
# variable.Next
# check:
# - if 'quit'
# was
# entered
# for color, print 'bye' and break.
# - if the
# color is not in VALID_COLORS, print
# 'Not a valid color' and
# continue.
# - otherwise
# print
# the
# color in lower
# case.
# """
#      while True:
#          user_choice = input('Enter a color').lower().strip()
#
#          if user_choice == 'quit':
#              print('bye')
#              break
#          elif user_choice not in VALID_COLORS:
#              print('Not a valid color')
#          elif user_choice in VALID_COLORS:
#              print(user_choice)
#  MIN_DRIVING_AGE = 18
#
#
#  def allowed_driving(name, age):
#      """
# Print
# '{name} is allowed to drive' or '{name} is not allowed to drive'
# checking
# the
# passed in age
# against
# the
# MIN_DRIVING_AGE
# constant
# """
#      is_allowed = 'is allowed' if age >= MIN_DRIVING_AGE else 'is not allowed'
#      print(f'{name} {is_allowed} to drive')
#
#  MIN_DRIVING_AGE = 18
#
#
#  def allowed_driving(name, age):
#      """
# Print
# '{name} is allowed to drive' or '{name} is not allowed to drive'
# checking
# the
# passed in age
# against
# the
# MIN_DRIVING_AGE
# constant
# """
#      if age >= MIN_DRIVING_AGE:
#          filler = 'is allowed'
#      else:
#          filler = 'is not allowed'
#      print(f'{name} {filler} to drive')
#
#  allowed_driving(name, age)
#
#  games_won = dict(sara=0, bob=1, tim=5, julian=3, jim=1)
#
#
#  def print_game_stats(games_won):
#      """
# Loop
# through
# games_won
# 's dict (key, value) pairs (dict.items)
# printing(print, not
# return) how
# many
# games
# each
# person
# has
# won,
# pluralize
# 'game'
# based
# on
# number.
#
#     Expected
# output(ignore
# the
# docstring
# 's indentation):
#
# sara
# has
# won
# 0
# games
# bob
# has
# won
# 1
# game
# tim
# has
# won
# 5
# games
# julian
# has
# won
# 3
# games
# jim
# has
# won
# 1
# game
#
# (Note that as of Python 3.7 - which we're using atm - dict insert order
# is retained so no sorting is required for this Bite.)
# """
#
# for x, y in games_won.items():
#     if y == 1:
#         print(f'{x} has won {y} game')
#     else:
#         print(f'{x} has won {y} games')
#
# print_game_stats(games_won)
# '''
#
# Split up the message on newline
# (\n) using the split builtin, then use the join builtin to stitch it together using a '|' (pipe).
#
# So Hello world:\nI am coding in Python :)\nHow awesome! would turn into: Hello world:|I am coding in Python :)|
# How awesome!
#
# Your code should work for other message strings as well.
#
# Note that as opposed to previous Intro Bites your need to return the new string!
#
# Also note that, although we wanted you to learn about split and join here,
# there are more ways to pull this one off (check out the forum upon resolving this Bite ...)
# '''
#
#
# message = """
# Hello
# world!
# We
# hope
# that
# you
# are
# learning
# a
# lot
# of
# Python.
# Have
# fun
# with our Bites of Py.
# Keep
# calm and code in Python!
# Become
# a
# PyBites
# ninja!"""
#
#  def split_in_columns(message=message):
#      """
# Split
# the
# message
# by
# newline(\n) and join
# it
# together
# on
# '|'
# (pipe),
# return the
# obtained
# output
# string
# """
#      sep = message.split('\n')
#      return '|'.join(sep)
#
#
#  print(split_in_columns())
#
#  message = """
# Hello
# world!
# We
# hope
# that
# you
# are
# learning
# a
# lot
# of
# Python.
# Have
# fun
# with our Bites of Py.
# Keep
# calm and code in Python!
# Become
# a
# PyBites
# ninja!"""
#
#
#  def split_in_columns(message=message):
#      """
# Split
# the
# message
# by
# newline(\n) and join
# it
# together
# on
# '|'
# (pipe),
# return the
# obtained
# output
# string
# """
#      lines = message.split('\n')
#      print( '|'.join(lines))
#
#
#  split_in_columns()
#
#  '''
#
#      Write a function that can sum up numbers:
#
#          It should receive a sequence of n numbers.
#          If no argument is provided, return sum of numbers 1..100.
#          Look closely to the type of the function's default argument ...
#
#      Have fun!
#  '''
#
#
#  def sum_numbers(numbers=None):
#      if numbers is None:
#          numbers = range(1, 101)
#          numbers = sum(numbers)
#          return numbers
#      else:
#          numbers = sum(numbers)
#          return numbers
#
#
#  print(sum_numbers())
#
#
#  VALID_COLORS = ["blue", "yellow", "red"]
#
#
#  def print_colors():
#      """
# In
# the
# while loop ask the user to enter a color,
# lowercase
# it and store
# it in a
# variable.Next
# check:
# - if 'quit'
# was
# entered
# for color, print 'bye' and break.
# - if the
# color is not in VALID_COLORS, print
# 'Not a valid color' and
# continue.
# - otherwise
# print
# the
# color in lower
# case.
# """
#      while True:
#          user_choice = input("Enter a color").lower().strip()
#
#          if user_choice == "quit":
#              print("bye")
#              break
#          elif user_choice not in VALID_COLORS:
#              print("Not a valid color")
#          elif user_choice in VALID_COLORS:
#              print(user_choice)
#
#          return user_choice
#
#
#  def user_track(user_choice):
#      limit = 3
#      score = 0
#      for user_choice in VALID_COLORS:
#          score +=1
#
#  import os
#
#  file_fuck_path = os.path.isdir('D:\\codeing\\bullshit 1\\testing_lots_of_things')
#  D:\codeing\bullshit 1\testing_lots_of_things
#   f = open("myfile.txt", "x")
#   print(f.readlines())
#  sss = input()
#  f = open("demofile2.txt", "a")
#  f.write("Now the file has more content!")
#  f.close()
#
#  open and read the file after the appending:
#  f = open("demofile2.txt", "r")
#  print(f.read())
#
#  VALID_COLORS = ['blue', 'yellow', 'red']
#
#
#  def Color_Game():
#      wincon = 3
#      guesses = 0
#      already_guessed = []
#      gamelogic
#      while guesses < wincon:
#          guess = input("Enter a color.").lower().strip()
#          if guess == "quit":
#              print("Buhbye Meowster!<3")
#              break
#          elif guess not in VALID_COLORS:
#              print("Try again Meowster!")
#          elif guess in already_guessed:
#              print("That's cheating, silly! You can't fool an old cat like me!")
#          elif guess in VALID_COLORS:
#              print("That is totally one of my faves! Good guess Meowster!")
#              already_guessed = [guess]
#              guesses += 1
#      if guesses == 3:
#          print("Smart work Meowster! You know me almost as well as I know you!")
#
#  mycar = {
#      "brand": "Ford",
#      "model": "Mustang",
#      "year": 1964
#  }
#  thisdict["color"] = "red"
#  print(thisdict)
#
#
#  Color_Game()
#
#  message = """
# Hello
# world!
# We
# hope
# that
# you
# are
# learning
# a
# lot
# of
# Python.
# Have
# fun
# with our Bites of Py.
# Keep
# calm and code in Python!
# Become
# a
# PyBites
# ninja!"""
#
#
#  def split_in_columns(message=message):
#      """
# Split
# the
# message
# by
# newline(\n) and join
# it
# together
# on
# '|'
# (pipe),
# return the
# obtained
# output
# string
# """
#      sep = message.split('\n')
#      return '|'.join(sep)
#
#
#  print(split_in_columns())
#
# '''
#
#     Take the block of text provided and strip off the whitespace at both ends. Split the text by newline (\n).
#
#     Loop through the lines, for each line:
#
#         strip off any leading spaces,
#         check if the first character is lowercase,
#         if so, split the line into words and get the last word,
#         strip off BOTH the trailing dot (.) and exclamation mark (!) from this last word,
#         and finally add it to the results list.
#
#     Return the results list.
# '''
#
#  from string import ascii_lowercase
#
#  text = """
# One
# really
# nice
# feature
# of
# Python is polymorphism: using
# the
# same
# operation
# on
# different
# types
# of
# objects.
# Let
# 's talk about an elegant feature: slicing.
# You
# can
# use
# this
# on
# a
# string as well as a
# list
# for example
#     'pybites'[0:2]
# gives
# 'py'.
# The
# first
# value is inclusive and the
# last
# one is exclusive
# so
# here
# we
# grab
# indexes
# 0 and 1, the
# letter
# p and y.
# When
# you
# have
# a
# 0
# index
# you
# can
# leave
# it
# out
# so
# can
# write
# this as 'pybites'[:2]
# but
# here is the
# kicker: you
# can
# use
# this
# on
# a
# list
# too!
# ['pybites', 'teaches', 'you', 'Python'][-2:]
# would
# gives['you', 'Python']
# and now
# you
# know
# about
# slicing
# from the end as well:)
# keep
# enjoying
# our
# bites!
# """
#
#
# def slice_and_dice(text: str = text) -> list:
#     """
# Get
# a
# list
# of
# words
# from the passed in text.
#     See
# the
# Bite
# description
# for step by step instructions"""
#      results = []
#
#
#  slice_and_dice()
#
#  print('sdfsfsfsf\nsfss')
#
#
#  Program to get a substring from the given string
#
#  py_string = 'Python'
#
#   stop = 3
#   contains 0, 1 and 2 indices
#  slice_object = slice(3)
#  print(py_string[slice_object])   Pyt
#
#   start = 1, stop = 6, step = 2
#   contains 1, 3 and 5 indices
#  slice_object = slice(1, 6, 2)
#  print(py_string[slice_object])    yhn
#
#
#  a = '     python     java'
#
#  sliced = slice(3)
#
#  print(a.strip()[sliced])
#
#  Importing random to generate
#  random string sequence
# import random
#
#  Importing string library function
#  import string
#
#
#  def rand_pass(size):
#       Takes random choices from
#       ascii_letters and digits
#      generate_pass = ''.join([random.choice(
#          string.ascii_letters + string.digits)
#          for n in range(size)])
#
#      return generate_pass
#
#
#   Driver Code
#  password = rand_pass(10)
#  print(password)
#
#  from string import ascii_lowercase
#
#  text = """
# One really nice feature of Python is polymorphism: using
# the
# same
# operation
# on
# different
# types
# of
# objects.
#     Let
# 's talk about an elegant feature: slicing.
# You
# can
# use
# this
# on
# a
# string as well as a
# list
# for example
# 'pybites'[0:2] gives 'py'.
# The first value is inclusive and the last one is exclusive so
# here we grab indexes 0 and 1, the letter p and y.
# When you have a 0 index you can leave it out so can write this as 'pybites'[:2]
# but
# here is the
# kicker: you
# can
# use
# this
# on
# a
# list
# too!
# ['pybites', 'teaches', 'you', 'Python'][-2:]
# would
# gives['you', 'Python']
# and now
# you
# know
# about
# slicing
# from the end as well:)
# keep
# enjoying
# our
# bites!
# """
#
#
# def slice_and_dice(text: str = text) -> list:
#     """
# Get
# a
# list
# of
# words
# from the passed in text.
#     See
# the
# Bite
# description
# for step by step instructions"""
#      results = []
#      for line in text.strip().splitlines():
#          line = line.lstrip()
#
#          if line[0] not in ascii_lowercase:
#              continue
#
#          words = line.split()
#          last_word_stripped = words[-1].rstrip('!.')
#          results.append(last_word_stripped)
#
#      return results
#
#
#  print(slice_and_dice())
#  """
# Split up the message on newline
# (\n) using the split builtin, then use the join builtin to stitch it together using a '|' (pipe).
# So Hello world:\
#     nI
# am
# coding in Python:)\nHow
# awesome! would
# turn
# into: Hello
# world: | I
# am
# coding in Python:) | How
# awesome!
# Your
# code
# should
# work
# for other message strings as well
# """
#
# message = """Hello world!
# We hope that you are learning a lot of Python.
# Have fun with our Bites of Py.
# Keep calm and code in Python!
# Become a PyBites ninja!"""
#
#  def split_in_columns(message=message):
#      """Split the message by newline (\n) and join it together on '|'
# (pipe),
# return the
# obtained
# output
# """
#      pipe = "|"
#      message_split = message.split("\n")
#      message_join = pipe.join(message_split)
#      return message_join
#
#  print(split_in_columns())
#
# print('0b{:04b}'.format(0b1100 & 0b1010))
#
#  """
# Take
# the
# block
# of
# text
# provided and strip
# off
# the
# whitespace
# at
# both
# ends.Split
# the
# text
# by
# newline(\n) using
# split.
# Loop
# through
# the
# lines and if the
# first
# character
# of
# each(stripped)
# line is lowercase, split
# the
# line
# into
# words and add
# the
# last
# word
# to
# the(given)
# results
# list, stripping
# the
# trailing
# dot(.) and exclamation
# mark(!) from the end
#
# of
# the
# word.
# At
# the
# end
# of
# the
# function
# return the
# results
# list.
# """
# text = """
# One
# really
# nice
# feature
# of
# Python is polymorphism: using
# the
# same
# operation
# on
# different
# types
# of
# objects.
# Let
# 's talk about an elegant feature: slicing.
# You
# can
# use
# this
# on
# a
# string as well as a
# list
# for example
#     'pybites'[0:2]
# gives
# 'py'.
# The
# first
# value is inclusive and the
# last
# one is exclusive
# so
# here
# we
# grab
# indexes
# 0 and 1, the
# letter
# p and y.
# When
# you
# have
# a
# 0
# index
# you
# can
# leave
# it
# out
# so
# can
# write
# this as 'pybites'[:2]
# but
# here is the
# kicker: you
# can
# use
# this
# on
# a
# list
# too!
# ['pybites', 'teaches', 'you', 'Python'][-2:]
# would
# gives['you', 'Python']
# and now
# you
# know
# about
# slicing
# from the end as well:)
# keep
# enjoying
# our
# bites!
# """
#
#
# def slice_and_dice(text=text):
#     results = []
#     strip_text = text.strip("\n")
#     split_strip = strip_text.split("\n")
#
#     for i in split_strip:
#         i = i.strip(" ")
#         if i[0].islower():
#             strip_i = i.strip('!.')
#             split_i = strip_i.split(" ")
#             results.append(split_i[-1])
#     return results
#
# price_list = {
#     'fish': 8,
#     'beef': 7,
#     'broccoli': 3,
# }
#
# find price clunky ver
# def find_price(item):
#     if item in price_list:
#         return 'The price for {} is {}'.format(item, price_list[item])
#     else:
#         return 'The price for {} is not available'.format(item)
#
#
# print(find_price('fish'))
# print(find_price('cauliflower'))
#
# find price better ver
# def find_price(item):
#     return f'The price for {item} is {price_list.get(item, "not available")}'
#
#
# print(find_price('fish'))
# print(find_price('cauliflower'))
#
#
# operations worse ver
# def operations(operator, x, y):
#     if operator == 'add':
#         return x + y
#     elif operator == 'sub':
#         return x - y
#     elif operator == 'mul':
#         return x * y
#     elif operator == 'div':
#         return x / y
#
#
# operations('mul', 2, 8)
#
#
# operations better ver
# def operations(operator, x, y):
#     return {
#         'add': lambda: x + y,
#         'sub': lambda: x - y,
#         'mul': lambda: x * y,
#         'div': lambda: x / y,
#     }.get(operator, lambda: 'Not a valid operation')()
#
#
# print(operations('mul', 2, 8))
# print(operations('unknown', 2, 8))
#
# x = lambda a: a + 10
# print(x(5))
#
# x = lambda a, b: a * b
# print(x(5, 6))
#
# x = lambda a, b, c: a + b + c
# print(x(5, 6, 2))
#
#
# def myfunc(n):
#     return lambda a: a * n
#
#
# mydoubler = myfunc(2)
#
# print(mydoubler(11))
#
#
# def myfunc(n):
#     return lambda a: a * n
#
#
# mydoubler = myfunc(2)
# mytripler = myfunc(3)
#
# print(mydoubler(11))
# print(mytripler(11))
#
# a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
#      21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
#      41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
#      61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
#      81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100,
#      ]
#
# for x in a:
#     print(a, 'much Numbers suck wow', end='')
# Now it's your turn. Try this practice below.
#
# The core idea in this chapter was about dictionaries and data structures in general.
# Create a simple program that creates a dictionary called d
# such that the following runs without error and prints what is expected:
#
#  d = create d using core concepts above.
#
# print(d["Sam"])           outputs 7
# print(d['rolls'])         outputs ['rock', 'paper', 'scissors']
# print(d.get('Sarah'))     outputs None
# print(d.get('Jeff', -1))  outputs -1
# print(d['done'])          outputs True
#
# rolls = {
#     'rock': {
#         'defeats': ['scissors'],
#         'defeated_by': ['paper']
#     },
#     'paper': {
#         'defeats': ['rock'],
#         'defeated_by': ['scissors']
#     },
#     'scissors': {
#         'defeats': ['paper'],
#         'defeated_by': ['rock']
#     },
# }
#
#
# d = {
#     'Sam': 7,
#     'rolls': ['rock', 'paper', 'scissors'],
#     'Sarah': None,
#     'Jeff': 0,
#     'done': True,
# }
#
# print(d["Sam"])   outputs 7
# print(d['rolls'])   outputs ['rock', 'paper', 'scissors']
# print(d.get('Sarah'))   outputs None
# print(d.get('Jeff', -1))   outputs -1
# print(d['done'])   outputs True
#
# print(d)
#
# from string import ascii_lowercase
#
# text = """
# One
# really
# nice
# feature
# of
# Python is polymorphism: using
# the
# same
# operation
# on
# different
# types
# of
# objects.
#     Let
# 's talk about an elegant feature: slicing.
# You
# can
# use
# this
# on
# a
# string as well as a
# list
# for example
# 'pybites'[0:2] gives 'py'.
# The first value is inclusive and the last one is exclusive so
# here we grab indexes 0 and 1, the letter p and y.
# When you have a 0 index you can leave it out so can write this as 'pybites'[:2]
# but
# here is the
# kicker: you
# can
# use
# this
# on
# a
# list
# too!
# ['pybites', 'teaches', 'you', 'Python'][-2:]
# would
# gives['you', 'Python']
# and now
# you
# know
# about
# slicing
# from the end as well:)
# keep
# enjoying
# our
# bites!
# """
# text = text.strip()
# print(text)
#
# sep = text.split('\n')
#
# s = sep.strip()
#
# print(sep)
#
# def slice_and_dice(text: str = text) -> list:
#     """
# Get
# a
# list
# of
# words
# from the passed in text.
#     See
# the
# Bite
# description
# for step by step instructions"""
#      sep = text.split('\n')  from byte 4
#
#      results = []
#
#  def main():
#      x = get_user_input()
#      get_factorial(x)
#
#
#  def get_user_input():
#      x = int(input('enter a number to find the factorial'))
#      return x
#
#
#  def get_factorial(x):
#      factorial = 1
#      if x < 0:
#          print("Sorry, factorial does not exist for negative numbers")
#      elif x == 0:
#          print("The factorial of 0 is 1")
#      else:
#          for i in range(1, x + 1):
#              factorial = factorial * i
#          print("The factorial of", x, "is", factorial)
#
#
#  if __name__ == '__main__':
#      main()
#
#  a = 'python'
#  b = 'is'
#  c = 'excellent'
#
#  d = a[0] + c[0] + a[len(a)-1] + b
#
#  print(d)
#
#  board = None
#  board = [
#      [None, None, None],
#      [None, None, None],
#      [None, None, None]
#  ]
#
#  print(board)
#
#
#  def a(n):
#      for i in range(n):
#          for j in range(n):
#              if i == 0 or i == n - 1 or j == 0 or j == n - 1:
#                  print('*', end='')
#              else:
#                  print(' ', end='')
#          print()
#
#
#  print(a(10))
#
#  def show_board(board):
#      for row in board:
#          print("| ", end='')
#          for cell in row:
#              symbol = None
#              if cell is None:
#                  symbol = "_"
#              else:
#                  symbol = cell
#              print(symbol, end=" | ")
#          print()
#
#
#  print("Welcome to")
#  print("GeeksforGeeks")
#
#  print()
#
#  print("Welcome to", end=' ')
#  print("GeeksforGeeks", end=' ')
#
#  print('\n')
#
#  print("Welcome to", end='|')
#  print("GeeksforGeeks", end='|')
#
#  l1 = ['a1', 'a2', 'a3', 'a4', 'a5']
#
#  print(l1)
#  print(len(l1))
#
#   x = ['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', ['hh', 'ii'], 'j']
#
#  l1.append('a6')
#
#  print(l1)
#  print(len(l1))
#
#  l1.insert(0, 'a0')
#
#  print(l1)
#  print(len(l1))
#
#  l2 = ['a7', 'a8'] 6
#
#  l1.extend(l2)
#  print(l1)
#  print(len(l1))

# def main():
#     num = get_user_input()
#     get_fac(num)
#
#
#
# def get_user_input():
#     n = int(input('enter number'))
#     return n
#
#
# def get_fac(n):
#     if n < 0:
#         return -1
#     elif n < 2:
#         return 1
#     else:
#         #return n * get_fac(n-1)
#         n = n * get_fac(n-1)
#         print(n)
#
#
#
# if __name__ == '__main__':
#     main()

# print(get_fac(5))

# def round_and_round():
#     print('Again and Again')
#     round_and_round()
#
#
# round_and_round()

