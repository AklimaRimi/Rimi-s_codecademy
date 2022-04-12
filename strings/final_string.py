medical_data = \
"""Marina Allison   ,27   ,   31.1 , 
#7010.0   ;Markus Valdez   ,   30, 
22.4,   #4050.0 ;Connie Ballard ,43 
,   25.3 , #12060.0 ;Darnell Weber   
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1 
,#3022.0   ;   Vinay Padilla,24,   
26.9 ,#4620.0 ;Meredith Santiago, 51   , 
29.3 ,#16330.0;   Andre Mccarty, 
19,22.7 , #2900.0 ; 
Lorena Hodson ,65, 33.1 , #19370.0; 
Isaac Vu ,34, 24.8,   #7045.0"""

# Add your code here
#print(medical_data)
updated_medical_data= medical_data.replace('#','$')
print(updated_medical_data)

# replace a letter
num_records =0
for i in updated_medical_data:
  if i[0] =='$':
    num_records+=1

print('\n\nThere are {} medical records in the data.'.format(num_records))

#splitting by ;

medical_data_split  = updated_medical_data.split(';')

print('\n\n\n'+str(medical_data_split))


#again splitting by ,
medical_records =[]
for i in  medical_data_split:
  medical_records.append(i.split(','))

print(medical_records)


#Cleaning blank spaces and store value
medical_records_clean=[]

for i in medical_records:
  record_clean=[]
  for j in i:
    record_clean.append(j.strip())
    record_clean[0]=record_clean[0].upper()

  medical_records_clean.append(record_clean)

print(medical_records_clean)

#arrange 4 values by their name

names =[]
ages =[]
bmis =[]
insurance_costs=[]

for i in medical_records_clean:
  names.append(i[0])
  ages.append(i[1])
  bmis.append(i[2])
  insurance_costs.append(i[3])



total_bmi =0
for i in bmis:
  total_bmi += float(i)


print('\n\n\n Total BMI: {}'.format(total_bmi))

print('\n\n\nAverage BMI: {}'.format(total_bmi/len(bmis)))


#Print all informations

for i in range(len(ages)):
  print('{} is {} years old with a BMI of {} and an insurance cost of {}'.format(names[i],ages[i],bmis[i],insurance_costs[i]))

