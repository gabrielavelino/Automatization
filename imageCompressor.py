from tkinter import *
from PIL import Image
import os


def compressImage():
    # Get the path of the image to be compressed
    path = entrada.get()
    # print(path)
    pathOut = entrada.get()

    for file in os.listdir(path):
        if file.endswith(".jpeg"):
            # print(file)
            # Open the image
            img = Image.open(path + '/' + file)
            # Resize the image
            img = img.resize((480, 640), Image.ANTIALIAS)
            # clean the name of the file
            cleanName = os.path.splitext(file)[0]
            # Save the image
            img.save(pathOut + '/' + cleanName + '_compressed.jpg', optimize=True, quality=50)

def deleteFile():
    # Get the path of the image to be compressed
    path = entrada.get()
    # print(path)

    for file in os.listdir(path):
        if file.endswith(".jpeg"):
            print(file)
            # os.remove(path + '/' + file)

# Create the App
app = Tk()

app.title("Image Compressor")
app.geometry('600x300')
app.resizable(False, False)
app.configure(background='white')


texto = Label(app, text="Compressor de imagens (JPEG,JPG,PNG)", background='white', foreground='black', font=('Arial', 14))
texto.grid(row=0, column=1, padx=120, pady=50)

textoEntrada = Label(app, text="Copie o caminho do arquivo e cole abaixo:", background='white', foreground='black', font=('Arial', 10))
textoEntrada.place(x=100, y=110)

entrada = Entry(app,background='#DCDCDC')
entrada.place(x=100, y=130, width=400, height=20)

botao = Button(app, text="COMPRIMIR", command=compressImage)
botao.grid(row=1, column=1, padx=10, pady=50)

botao2 = Button(app, text="DELETAR", command=deleteFile)
botao2.place(x=400, y=178.5, width=80, height=25)


app.mainloop()