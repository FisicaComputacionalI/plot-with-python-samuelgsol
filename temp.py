00#Python usa librerias como matplotlib con objetos predeterminados como pyplot que tienen propiedades que permiten enviar las instrucciones a la maquina de una forma resumida. Matplotlib es una libreria para crear graficas en 2 dimensiones. 
import matplotlib.pyplot as plt
#Construimos el objeto plt introduciendo valores que se grafican contra el numero de entrada. Por ejemplo si queremos graficar el crecimiento de un material por dia en centimetros. 
plt.plot([1,1,1,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3])
#Con esta isntruccion colocamos un titulo al eje Y de la grafica.
plt.xlabel('mis anios de vida') 
plt.ylabel('numero de hermanos partir de mi nacimiento')
plt.ylim(0,6)
#Con esta isntruccion guardamos la imagen con el formato que queramos.
plt.savefig('temp.png')
#Con esta instruccion mostramos la figura. 
plt.show()

