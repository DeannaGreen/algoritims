from flask import Flask, render_template,request
from flask import jsonify
import json
import time
import random
import numpy
from random import randint

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
  co_ords = []
  for k in range (0, 1001, +50):
      list = numpy.random.random_integers(1, 100, k)
      current_time = time.time()
      print(list)
      for i in range((len(list) -1), 0, -1):
          j = random.randint(0, (i + 1))
          list[i], list[j] = list[j], list[i]
      print(list)
      time_now = time.time()
      final_time = time_now - current_time
      co_ords.append([k, final_time])
  return jsonify(co_ords)

@app.route("/my_last")
def my_last():
  co_ords = []
  for i in range (1, 1001, +50):
      list = numpy.random.random_integers(1, 100, i)
      current_time = time.time()
      list[-1]
      time_now = time.time()
      final_time = time_now - current_time
      co_ords.append([i, final_time])
  return jsonify(co_ords)

@app.route("/my_reverse")
def my_reverse():
  co_ords = []
  for k in range (1, 1001, +50):
      list = numpy.random.random_integers(1, 100, k)
      current_time = time.time()
      # print(list)
      i = 0            # first item
      j = len(list)-1   # last item
      while i < j:
          list[i],list[j] = list[j],list[i]
          i += 1
          j -= 1
      # print(list)
      time_now = time.time()
      final_time = time_now - current_time
      co_ords.append([k, final_time])
  return jsonify(co_ords)

@app.route("/students")
def students():
    names = ["john", "bob", "madison", "jenny"]
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
    return "yay"

@app.route("/dupe")

# example: ["car", "dog", "cat", "car", "fish", "dog"] answer:dog car
# loop over each element in the Array
# compare each element to all other elements in the Array
# if they match then print word
# ignore cases of comparing itself
def dupe():
    list = [1, 2, 1]
    dupes = []
    current_time = time.time()
    for i in range(0, (len(list) -1), +1):
        count = 0
        while count < len(list):
            if word != count:
                if list[i] == list[count]:
                    dupe.append(list[i])
                    count += 1
                else:
                    count += 1
            else:
                count += 1
    time_now = time.time()
    final_time = time_now - current_time
    print(dupes)
    return "yay"

@app.route("/dupe2")
def dupe2():
    arr = [1, 2, 3, 2]
    arr_size = len(arr)
    dupes = []

    print("The repeating elements are: ")

    for i in range(0, arr_size):
        if arr[abs(arr[i])] >= 0:
            arr[abs(arr[i])] = -arr[abs(arr[i])]
        else:
            dupes.append(abs(arr[i]))
    print(dupes)
    return jsonify(dupes)

@app.route("/graph")
def graph():
    return render_template ("graph.html")

@app.route("/graph2")
def graph2():
    return render_template ("graph2.html")

def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

if __name__ == "__main__":
  test_sum()
  print("Everything passed")
  app.run()
