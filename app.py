from flask import Flask, render_template,request
from flask import jsonify
import json
import time
import random
import numpy
from random import randint
import matplotlib.pyplot as plt, mpld3

app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello"

@app.route("/sort")
def sort_time():
  co_ords = []
  for i in range (0, 1001, +50):
      list = numpy.random.random_integers(1, 1000, i)
      current_time = time.time()
      list.sort()
      time_now = time.time()
      final_time = time_now - current_time
      co_ords.append([i, final_time])
  print(co_ords)
  return jsonify(co_ords)

@app.route("/last")
def last_time():
  co_ords = []
  for i in range (1, 1001, +50):
      list = numpy.random.random_integers(1, 1000, i)
      current_time = time.time()
      list[-1]
      time_now = time.time()
      final_time = time_now - current_time
      co_ords.append([i, final_time])
  return jsonify(co_ords)

@app.route("/reverse")
def reverse_time():
  co_ords = []
  for i in range (1, 1001, +50):
      list = numpy.random.random_integers(1, 1000, i)
      current_time = time.time()
      list[:] = list[::-1]
      time_now = time.time()
      final_time = time_now - current_time
      co_ords.append([i, final_time])
  return jsonify(co_ords)

@app.route("/shuffle")
def shuffle_time():
  co_ords = []
  for i in range (1, 1001, +50):
      list = numpy.random.random_integers(1, 1000, i)
      current_time = time.time()
      random.shuffle(list)
      time_now = time.time()
      final_time = time_now - current_time
      co_ords.append([i, final_time])
  return jsonify(co_ords)


@app.route("/my_shuffle")
def my_shuffle():
  x = randint(1,100)
  x_co_ord.append(x)
  list = numpy.random.random_integers(1, 100, x)
  current_time = time.time()
  print(list)
  for i in range((len(list) -1), 0, -1):
      j = random.randint(0, (i + 1))
      list[i], list[j] = list[j], list[i]
  print(list)
  time_now = time.time()
  final_time = time_now - current_time
  y_co_ord.append(final_time)
  print(x_co_ord)
  print(y_co_ord)
  return str(final_time) + " seconds and " + str(x) + " elements in array"

@app.route("/my_last")
def my_last():
  x = randint(1,100)
  x_co_ord.append(x)
  list = numpy.random.random_integers(1, 100, x)
  current_time = time.time()
  list[-1]
  time_now = time.time()
  final_time = time_now - current_time
  y_co_ord.append(final_time)
  print(x_co_ord)
  print(y_co_ord)
  return str(final_time) + " seconds and " + str(x) + " elements in array"

@app.route("/my_reverse")
def my_reverse():
  x = randint(1,100)
  x_co_ord.append(x)
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
  y_co_ord.append(final_time)
  print(x_co_ord)
  print(y_co_ord)
  return str(final_time) + " seconds and " + str(x) + " elements in array"

@app.route("/students")
def students():
    names = ["john", "bob", "madison", "jenny"]
    x_co_ord.append(len(names))
    current_time = time.time()
    for name in range(0, (len(names) -1), +1):
        count = 0
        while count < len(names):
            if name != count:
                print("pair: " + names[name] + " and " + names[count])
                count += 1
            else:
                count += 1
    time_now = time.time()
    final_time = time_now - current_time
    y_co_ord.append(final_time)
    print(x_co_ord)
    print(y_co_ord)
    return "yay"

@app.route("/dupe")
def dupe():
    words = ["car", "dog", "cat", "car", "fish", "dog"]
    x_co_ord.append(len(words))
    current_time = time.time()
    for word in range(0, (len(words) -1), +1):
        count = 0
        while count < len(words):
            if word != count:
                # print(words[word])
                # print(words[count])
                if words[word] == words[count]:
                    print("dulicate word: " + words[word])
                    count += 1
                else:
                    count += 1
            else:
                count += 1
    time_now = time.time()
    final_time = time_now - current_time
    y_co_ord.append(final_time)
    print(x_co_ord)
    print(y_co_ord)
    return "yay"

@app.route("/graph")
def graph():
    return render_template ("graph.html")

if __name__ == "__main__":
  app.run()
