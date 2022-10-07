# -*- coding: utf-8 -*-
"""Stack.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19iNZNqNy-Zkz00AB6mM_Na5GDLRhBT5k
"""

from collections import deque

class Stack:
  def __init__(self):
    self.container = deque()
  def push(self, val):
    self.container.append(val)
  def pop(self):
    self.container.pop()
  def is_empty(self):
    return len(self.container) == 0
  def size(self):
    return len(self.container)
  def peek(self):
    return self.container[-1]
  def first(self):
    return self.container[0]

s = Stack()

s.push(1)
s.push(2)
s.push(3)
s.push(4)
print(s.container)

s.pop()

print(s.peek())
print(s.first())

print(s.container)