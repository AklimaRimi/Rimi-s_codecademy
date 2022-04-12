# Add your code here

medical_costs={}

medical_costs.update({'Marina':6607.0,'Vinay':3225.0})

medical_costs.update({'Connie':8886.0,'Isaac':16444.0,'Valentina':6420.0})

print(medical_costs)
medical_costs['Vinay'] = 3325.0
print(medical_costs)
total_cost =0
for i in medical_costs.values():
  total_cost += i

print('\n\nAverage Insurance Cost: {}'.format(total_cost/len(medical_costs)))

names =['Marina','Vinay','Connie','Issac','Valentina']
ages = [27,24,43,35,52]
zipped_ages =zip(names,ages)

names_to_ages ={key:value for key,value in zipped_ages}

print('\n\n'+str(names_to_ages))

marina_age = names_to_ages.get('Marina')
print("\n\nMarina's age is {}".format(marina_age))

medical_records ={}

medical_records['Marina'] = {"Age": 27, "Sex": "Female", "BMI": 31.1, "Children": 2, "Smoker": "Non-smoker", "Insurance_cost": 6607.0}


medical_records["Vinay"] = {"Age": 24, "Sex": "Male", "BMI": 26.9, "Children": 0, "Smoker": "Non-smoker", "Insurance_cost": 3225.0}
medical_records["Connie"] = {"Age": 43, "Sex": "Female", "BMI": 25.3, "Children": 3, "Smoker": "Non-smoker", "Insurance_cost": 8886.0}
medical_records["Isaac"] = {"Age": 35, "Sex": "Male", "BMI": 20.6, "Children": 4, "Smoker": "Smoker", "Insurance_cost": 16444.0}
medical_records["Valentina"] = {"Age": 52, "Sex": "Female", "BMI": 18.7, "Children": 1, "Smoker": "Non-smoker", "Insurance_cost": 6420.0}

print('\n\n\n')
print(medical_records)




print("\n\nConnie's insurance cost is {} dollars.".format(medical_records['Connie']['Insurance_cost']))



medical_records.pop('Vinay')

for k,v in medical_records.items():
  print("{} is a {} year old {} {} with a BMI of {} and insurance cost of {}".format(k,v['Age'],v['Sex'],v['Smoker'],v['BMI'],v['Insurance_cost']))





