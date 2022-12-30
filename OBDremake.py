import obd

ports = obd.scan_serial()
print(ports)
connection = obd.OBD(ports[0])

# send the command, and parse the response
response = connection.query(obd.commands.RPM)

print(response.value)  # returns unit-bearing values thanks to Pint
