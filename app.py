from flask import Flask, render_template,request
from flask import jsonify
import json
import time
import random
import numpy
from random import randint
import collections

app = Flask(__name__)

@app.route("/")
def hello():
  return render_template ("home.html")

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

def my_shuffle2():
  list = [1, 2, 3, 4]
  for i in range((len(list) -1), 0, -1):
    j = random.randint(0, (i + 1))
    list[i], list[j] = list[j], list[i]
  return str(list)

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

def my_reverse2():
    list = [1, 2, 3, 4]
    i = 0            # first item
    j = len(list)-1   # last item
    while i < j:
      list[i],list[j] = list[j],list[i]
      i += 1
      j -= 1
    return str(list)

@app.route("/students")
def students():
    names = ["john", "bob", "madison"]
    pairs = []
    current_time = time.time()
    for name in range(0, (len(names) -1), +1):
        count = 0
        while count < len(names):
            if name != count:
                # print("pair: " + names[name] + " and " + names[count])
                pairs.append([names[name], names[count]])
                count += 1
            else:
                count += 1
    time_now = time.time()
    final_time = time_now - current_time
    # print(pairs)
    return str(pairs)

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
def dupe2(arr = numpy.random.random_integers(1, 5, 6)):
    # arr = numpy.random.random_integers(1, 5, 6)
    arr_size = len(arr)
    dupes = []
    # print(arr)

    # print("The repeating elements are: ")

    for i in range(0, arr_size):
        if arr[abs(arr[i])] >= 0:
            arr[abs(arr[i])] = -arr[abs(arr[i])]
        else:
            dupes.append(abs(arr[i]))
    # print(dupes)
    return str(dupes)

@app.route("/dupe3")
def dupe3():
    arr = [1, 2, 1]
    for i in range(0, 2):
        if arr[i] in list:
            print(arr[i])
    return "yay"

@app.route("/common")
def common():
    a= "the the cat in the bag"

    wordcount = {}

    for word in a.lower().split():
        word = word.replace(".","")
        word = word.replace(",","")
        word = word.replace(":","")
        word = word.replace("\"","")
        word = word.replace("!","")
        word = word.replace("â€œ","")
        word = word.replace("â€˜","")
        word = word.replace("*","")
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
    # Print most common word
    n_print = 2
    print("\nOK. The {} most common words are as follows\n".format(n_print))
    word_counter = collections.Counter(wordcount)
    for word, count in word_counter.most_common(n_print):
        print(word, ": ", count)
    return str(wordcount)

@app.route("/sort01")
def sort01():
    list = [1, 0, 1, 0, 0]
    zero = []
    one = []
    for i in list:
        if i == 0:
            zero.append(i)
        else:
            one.append(i)
    sorted_list = zero + one
    # print(sorted_list)
    return str(sorted_list)

@app.route("/sorted")
def sorted():
    data_list = [-5, -23, 5, 0, 23, -6, 23, 67]
    new_list = []

    while data_list:
        minimum = data_list[0]  # arbitrary number in list
        for x in data_list:
            if x < minimum:
                minimum = x
        new_list.append(minimum)
        data_list.remove(minimum)

    print(new_list)
    return str(new_list)

@app.route("/sum")
def sum(arr = [15, 2, 4, 8, 9, 5, 10, 23], n = 8, sum = 21):
    for i in range(n):
        curr_sum = arr[i]
        j = i+1
        while j <= n:
            if curr_sum == sum:
                print ("Sum found between")
                print("indexes %d and %d"%( i, j-1))
                return "true"
            if curr_sum > sum or j == n:
                break
            curr_sum = curr_sum + arr[j]
            j += 1
    print ("No subarray found")
    return "false"

@app.route("/graph")
def graph():
    return render_template ("graph.html")

@app.route("/graph2")
def graph2():
    return render_template ("graph2.html")

if __name__ == "__main__":
  app.run()
