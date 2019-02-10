#!/usr/bin/env python
# coding: utf-8

# In[93]:


from tkinter import *
from backend.GoalsList import *
import json

def show_entry_fields(event=None):

    global i
    Label(master, text=e.get()).grid(row=i)
    i = i+1
    g.goalList.append(e.get())
    e.delete(0,len(e.get()))

master = Tk()


Label(master, text="Goals for Today?").grid(row=0)

g = Goals()

e = Entry(master)

e.grid(row=0, column=1)

i = 1
#Button(master, text='Enter', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
e.bind('<Return>', show_entry_fields)

mainloop()
with open('goals.txt', 'w') as json_goals:
    json.dump(getGoals(g),json_goals)