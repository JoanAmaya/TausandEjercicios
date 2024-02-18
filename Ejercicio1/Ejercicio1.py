from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.animation as animation
import datetime as dt
import numpy as np




class MainApp(QMainWindow):
    def __init__(self, parent= None ,*args):

        #-----------Inicializacion de la ventana---------------
        super(MainApp,self).__init__(parent=parent)
        #self.setMinimumSize(700,500)
        #self.setMaximumSize(1100,500)
        self.setFixedSize(800,600)
        self.setWindowTitle("Aplicación contar el tiempo")
        self.setStyleSheet("background-color: white;")
        self.valor_conteo=0
        self.listaregistros=[]
        #-----------Fin parametros de inicializacion-----------

        #-----------labelLoginSimple---------------
        #Login
        login_font = QFont("Segoe UI", 24)
        login_font.setBold(True)
        self.label = QLabel("Gráfica de conteo temporal:", self)
        self.label.setFont(login_font)
        self.label.setAlignment(Qt.AlignCenter)  # Centrar el título
        self.label.setGeometry(0, 50, 800, 80)
        #-----------BotonReiniciar---------------
        self.botonReiniciar = QPushButton("Reiniciar contador", self)
        self.botonReiniciar.setGeometry(100, 465, 190, 60)
        self.botonReiniciar.setFont(QFont("Segoe UI", 12))
        self.botonReiniciar.setStyleSheet(
            """
            QPushButton {
                background-color: #4CAF50;
                border: none;
                color: white;
                padding: 10px 24px;
                text-align: center;
                text-decoration: none;
                font-size: 16px;
                margin: 4px 2px;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #45a049;
                color: white;
            }
            """
        )
        self.botonReiniciar.clicked.connect(self.slot_Reboot)
        #-----------FinBotonReiniciar---------------

        #-----------BotonCerrarPrograma---------------
        self.botonCerrar = QPushButton("Fin de programa", self)
        self.botonCerrar.setGeometry(500, 465, 190, 60)
        self.botonCerrar.setFont(QFont("Segoe UI", 12))
        self.botonCerrar.setStyleSheet(
            """
            QPushButton {
                background-color: #CD4E31;
                border: none;
                color: white;
                padding: 10px 24px;
                text-align: center;
                text-decoration: none;
                font-size: 16px;
                margin: 4px 2px;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #AB2506;
                color: white;
            }
            """
        )
        self.botonCerrar.clicked.connect(self.slot_Close)
        #-----------FinBotonCerrarPrograma---------------

        #-----------BotonVerregistros---------------
        self.botonRegistro = QPushButton("Ver registros teclas", self)
        self.botonRegistro.setGeometry(300, 465, 190, 60)
        self.botonRegistro.setFont(QFont("Segoe UI", 12))
        self.botonRegistro.setStyleSheet(
            """
            QPushButton {
                background-color: #0397E7;
                border: none;
                color: white;
                padding: 10px 24px;
                text-align: center;
                text-decoration: none;
                font-size: 16px;
                margin: 4px 2px;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #067CBC;
                color: white;
            }
            """
        )
        self.botonRegistro.clicked.connect(self.slot_registros)
        
        #-----------FinBotonVerregistros---------------

        #-----------InsercionGrafico---------------
        self.grafico = Canvas(self,self.valor_conteo)
        self.grafico.setGeometry(50, 150, 700, 300)
        #-----------FinInsercionGrafico------------

        #-----------InsercionTimer---------------
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_graph)
        self.timer.start(50)  
        #-----------FinInsercionTimer------------
 

    #-----------InicioFunciones---------------
        

    #-----------FuncionBotonCerrarPrograma---------------
    def slot_Close(self):
        self.close() 
    #-----------FinFuncionBotonCerrarPrograma---------------
        
    #-----------FuncionBotonCerrarPrograma---------------
    def slot_Reboot(self):
        self.valor_conteo=0 
    #-----------FinFuncionBotonCerrarPrograma---------------
        

    #-----------EventoPresiondeTecla---------------
    def keyPressEvent(self,event):
        string_temp=""
        match event.text():
            case '1':
                self.valor_conteo+=1
                string_temp="Se presionó la tecla "+event.text()+" en la fecha "+str(dt.datetime.now())
                self.listaregistros.append(string_temp) 
            case '2': 
                self.valor_conteo+=2 
                string_temp="Se presionó la tecla "+event.text()+" en la fecha "+str(dt.datetime.now())
                self.listaregistros.append(string_temp) 
            case '3': 
                self.valor_conteo+=3 
                string_temp="Se presionó la tecla "+event.text()+" en la fecha "+str(dt.datetime.now())
                self.listaregistros.append(string_temp) 
            case '4': 
                self.valor_conteo+=4 
                string_temp="Se presionó la tecla "+event.text()+" en la fecha "+str(dt.datetime.now())
                self.listaregistros.append(string_temp) 
            case '5': 
                self.valor_conteo+=5     
                string_temp="Se presionó la tecla "+event.text()+" en la fecha "+str(dt.datetime.now())
                self.listaregistros.append(string_temp) 
                    
        
    #-----------FinEventoPresiondeTecla---------------
        
    #-----------FuncionActualizarGrafico---------------  
    def update_graph(self):
        
        self.grafico.update_plot()  
        self.grafico.setvalor(self.valor_conteo)
        
        
    #-----------FinFuncionActualizarGrafico---------------    

    #-----------FuncionVerRegistros------------------
    def slot_registros(self):
        ventana_registros = QDialog(self)
        ventana_registros.setWindowTitle("Registros de Teclas")
        layout = QVBoxLayout(ventana_registros)
        registros = self.listaregistros 
        lista_registros = QListWidget()
        lista_registros.addItems(registros)
        layout.addWidget(lista_registros)
        ventana_registros.exec_()
    #-----------FinFuncionVerRegistros---------------     
        

    #-----------FinFunciones---------------

