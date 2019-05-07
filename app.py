from flask import Flask
import time
import random
import numpy
from random import randint
import matplotlib.pyplot as plt

app = Flask(__name__)

global x_co_ord
x_co_ord = []

global y_co_ord
y_co_ord = []

@app.route("/")
def hello():
  return "Hello"

@app.route("/sort")
def sort_time():
  x = randint(1,1000)
  x_co_ord.append(x)
  list = numpy.random.random_integers(1, 1000, x)
  current_time = time.time()
  list.sort()
  time_now = time.time()
  final_time = time_now - current_time
  y_co_ord.append(final_time)
  print(x_co_ord)
  print(y_co_ord)
  return str(final_time) + " seconds and " + str(x) + " elements in array"

@app.route("/last")
def last_time():
  x = randint(1,1000)
  list = numpy.random.random_integers(1, 1000, x)
  current_time = time.time()
  list[-1]
  time_now = time.time()
  final_time = time_now - current_time
  return str(final_time) + " seconds and " + str(x) + " elements in array"

@app.route("/reverse")
def reverse_time():
  x = randint(1,1000)
  list = numpy.random.random_integers(1, 1000, x)
  current_time = time.time()
  list[:] = list[::-1]
  time_now = time.time()
  final_time = time_now - current_time
  return str(final_time) + " seconds and " + str(x) + " elements in array"

@app.route("/shuffle")
def shuffle_time():
  x = randint(1,1000)
  list = numpy.random.random_integers(1, 1000, x)
  current_time = time.time()
  random.shuffle(list)
  time_now = time.time()
  final_time = time_now - current_time
  return str(final_time) + " seconds and " + str(x) + " elements in array"

@app.route("/my_shuffle")
def my_shuffle():
  x = randint(1,100)
  list = numpy.random.random_integers(1, 100, x)
  current_time = time.time()
  print(list)
  for i in range((len(list) -1), 0, -1):
      j = random.randint(0, (i + 1))
      list[i], list[j] = list[j], list[i]
  print(list)
  time_now = time.time()
  final_time = time_now - current_time
  return str(final_time) + " seconds and " + str(x) + " elements in array"

@app.route("/my_last")
def my_last():
  x = randint(1,100)
  list = numpy.random.random_integers(1, 100, x)
  current_time = time.time()
  list[-1]
  time_now = time.time()
  final_time = time_now - current_time
  return str(final_time) + " seconds and " + str(x) + " elements in array"

@app.route("/my_reverse")
def my_reverse():
  x = randint(1,100)
  list = numpy.random.random_integers(1, 100, x)
  current_time = time.time()
  print(list)
  i = 0            # first item
  j = len(list)-1   # last item
  while i < j:
      list[i],list[j] = list[j],list[i]
      i += 1
      j -= 1
  print(list)
  time_now = time.time()
  final_time = time_now - current_time
  return str(final_time) + " seconds and " + str(x) + " elements in array"

@app.route("/students")
def students():
    names = ["john", "bob", "madison", "jenny"]
    for name in range(0, (len(names) -1), +1):
        count = 0
        while count < len(names):
            if name != count:
                print("pair: " + names[name] + " and " + names[count])
                count += 1
            else:
                count += 1
    return "yay"


if __name__ == "__main__":
  app.run()
