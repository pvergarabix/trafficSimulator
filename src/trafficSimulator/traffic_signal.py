from datetime import datetime
from .client import *

class TrafficSignal:
    def __init__(self, roads, config={}):
        # Initialize roads
        self.roads = roads

        # Set default configuration
        self.set_default_config()
        # Update configuration
        for attr, val in config.items():
            setattr(self, attr, val)

        # Agregados PV
        self.start_time = datetime.now()
        self.notificado = False        
        self.cliente = Client()                
        
        # Calculate properties
        self.init_properties()

    def set_default_config(self):
        self.cycle = [(True, False), (False, True)]
        self.slow_distance = 50
        self.slow_factor = 0.4
        self.stop_distance = 15
        self.current_cycle_index = 0
        self.last_t = 0
        #self.cliente.conect()
        

    def init_properties(self):
        for i in range(len(self.roads)):
            for road in self.roads[i]:
                road.set_traffic_signal(self, i)

    @property
    def current_cycle(self):
        return self.cycle[self.current_cycle_index]
    
    def update(self, sim):
        cycle_length = 120 
        valor_actual = int(self.current_cycle_index)       
        k = (sim.t // cycle_length) % 2
        nuevo_valor = int(k) 
        if valor_actual != nuevo_valor:
            end_time = datetime.now()
            print(f"Ocurre el cambio de estados de semaforo. Tiempo transcurrido: {(end_time - self.start_time).seconds}")
            self.cliente.upd_send_info() #mandamos señal de cambiar de estado para sincronizar 
            self.start_time = datetime.now() # reiniciamos nomas..
            self.notificado = False
        #print(f"Nuevo update: cycle_length: {cycle_length}, k: {k}, sim.t: {sim.t}, cycle_length: {cycle_length} ")
        self.current_cycle_index = int(k)
