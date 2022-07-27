import typing 

class Employer:

    
    def __init__(self,
                 first_name: str,
                 last_name : str,
                 age       : int,
                 job       : str,
                 salary    : float,
                 bonus     : float,
                 next      = None):
        
        self.first_name = first_name
        self.last_name  = last_name
        self.age        = age
        self.job        = job
        self.salary     = salary
        self.bonus      = bonus 
        self.total_salary  = salary + bonus
        self.next_employer = next

    def apply_bonus(self,amount:float):
        self.bonus = self.bonus + amount
        self.total_salary = self.total_salary + amount
   
x= Employer('Kaisa','Xin',33,'sad',1000,2000)
q= Employer('Jinx','Ela',33,'sad',1000,2000)
w= Employer('Cait','Tula',33,'sad',1000,2000)
e= Employer('Adrien','Guli',33,'sad',1000,2000)
r= Employer('Monica','Bec',33,'sad',1000,2000)

class Department:

    def __init__(self,
                 name: str,
                 next = None):
        
        self.name = name
        self.users = None
        self.next_department = next
       
    def append(self, value:Employer )->None:
        NewEmployer = value
        if self.users is None:
            self.users = NewEmployer
            return
        NewEmployer.next_employer = self.users
        self.users = value
            
    def display_employers_in_department(self):
        loop = self.users
        while loop is not None:
            print(loop.first_name, loop.last_name)
            loop = loop.next_employer

    def remove(self,
               Employers_firstname:str,
               Employers_lastname:str):

        EmpVal = self.users
         
        while (EmpVal is not None):
            if EmpVal.first_name == Employers_firstname:
                if EmpVal.last_name == Employers_lastname:
                    break
            prev  = EmpVal
            EmpVal = EmpVal.next_employer

        if(EmpVal == None):
            return

        prev.next_employer = EmpVal.next_employer
        EmpVal = None
               
    def display_departments(self):
        pass

y = Department('dziki')
z = Department('kozy')
u = Department('adsy')
y.append(x)
y.append(q)
y.append(w)
#y.append(e)
#y.append(r)
#y#.remove('Jinx','Ela')

#y.display_employers_in_department()


class Company:

    Employees    : Employer
    Departments : Department

    def __init__(self):
        
        self.Employers = None
        self.Departments = None

    def add_department(self,
                       department_name:Department):

        NewDepartment = department_name
        
        if self.Departments is None:
            self.Departments = NewDepartment
            return
        NewDepartment.next_department = self.Departments
        self.Departments = department_name

    def delete_department(self,
                          department_name:str):
        
        DepVal = self.Departments
         
        while (DepVal is not None):
            if  DepVal.name == department_name:
                    break
            prev  = DepVal
            DepVal =  DepVal.next_department

        if(DepVal == None):
            return

        prev.next_department = DepVal.next_department
        DepVal = None

    def apply_bonuss(self,
                    employer_firstname:str,
                    employer_lastname:str,
                    bonus:float):

        BonusVal = self.Employers
         
        while (BonusVal is not None):
            print(BonusVal.first_name)
            if BonusVal.first_name == employer_firstname:
                if EmpVal.last_name == employer_lastname:
                    break
        BonusVal.apply_bonus(bonus)
        
    def add_employer(self, name):
        NewEmployer = name
        if self.Employers is None:
            self.Employers = NewEmployer
            return
        NewEmployer.next_employer = self.Employers
        self.Employers = name

    def remove_employer(self,
                Employers_firstname:str,
                Employers_lastname:str):

        EmpVal = self.Employers
         
        while (EmpVal is not None):
            if EmpVal.first_name == Employers_firstname:
                if EmpVal.last_name == Employers_lastname:
                    break
            prev  = EmpVal
            EmpVal = EmpVal.next_employer

        if(EmpVal == None):
            return

        prev.next_employer = EmpVal.next_employer
        EmpVal = None

    def search(self, firstname, lastname):

        EmpVal = self.Departments
        while (EmpVal is not None):
            loop = self.Employers
            while loop is not None:
                if loop.first_name == firstname or loop.last_name == lastname :
                    print("xfdsf")
                    print(EmpVal.name)
                    break
                loop = loop.next_employer
            break
            
    def export_to_txt_file(self,employer_name):
        pass


    def display_departments(self):
        loop = self.Departments
        while loop is not None:
            print(loop.name)
            loop = loop.next_department

    def display_employers(self):
        loop = self.Employers
        while loop is not None:
            print(loop.first_name,loop.last_name,loop.total_salary)
            loop = loop.next_employer
        
        
c= Company()
c.add_department(y)
c.add_department(z)
c.delete_department('dziki')
c.display_departments()
c.add_employer(q)
c.add_employer(w)
c.add_employer(e)
c.display_employers()
#c.remove_employer('Jinx','Ela')
#print("x")
#c.display_employers()
#c.apply_bonuss('Jinx','Ela',2000)
#c.search('Cait','Tula')
    
    
