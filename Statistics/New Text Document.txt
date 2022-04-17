names = ["Judith", "Abel", "Tyson", "Martha", "Beverley", "David", "Anabel"]
estimated_insurance_costs = [1000.0, 2000.0, 3000.0, 4000.0, 5000.0, 6000.0, 7000.0]
actual_insurance_costs = [1100.0, 2200.0, 3300.0, 4400.0, 5500.0, 6600.0, 7700.0]

# Add your code here
total_cost =0
for i in actual_insurance_costs:
  total_cost += i

average_cost =total_cost/len(estimated_insurance_costs)

print('Average Insurance Cost: '+str(average_cost)+' dollars.')


for i in range(len(names)):
 # print('The insurance cost for '+str(names[i])+' is '+str(actual_insurance_costs[i])+' dollars.')
  if actual_insurance_costs[i]> average_cost:
    print('The insurance cost for '+str(names[i])+' is above average.')
  else:
    print('The insurance cost for '+str(names[i])+' is equal to the average')

updated_estimated_costs =[i*(11/10) for i in estimated_insurance_costs ]

print(updated_estimated_costs)





















