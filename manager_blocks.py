from gnuradio import gr
import numpy as np
class e_add_cc(gr.sync_block):  
    """Aqui debes explicar como funciona el bloque, los parametros usados. En este caso particular el proposito es que esta clase sirva como ejemplo o plantilla para otras clase. La idea es que cada vez que vayas a crear una clase para un bloque GNU Radio vuelvas aqui ya que no es facil memorizar todos los detalles para crear un bloque GNU Radio. En todo caso, el ejemplo consiste en un bloque para una suma escalada de dos senales complejas. Por lo tanto hay dos senales de entrada y una de salida. Si escala=0.5 lo que se logra es promediar las dos senales"""

    def __init__(self, escala=0.5):
 
       
        gr.sync_block.__init__(
            self,
 
            # Lo siguiente es para definir el nombre que tendra nuestro bloque para los usuarios de GRC
            name='Plantilla_para_crear_bloques_cc', 
 
           
            in_sig=[np.complex64,np.complex64], 
            out_sig=[np.complex64]
        )
 
        # las variables que entran como parametros del bloque deben ser declaradas nuevamente asi:
        self.escala=escala
 
        
        self.coef = 1.0
 
    # La funcion work() siempre debe estar presente en un bloque. Es alli donde estara la logica del bloque 
    
    def work(self, input_items, output_items):
        in0 = input_items[0]
        in1 = input_items[1]
        out0 = output_items[0]
        out0[:]=(in0+in1)*self.escala/self.coef
        return len(out0)
 
####################################################
##     clase e_add_ff                             ##
####################################################
class e_add_ff(gr.sync_block):  
    """consiste en un bloque para una suma escalada de dos senales reales. Por lo tanto hay dos senales de entrada y una de salida. Si escala=0.5 lo que se logra es promediar las dos senales"""
     
    def __init__(self, escala=0.5):
 
        gr.sync_block.__init__(
            self,
            name='e_add_ff', 
            in_sig=[np.float32,np.float32], 
            out_sig=[np.float32]
        )
        self.escala=escala
    def work(self, input_items, output_items):
        in0 = input_items[0]
        in1 = input_items[1]
        out0 = output_items[0]
        out0[:]=(in0+in1)*self.escala
        return len(out0)
#######################################################################
##   clase para calcular la FFT en magnitud de una senal vectorial   ##
#######################################################################

class e_vector_fft_ff(gr.sync_block):
    """calcula la fft en magnitud a una senal vectorial de N muestras y emtrega N muestras del espectro. N deber ser potencia de 2"""
 
    def __init__(self, N=128):  
        gr.sync_block.__init__(
            self,
            name='e_vector_fft_ff', 
             in_sig=[(np.float32,N)],
            out_sig=[(np.float32,N)]
        )
        self.N = N
 
    def work(self, input_items, output_items):
        in0 = input_items[0]
        out0 = output_items[0]
        out0[:]=abs(np.fft.fftshift(np.fft.fft(in0,self.N),1)) 
        return len(output_items[0])

####    FFT en magnitud al cuadrado   ####

class  e_vector_fft_square_ff(gr.sync_block):  

	def __init__(self, N,samp_rate):  
		self.N = N
		self.samp_rate=samp_rate
		gr.sync_block.__init__(
		    self,
		    name='e_vector_fft_square_ff',   
		    in_sig=[(np.float32,N)],
		    out_sig=[(np.float32,N)]
		)
		
	def work(self, input_items, output_items):
		in0 = input_items[0]
		out0 = output_items[0]
		out0[:]=(self.samp_rate/(2.0*self.N))*(abs(np.fft.fftshift(np.fft.fft(in0,self.N),1))) 
		return len(output_items[0])





class vector_average_hob(gr.sync_block):
    """
    El bloque vector_averager_hob recibe una senal con tramas de tamano fijo de N valores y va entregando una trama del mismo tamano que corresponde a la trama media de todas las tramas que va recibiendo. 
Los parametros usados son:
N:        Es el tamano del vector o trama
Nensayos: Es el umbral que limita el numero maximo de promedios correctamente realizados. Cuando a la funcion se le ha invocado un numero de veces mayor a Nensayos, el promedio continua realizandose, pero considerando que el numero de promedios realizado hasta el momento ya no se incrementa, sino que es igual a Nensayos. 
    """
 
    def __init__(self, N, Nensayos):
        gr.sync_block.__init__(self, name="vector_average_hob", in_sig=[(np.float32, N)], out_sig=[(np.float32, N)])
 
        # Nuestras variables especificas
        self.N=N
        self.Nensayos=np.uint64=Nensayos
        self.med=np.empty(N,dtype=np.float64)
        self.count=np.uint64=0
 
    def work(self, input_items, output_items):
 
        # Traduccion de matrices 3D a 2D 
        in0 = input_items[0]
        out0=output_items[0]
        
        # El tamano de la matriz in0 es L[0]xL[1]=L[0]xN
        L=in0.shape
 
        # conteo de funciones muestras (filas de matriz) procesadas
        if self.count < self.Nensayos:
            self.count += L[0] 
 
        # La media de las funciones muestras (filas de matriz) que tiene in0
        mean=in0.mean(0)    
 
        # ajuste de la media ya calculada, con la media de in0
        self.med = (self.med*(self.count-L[0])+mean*L[0])/self.count
 
        # Entrega de resultado
        out0[:]=self.med
        return len(out0)

