#Importe os e cv2 no arquivo CreateVideo.py.
import os
import cv2

#Defina uma variável path (caminho) para a pasta Images.
path = "Images/"

#Crie uma variável de lista chamada Images = [ ].
images = [ ]

#Use o loop for para verificar cada arquivo da pasta usando os.listdir(path).
for file in os.listdir(path):
    name, ext = os.splitext(file)

#Crie uma condição if para verificar se a extensão do arquivo corresponde à extensão da imagem.
if ext in ['.gif', '.png', '.jpg', '.jpeg', '.jfif']:
    file_name = path+"/"+file

    print(file_name)

    images.append(file_name)

    count =len(images)

    frame = cv2.imread(images[0])

    width,height,channels = frame.shape

    size = (width,height)

    print(size)

    out = cv2.VideoWriter('project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

#Crie um loop for para adicionar as imagens ao VideoWriter.
for i in range(0, count-1):
    frame = cv2.imread(images[i])
    out.write(frame)

#Imprima uma mensagem para saber que o vídeo está completo, como print(“Concluído”).
print("Concluído")