import sqlite3

con = sqlite3.connect('projektnt.db')
print ('Database åbnet')

try:
    con.execute("""DROP TABLE IF EXISTS Process;""")
    con.execute("""DROP TABLE IF EXISTS Machine;""")
    con.execute("""DROP TABLE IF EXISTS Material;""")
    con.execute("""DROP TABLE IF EXISTS Cost;""")


    print('Tabel slettet')

except Exception as e:
    print('Fejl ved sletning af tabel')

try:   
    con.execute("""CREATE TABLE Process (
        ProcessID INT PRIMARY KEY,
        ProcessName VARCHAR(50) NOT NULL UNIQUE);""")


    con.execute("""CREATE TABLE Machine (
        MachineID INT PRIMARY KEY,
        MachineName VARCHAR(50) NOT NULL UNIQUE,
        ProcessID INT,
        FOREIGN KEY (ProcessID) REFERENCES Process(ProcessID));""")


    con.execute("""CREATE TABLE Material (
        MaterialID INT PRIMARY KEY,
        MaterialName VARCHAR(50) NOT NULL UNIQUE,
        Density DECIMAL(5, 2));""")


    con.execute("""CREATE TABLE Cost (
        CostID INT PRIMARY KEY,
        MaterialID INT,
        Unit VARCHAR(10),
        Cost DECIMAL(10, 2),
        FOREIGN KEY (MaterialID) REFERENCES Material(MaterialID));""")

    print('Tabel oprettet')
except Exception as e:
    print('Tabellen findes allerede')


con.execute("""INSERT INTO Process (ProcessID, ProcessName) VALUES(1, 'FDM');""") 
con.execute("""INSERT INTO Process (ProcessID, ProcessName) VALUES(2, 'SLA');""")
con.execute("""INSERT INTO Process (ProcessID, ProcessName) VALUES(3, 'SLS');""")
con.execute("""INSERT INTO Process (ProcessID, ProcessName) VALUES(4, 'SLM');""")
con.execute("""INSERT INTO Process (ProcessID, ProcessName) VALUES(5, 'DLP');""")


con.execute("""INSERT INTO Machine (MachineID, MachineName, ProcessID) VALUES(1, 'Ultimaker 3', 1);""")
con.execute("""INSERT INTO Machine (MachineID, MachineName, ProcessID) VALUES(2, 'Fortus 360mc', 1);""")
con.execute("""INSERT INTO Machine (MachineID, MachineName, ProcessID) VALUES(3, 'Form2', 2);""")
con.execute("""INSERT INTO Machine (MachineID, MachineName, ProcessID) VALUES(4, 'ProX 950', 2);""")
con.execute("""INSERT INTO Machine (MachineID, MachineName, ProcessID) VALUES(5, 'EOSINT P800', 3);""")
con.execute("""INSERT INTO Machine (MachineID, MachineName, ProcessID) VALUES(6, 'EOSm100 or 400-4', 4);""")
con.execute("""INSERT INTO Machine (MachineID, MachineName, ProcessID) VALUES(7, '3D Systems Figure 4', 5);""")

con.execute("""INSERT INTO Material (MaterialID, MaterialName, Density) VALUES(1, 'ABS', 1.10);""")
con.execute("""INSERT INTO Material (MaterialID, MaterialName, Density) VALUES(2, 'Ultem', 1.27);""")
con.execute("""INSERT INTO Material (MaterialID, MaterialName, Density) VALUES(3, 'Clear Resin', 1.18);""")
con.execute("""INSERT INTO Material (MaterialID, MaterialName, Density) VALUES(4, 'Dental Model Resin', 1.18);""")
con.execute("""INSERT INTO Material (MaterialID, MaterialName, Density) VALUES(5, 'Accura Xtreme', 1.18);""")
con.execute("""INSERT INTO Material (MaterialID, MaterialName, Density) VALUES(6, 'Casting Resin', 1.18);""")
con.execute("""INSERT INTO Material (MaterialID, MaterialName, Density) VALUES(7, 'PA2200', 0.93);""")
con.execute("""INSERT INTO Material (MaterialID, MaterialName, Density) VALUES(8, 'PA12', 1.01);""")
con.execute("""INSERT INTO Material (MaterialID, MaterialName, Density) VALUES(9, 'Alumide', 1.36);""")
con.execute("""INSERT INTO Material (MaterialID, MaterialName, Density) VALUES(10, 'Ti6Al4V', 4.43);""")
con.execute("""INSERT INTO Material (MaterialID, MaterialName, Density) VALUES(11, 'SSL316', 8);""")
con.execute("""INSERT INTO Material (MaterialID, MaterialName, Density) VALUES(12, 'Problack 10', 1.07);""")

con.execute("""INSERT INTO Cost (CostID, MaterialID, Unit, Cost) VALUES(1, 1, '$/kg', 66.66);""")
con.execute("""INSERT INTO Cost (CostID, MaterialID, Unit, Cost) VALUES(2, 2, 'unit', 343.00);""")
con.execute("""INSERT INTO Cost (CostID, MaterialID, Unit, Cost) VALUES(3, 3, '$/L', 149.00);""")
con.execute("""INSERT INTO Cost (CostID, MaterialID, Unit, Cost) VALUES(4, 4, '$/L', 149.00);""")
con.execute("""INSERT INTO Cost (CostID, MaterialID, Unit, Cost) VALUES(5, 5, '$/10kg', 2800.00);""")
con.execute("""INSERT INTO Cost (CostID, MaterialID, Unit, Cost) VALUES(6, 6, '$/L', 299.00);""")
con.execute("""INSERT INTO Cost (CostID, MaterialID, Unit, Cost) VALUES(7, 7, '$/kg', 67.50);""")
con.execute("""INSERT INTO Cost (CostID, MaterialID, Unit, Cost) VALUES(8, 8, '$/kg', 60.00);""")
con.execute("""INSERT INTO Cost (CostID, MaterialID, Unit, Cost) VALUES(9, 9, '$/kg', 50.00);""")
con.execute("""INSERT INTO Cost (CostID, MaterialID, Unit, Cost) VALUES(10, 10, '$/kg', 400.00);""")
con.execute("""INSERT INTO Cost (CostID, MaterialID, Unit, Cost) VALUES(11, 11, '$/kg', 30.00);""")
con.execute("""INSERT INTO Cost (CostID, MaterialID, Unit, Cost) VALUES(12, 12, '$/kg', 250.00);""")

con.commit()

inp = ''

print('')
print('Kommandoer: ')
print(' vis - Viser en masse fra Database')
print(' q - Afslut Program')

while not inp.startswith('q'):
    inp = input('>')

    if inp == 'vis':
        c = con.cursor()
        c.execute('SELECT * FROM Process;')
        for p in c:
            print('Process: {}'.format(p))

        c.execute('SELECT * FROM Machine;')
        for p in c:
            print('Machine: {}'.format(p))
        
        c.execute('SELECT * FROM Material;')
        for p in c:
            print('Material: {}'.format(p))

        c.execute('SELECT * FROM Cost;')
        for p in c:
            print('Cost: {}'.format(p))