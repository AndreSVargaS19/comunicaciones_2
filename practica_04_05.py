from gnuradio import gr
from gnuradio import filter
from gnuradio import qtgui
from PyQt5 import Qt
import sys,sip 
import manager_blocks as misbloques
from gnuradio import analog
from gnuradio import blocks

#################################################################################

class flujograma(gr.top_block):
	def __init__(self):
		gr.top_block.__init__(self)
		n= 262144
		samp_rate =50000
		src = blocks.wavfile_source('/home/vargas/Descargas/mi_voz.wav', True)
		resampler = filter.rational_resampler_fff(
                interpolation=samp_rate,
                decimation=44100,
         
        )
		str2vec=blocks.stream_to_vector(gr.sizeof_float*1, n)
		e_fft=misbloques.e_vector_fft_square_ff(n,samp_rate)
		v_avg=misbloques.vector_average_hob(n,10000)
		snk = qtgui.time_sink_f(n,samp_rate,"",1)
		vsnk = qtgui.vector_sink_f(
			n,
			-samp_rate/2.,
			(samp_rate*1.0)/n,
			"frecuencia [Hz]",
			"Magnitud",
			"Densida espectral de potencia",
			1
		)
		vsnk.enable_autoscale(True)
		snk.enable_autoscale(True)


#################################################################################################
		
		
 		self.connect(src, resampler, str2vec, e_fft, v_avg, vsnk)
 		self.connect(src, snk)
 		
 		
#################################################################################################
	
	
		pyobjv = sip.wrapinstance(vsnk.pyqwidget(), Qt.QWidget)
		pyobjv.show()
		pyobj = sip.wrapinstance(snk.pyqwidget(), Qt.QWidget)
		pyobj.show()
 
def main():
    qapp = Qt.QApplication(sys.argv)
    simulador_de_la_envolvente_compleja = flujograma()
    simulador_de_la_envolvente_compleja.start()
    qapp.exec_()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
