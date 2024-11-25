import sqlite3

#Skaber variable "con"
con = sqlite3.connect('projektnt.db')
print ('Database åbnet')

#Sletter tabellerne så vi kan lave dem senere opdaterede
try:
    con.execute("""DROP TABLE IF EXISTS Process;""")
    con.execute("""DROP TABLE IF EXISTS Machine;""")
    con.execute("""DROP TABLE IF EXISTS Material;""")
    con.execute("""DROP TABLE IF EXISTS Cost;""")
    con.execute("""DROP TABLE IF EXISTS MaterialSpecification;""")
    con.execute("""DROP TABLE IF EXISTS PostProcess;""")


    print('Tabel slettet')

except Exception as e:
    print('Fejl ved sletning af tabel')

#Laver de nye tabeller
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
    

    con.execute("""CREATE TABLE MaterialSpecification (
        SpecificationID INTEGER PRIMARY KEY,
        ProcessID INTEGER,
        MachineID INTEGER,
        MaterialID INTEGER,
        Cost DECIMAL(10, 2),
        Unit TEXT,
        FOREIGN KEY (ProcessID) REFERENCES Process(ProcessID),
        FOREIGN KEY (MachineID) REFERENCES Machine(MachineID),
        FOREIGN KEY (MaterialID) REFERENCES Material(MaterialID),
        UNIQUE(ProcessID, MachineID, MaterialID));""")


    con.execute("""CREATE TABLE PostProcess (
        PostProcessID INTEGER PRIMARY KEY,
        PostProcessName TEXT,
        ProcessID INTEGER,
        Description TEXT,
        TimeConstant DECIMAL(10, 2),
        FOREIGN KEY (ProcessID) REFERENCES Process(ProcessID));""")


    print('Tabel oprettet')
except Exception as e:
    print('Tabellen findes allerede')

#Tabellerne og deres indhold
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


con.execute("""INSERT INTO MaterialSpecification (SpecificationID, ProcessID, MachineID, MaterialID, Cost, Unit) VALUES(1, 1, 1, 1, 66.66, '$/kg');""")
con.execute("""INSERT INTO MaterialSpecification (SpecificationID, ProcessID, MachineID, MaterialID, Cost, Unit) VALUES(2, 1, 2, 2, 343.00, 'unit');""")
con.execute("""INSERT INTO MaterialSpecification (SpecificationID, ProcessID, MachineID, MaterialID, Cost, Unit) VALUES(3, 2, 3, 3, 149.00, '$/L');""")
con.execute("""INSERT INTO MaterialSpecification (SpecificationID, ProcessID, MachineID, MaterialID, Cost, Unit) VALUES(4, 2, 3, 4, 149.00, '$/L');""")
con.execute("""INSERT INTO MaterialSpecification (SpecificationID, ProcessID, MachineID, MaterialID, Cost, Unit) VALUES(5, 2, 5, 5, 2800.00, '$/10kg');""")
con.execute("""INSERT INTO MaterialSpecification (SpecificationID, ProcessID, MachineID, MaterialID, Cost, Unit) VALUES(6, 2, 3, 6, 299.00, '$/L');""")
con.execute("""INSERT INTO MaterialSpecification (SpecificationID, ProcessID, MachineID, MaterialID, Cost, Unit) VALUES(7, 3, 7, 7, 67.50, '$/kg');""")
con.execute("""INSERT INTO MaterialSpecification (SpecificationID, ProcessID, MachineID, MaterialID, Cost, Unit) VALUES(8, 3, 7, 8, 60.00, '$/kg');""")
con.execute("""INSERT INTO MaterialSpecification (SpecificationID, ProcessID, MachineID, MaterialID, Cost, Unit) VALUES(9, 3, 7, 9, 50.00, '$/kg');""")
con.execute("""INSERT INTO MaterialSpecification (SpecificationID, ProcessID, MachineID, MaterialID, Cost, Unit) VALUES(10, 4, 10, 10, 400.00, '$/kg');""")
con.execute("""INSERT INTO MaterialSpecification (SpecificationID, ProcessID, MachineID, MaterialID, Cost, Unit) VALUES(11, 4, 10, 11, 30.00, '$/kg');""")
con.execute("""INSERT INTO MaterialSpecification (SpecificationID, ProcessID, MachineID, MaterialID, Cost, Unit) VALUES(12, 5, 13, 13, 250.00, '$/kg');""")


con.execute("""INSERT INTO PostProcess (PostProcessID, PostProcessName, ProcessID, Description, TimeConstant) VALUES(1, 'Support Removal FDM', 1, 'Support removal time labor constant for FDM', 0.05);""")
con.execute("""INSERT INTO PostProcess (PostProcessID, PostProcessName, ProcessID, Description, TimeConstant) VALUES(2, 'Support Removal FDM', 2, 'Support removal time labor constant for FDM', 0.03);""")
con.execute("""INSERT INTO PostProcess (PostProcessID, PostProcessName, ProcessID, Description, TimeConstant) VALUES(3, 'Support Removal SLA', 3, 'Support removal time labor constant for SLA', 0.08);""")
con.execute("""INSERT INTO PostProcess (PostProcessID, PostProcessName, ProcessID, Description, TimeConstant) VALUES(4, 'Support Removal DLP', 4, 'Support removal time labor constant for DLP', 0.05);""")
con.execute("""INSERT INTO PostProcess (PostProcessID, PostProcessName, ProcessID, Description, TimeConstant) VALUES(5, 'Support Removal DLP', 5, 'Support removal time labor constant for DLP', 0.05);""")
con.execute("""INSERT INTO PostProcess (PostProcessID, PostProcessName, ProcessID, Description, TimeConstant) VALUES(6, 'Support Removal SLS', 6, 'Support removal time labor constant for SLS', 0.00);""")
con.execute("""INSERT INTO PostProcess (PostProcessID, PostProcessName, ProcessID, Description, TimeConstant) VALUES(7, 'Support Removal SLM', 7, 'Support removal time labor constant for SLM', 0.11);""")
con.execute("""INSERT INTO PostProcess (PostProcessID, PostProcessName, ProcessID, Description, TimeConstant) VALUES(8, 'Support Removal SLM', 8, 'Support removal time labor constant for SLM', 0.11);""")
con.execute("""INSERT INTO PostProcess (PostProcessID, PostProcessName, ProcessID, Description, TimeConstant) VALUES(9, 'Support Removal SLM', 9, 'Support removal time labor constant for SLM', 0.11);""")


con.commit()

inp = ''

#Kommandoer til at blandt andet vise data
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

        c.execute('SELECT * FROM MaterialSpecification;')
        for p in c:
            print('MaterialSpecification: {}'.format(p))

        c.execute('SELECT * FROM PostProcess;')
        for p in c:
            print('PostProcess: {}'.format(p))
