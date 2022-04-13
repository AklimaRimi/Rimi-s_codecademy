#creating a class
class Patient:
  def __init__(self, name, age,sex,bmi,num_of_children,smoker):
    self.name = name
    self.age = age
    self.sex = sex 
    self.bmi = bmi
    self.num_of_children=num_of_children
    self.smoker = smoker
    # add more parameters here
    #calculate cost using attributes
  def estimated_insurance_cost(self):
    self.estimated_cost = 250 * self.age - 128 * self.sex + 370 * self.bmi + 425 * self.num_of_children + 24000 * self.smoker - 12500
    print("{}’s estimated insurance costs is {} dollars.".format(self.name,self.estimated_cost))
  
  #update an attribute
  def update_age(self,new_age):
    self.age = new_age
    print("{} is now {} years old.",format(self.name,self.age))
    self.estimated_insurance_cost()

   #update attribute
  def update_num_children(self,new_num_children):
    self.num_of_children =new_num_children 
    if self.num_of_children==1:
      print("{} has {} child.".format(self.name,self.num_of_children))
    else:
      print("{} has {} children.".format(self.name,self.num_of_children))
    self.estimated_insurance_cost()

    #create dictionary
  def patient_profile(self):
    patient_information = {}
    patient_information["Name"] = self.name
    patient_information["Age"] = self.age
    patient_information["Sex"] = self.sex
    patient_information["BMI"] = self.bmi
    patient_information["Number of Children"] = self.num_of_children
    patient_information["Smoker"] = self.smoker
    return patient_information


 #instance 
patient1 = Patient("John Doe", 25, 1, 22.2, 0, 0)

#call value / method through instance
print(patient1.update_num_children(1))
print(patient1.patient_profile())
