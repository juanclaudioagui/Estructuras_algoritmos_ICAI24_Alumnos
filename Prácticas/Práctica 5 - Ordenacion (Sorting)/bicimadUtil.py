import csv
from dataclasses import dataclass
import datetime
import time

# lets define a data class as a proxy for the record
@dataclass
class Trayecto:
    """Class for keeping track of an item in inventory."""
    date             : datetime.date         # fecha del viaje
    hour             : int                   # hora de inicio del viaje
    ageRange         : int                   # Rango de edad de los usuarios.
    user_type        : int                   # Tipo de Usuario.
    idumplug_station : int                   # Estación de origen.
    idplug_station   : int                   # Estación de destino.
    travel_time_secs : int                   # Tiempo del trayecto. (Secs)
    file_id          : str                   # Fichero.- Nombre del fichero de donde se ha obtenido la información.

    def __gt__(self, trayecto):
        # returns true if self is > other, by whatever criteria you want to  use
        raise NotImplementedError
    
    
def readTrayectos(iSize):
    sizes = [1000,5000,10000,100000,500000,1000000]
    csvFile = f'bicimad_{sizes[iSize]}.csv'
    print (f"Reading file {csvFile}")
    trayectos = []
    with open(csvFile) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {" //  ".join(row)}')
                line_count += 1
            else:
                try:
                    trayectos.append(Trayecto(datetime.datetime.strptime(row[0],"%d/%m/%Y").date(), int(row[1]),int(row[2]),int(row[3]),int(row[4]),int(row[5]),int(row[6]),row[7]))
                    line_count += 1
                except:
                    print (f"Badly formated row {row}")
        print(f'Processed {line_count} Trayectos.')
        # print ( "Here are the first 10....")
        # for trayecto in trayectos[:10]: print (trayecto)
        return trayectos
    
# test Comment if this bothers you !
trayectos = readTrayectos(2)
trayectos.sort()
for i, tr in enumerate(trayectos[:100]):
    print (i, tr)