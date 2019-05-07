from flask import Flask
import time
import random
import numpy
from random import randint
import graph

app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello"

@app.route("/sort")
def sort_time():
  x = randint(1,1000)
  list = numpy.random.random_integers(1, 1000, x)
  # print(list)
  current_time = time.time()
  list.sort()
  time_now = time.time()
  final_time = time_now - current_time
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

if __name__ == "__main__":
  app.run()
