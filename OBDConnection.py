import obd

class OBDConnection:

    
    def __init__(self):
        pass

    def look_for_connections(self):
        self.ports = obd.scan_serial()
        return self.ports
    
    def connect_to_port(self, connectingport):
        self.connection = obd.OBD(self.ports[connectingport])
        if self.check_connection_status():
            print("Connection Successfull!")
        else:
            print("Connection Failed!")
    
    def check_connection_status(self):
        self.connection_status = self.connection.is_connected() #check to see if the device is connected to elm and car with iginition on

    def send_command(self, obd_command):
        if self.check_connection_status():
            response_val = self.connection.query(obd.commands[obd_command])
            return response_val
    
    





    




