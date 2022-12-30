import obd


def connectOBD():
    ports = obd.scan_serial()
    print (ports)
    connection = obd.OBD()
    connection_status = connection.is_connected();

    if connection_status:
        print ('connected succesfully!')
    else:
        print ('connection failed...')

    return connection, connection_status #returns physical connection that
#is used to query the car for commands and boolean status of connection

        

def getSpeed(connection, status, mainCanvas, whichArc):
    if status:
        speed = connection.query(obd.commands.SPEED) #asks the car for the value
        convert = -((speed.value.magnitude/200)*180)
        mainCanvas.itemconfig(whichArc, extent = convert)

        mainCanvas.after(10, getSpeed, connection, status, mainCanvas, whichArc)



##connection2, status, mainCanvas
##connection3, connection_status = connectOBD()
##getSpeed(connection3, connection_status)
