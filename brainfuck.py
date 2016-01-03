#!/usr/bin/env python3

import sys

ptr = 0
cells = {}
stack = []
i = 0

f = open(sys.argv[1])
content = f.read()

def readcell():
    global ptr, cells
    cell = 0
    if ptr in cells:
        cell = cells[ptr]
    return cell

def right():
    global ptr
    ptr = ptr + 1

def left():
    global ptr
    ptr = ptr - 1
    
def increment():
    global ptr, cells
    if ptr in cells:
        cells[ptr] = cells[ptr] + 1
    else:
        cells[ptr] = 1
        
def decrement():
    global ptr, cells
    if ptr in cells:
        cells[ptr] = cells[ptr] - 1
    else:
        cells[ptr] = -1

def putchar():
    global ptr, cells
    char = readcell()
    print(chr(char),end='')
    
def readchar():
    global ptr, cells
    char = sys.stdin.read(1)
    cells[ptr] = ord(char)
    
def startloop():
    global ptr, cells, i
    cell = readcell()
        
    if cell == 0:
        opened = 1
        while opened > 0 and i < len(content):
            c = content[i]
            i = i + 1
            if c == '[':
                opened = opened + 1
            elif c == ']':
                opened = opened - 1
    else:
        stack.append(i)
        i = i + 1
    
def endloop():
    global ptr, cells, i
    cell = readcell()
    
    if cell != 0:
        # move to start of loop
        i = stack.pop()
    else:
        i = i + 1
    
cmds = {
    '>': right,
    '<': left,
    '+': increment,
    '-': decrement,
    '.': putchar,
    ',': readchar
}

while i < len(content):
    c = content[i]
    if c in cmds:
        cmds[c]()
        i = i + 1
    elif c == '[':
        startloop()
    elif c == ']':
        endloop()
    else:
        i = i + 1
    
print()    