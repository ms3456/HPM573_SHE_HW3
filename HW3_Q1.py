class Patient:
    def __init__(self, name):
        self.name = name

class EmergencyPatient(Patient):
    def __init__(self, name):
        Patient.__init__(self, name)
        self.cost = 1000

    def discharge(self):
            print self.name, 'is discharged from emergency department.'

class HospitalizedPatient(Patient):
    def __init__(self,name):
        Patient.__init__(self, name)
        self.cost = 2000
    def discharge(self):
        print self.name, 'is discharged from hospitalization.'

class Hospital():
    cost = 0
    patients = []
    def admit(self, patient):
        self.patients.append(patient)

    def discharge_all(self):
        for person in self.patients:
            person.discharge()

    def get_total_cost(self):
        for person in self.patients:
            self.cost += person.cost
        print 'The total operating cost for today is:', self.cost, 'dollars'

# Admitting 2 hospitalized patients
myhospital = Hospital()
Patient1 = HospitalizedPatient("John")
myhospital.admit(Patient1)
Patient2 = HospitalizedPatient("Dan")
myhospital.admit(Patient2)

# Admitting 3 emergency patients
Patient3 = EmergencyPatient("Mary")
myhospital.admit(Patient3)
Patient4 = EmergencyPatient("Kim")
myhospital.admit(Patient4)
Patient5 = EmergencyPatient("Kenny")
myhospital.admit(Patient5)


myhospital.discharge_all()

myhospital.get_total_cost()
