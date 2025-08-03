class Dispositivo:
    def __init__(self, nombre, ip, mac, servicios, estado = "desconectado"):
        self.nombre = nombre
        self.ip = ip
        self.mac = mac
        self.servicios = servicios
        self.estado = estado
    
    def conectar(self):
        self.estado = "activo"
        print(f'El dispositivo se está conectando... El dispositivo está {self.estado}')

    def desconectar(self):
        self.estado = "desconectado"
        print(f'El dispositivo está {self.estado}')

    def __str__(self):
        return f"Dispositivo: {self.nombre}\nIP: {self.ip}\nMAC: {self.mac}\nServicios: {len(self.servicios)}\nEstado: {self.estado}"
    
    def __len__(self):
        return len(self.servicios)
    
    def __eq__(self, otro):
        return self.ip == otro.ip

class DispositivoCritico(Dispositivo):
    def __init__(self, nombre, ip, mac, servicios, nivel_riesgo, estado="desconectado"):
        super().__init__(nombre, ip, mac, servicios, estado)
        self.nivel_riesgo = nivel_riesgo
    
    def riesgo(self):
        if self.nivel_riesgo.upper() == "ALTO":
            print(f'El nivel de riesgo del dispositivo {self.nombre} es {self.nivel_riesgo}. ATENCION URGENTE')

def mostrar_red(lista_dispositivos):
    print('ESTADO DE LA RED LOCAL:')
    for dispositivo in lista_dispositivos:
        print(dispositivo)
        if isinstance(dispositivo, DispositivoCritico):
            dispositivo.riesgo()
        print("-" * 40)


d1 = Dispositivo('Router', '192.168.100.10', 'F3:20:EA', [20, 21, 22], estado='Desconectado')
d2 = Dispositivo('Switch', '192.168.100.20', 'F4:21:EE', [20, 21, 22], estado='Desconectado')
d3 = Dispositivo('HUB', '192.168.100.30', 'F5:22:EB', [20,21 ,22], estado='Desconectado')
dc1 = DispositivoCritico('Firewall', '192.168.100.40', 'A1:B2:C3', [22, 443], 'ALTO')

red = [d1, d2, d3]
red.append(dc1)

d1.conectar()
d1.desconectar()

d2.conectar()
d2.desconectar()

d3.conectar()
d3.desconectar()

print(d1)
print(d2)
print(d3)

print(d1 == d2)
print(len(d1))
print(len(d2))
print(len(d3))

dc1.riesgo()

mostrar_red(red)