#-----------------------------NuevaClase------------------------------------------
    #-----------------------------------------#
    #-------------CreacionGrafico-------------#
    #-----------------------------------------#

#Explicacion funcionamiento: Se crean 3 listas una para guardar los valores de la suma(ys)
#Otra para guardar el valor total en segundos desde que empezo el 2024(xsa)
#Otra para hacer la resta con los valores anteriormente tomados respecto al actual(xs)
#Se toma en la variable valor la suma que viene desde la clase MainApp 
#Posteriormente se obtiene en valor actual a partir de calculos simples el valor en segundos
#desde que empezo 2024 hasta la fecha actual, ese valor se registra en la ultima posicion de xsa
# y todos los valores se corren una casilla a la izquierda.
#Luego se resta a los demas valores de segundos el valor actual (Note que xs inicia todo en 1 esto es para que
#los valores que sean iguales a 1 no se tengan en cuenta en la resta y tampoco se grafique).
#Por ultimo, se grafican los valores en una animacion que se refresca cada 50 ms y se ejecuta cada 50 ms en la
#clase MainApp.
                


class Canvas(FigureCanvas):
    def __init__(self, parent,valor, *args):
        fig, self.ax = plt.subplots(figsize=(10, 4))
        fig.subplots_adjust(bottom=0.2)
        super(Canvas, self).__init__(fig)
        self.xs = np.zeros(650)+1 
        self.xsa=np.zeros(650)
        self.ys = np.zeros(650)
        self.ax.grid(True)
        self.valor=valor
        self.valor_actual=0
        self.referencia_segundos=dt.datetime(year=2024,month=1,day=1)
        self.ani = animation.FuncAnimation(fig, self.animate, interval=50)
        self.setParent(parent)    
    #--------------CreacionFuncionesParaAnimar---------------------    
    def setvalor(self,valor):
        self.valor=valor    
    def animate(self, i):
        
        hora_actual = dt.datetime.now()
        self.valor_actual=hora_actual-self.referencia_segundos
        self.valor_actual=self.valor_actual.total_seconds()
        self.xsa[:-1] = self.xsa[1:]
        self.xsa[-1] = self.valor_actual
        self.xs = np.where(self.xsa!=0,self.xsa-self.valor_actual,1)
        self.ys[:-1] = self.ys[1:]
        
        
        if self.ys[-1]!=self.valor:
             
             self.ys[-2]=self.ys[-1]
             self.ys[-1]=self.valor
             self.xs[-2]=self.xs[-1]
        else:
             self.ys[-1]=self.valor
        graficarx=self.xs[self.xs<=0]
        graficary=self.ys[self.xs<=0]     
     
    
        self.ax.clear()
        self.ax.plot(graficarx, graficary,linewidth=5.0,color='red')
        self.ax.set_title('Gráfica suma acumulada',fontweight='bold')
        self.ax.set_ylabel('Suma acumulada',fontweight='bold')
        self.ax.set_xlabel('Tiempo (s)',fontweight='bold')
        self.ax.tick_params(axis='x', rotation=45, labelsize=10)
        self.ax.tick_params(axis='y', labelsize=10)  
        self.ax.set_xlim(left=-30-0.1, right=max(self.xs)+0.01)
        self.ax.set_ylim(bottom=0-0.1, top=max(self.ys)+1)
        self.ax.grid(True)

    def update_plot(self):
        self.ani.new_frame_seq()

    #--------------FinCreacionFuncionesParaAnimar---------------------    


    #-----------------------------------------#
    #-------------FinCreacionGrafico----------#
    #----------------------------------------- #  
#-----------------------------FinNuevaClase------------------------------------------        

#Ejecucion de la aplicacion

if __name__=="__main__":
        
    app= QApplication([])
    window= MainApp()
    window.show() 
    app.exec_()

