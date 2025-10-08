class NetworkDevice:
    def __init__(self, name, ip_address, device_type):
        self.name = name
        self.ip_address = ip_address
        self.device_type = device_type

    def showInfo (self):
        print("dispositivo: "+self.name+" | Ip: "+self.ip_address+" | Tipo:"+ self.device_type)

    def pingTest(self):
        print("Realizando ping al dispositivo: "+self.name+", "+self.ip_address+", "+self.device_type)

        
dev1 = NetworkDevice("Router1", "10.0.0.1", "Router")
dev1.showInfo()
dev1.pingTest()

dev2 = NetworkDevice("Switch1", "10.0.0.2", "Switch")
dev2.showInfo()
dev2.pingTest()

dev3 = NetworkDevice("Firewall1", "10.0.0.3", "Firewall")
dev3.showInfo()
dev3.pingTest()