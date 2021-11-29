import webbrowser
import tkinter

# Objeto root representará o Tk
root = tkinter.Tk( )
root.title('Abrir Navegador')
root.geometry('300x200')

def google():
    webbrowser.open('www.google.com.br')

mygoogle = tkinter.Button(root, text='Abrir o Google', command=google).pack(pady=20)
root.mainloop()