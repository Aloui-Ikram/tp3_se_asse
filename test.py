from tkinter import *
import numpy as np
import random

def gridtab(l, pages):
    c = len(pages)
    index = 0
    for ligne in range(l):
        for colonne in range(c + 1):
            if ligne == 0 and colonne == 0:
                Button(Mafenetre, text='/', borderwidth=1, font=('times', 14, 'bold'), width=5, bg='gray').grid(row=ligne, column=colonne, sticky=EW)
            elif ligne == 0 and colonne != 0:
                Button(Mafenetre, text=pages[index], borderwidth=1, font=('times', 14, 'bold'), width=5, bg="white").grid(row=ligne, column=colonne, sticky=EW)
                listmessage.insert(END, 'P' + str(pages[index]))
                index += 1
            elif ligne != 0 and colonne == 0:
                Button(Mafenetre, text='PM' + str(ligne), borderwidth=1, font=('times', 14, 'bold'), width=5, bg='white').grid(row=ligne, column=colonne, sticky=EW)
            else:
                Button(Mafenetre, text='  ', borderwidth=1, font=('times', 14, 'bold'), width=5).grid(row=ligne, column=colonne, sticky=EW)

def addmemory(memory, c, cl):
    for ligne in range(size):
        try:
            if cl >= 0 and cl == ligne:
                Button(Mafenetre, text=memory[ligne], borderwidth=1, font=('times', 14, 'bold'), width=5, bg='green').grid(row=ligne + 1, column=c + 1, sticky=EW)
            else:
                Button(Mafenetre, text=memory[ligne], borderwidth=1, font=('times', 14, 'bold'), width=5).grid(row=ligne + 1, column=c + 1, sticky=EW)
        except:
            Button(Mafenetre, text='  ', borderwidth=1, font=('times', 14, 'bold'), width=5, bg='#F5413E').grid(row=ligne + 1, column=c + 1, sticky=EW)

def FIFO():
    count = 0
    memory = []
    DP = 0
    cl = -1
    fifoIndex = 0
    c = 0

    for page in pages:
        if memory.count(page) == 0 and count < size:
            memory.append(page)
            cl = count
            count += 1
            DP += 1
        elif memory.count(page) == 0 and count == size:
            memory[fifoIndex] = page
            cl = fifoIndex
            fifoIndex = (fifoIndex + 1) % size
            DP += 1
        elif memory.count(page) > 0:
            # already in memory
            cl = -1
        addmemory(memory, c, cl)
        c += 1

    return DP

def lrupage(memory, lst):
    max_len = len(lst)
    for MI, i in enumerate(memory):
        index = max_len - lst[::-1].index(i) - 1
        if index < max_len:
            max_len = index
            lruIndex = MI
    return lruIndex



# Creating the main window
fenetre = Tk()
fenetre.title("TP4")
fenetre.geometry('1400x700')
fenetre.resizable(False, False)



Mafenetre = Frame(fenetre)
Mafenetre.pack(pady=20)

pages = np.random.randint(0, 10, 10)
pages = list(pages)
size = int(5)

commande = Frame(fenetre, bg="red")
commande.pack()

messageframe = Frame(fenetre)
messageframe.pack()

scroll = Scrollbar(messageframe, orient=VERTICAL)
listmessage = Listbox(messageframe, width=10, height=15, bg='white', yscrollcommand=scroll.set, font=('times', 10, 'bold'))

scroll.config(command=listmessage.yview)
scroll.pack(side=RIGHT, fill=Y)

listmessage.pack(pady=20)

fifo = Button(commande, text='FIFO', command=FIFO, width=10, bg='pink', fg='white')
fifo.config(font=('times', 14, 'bold'))
fifo.pack()





gridtab(size + 1, pages)
fenetre.mainloop()