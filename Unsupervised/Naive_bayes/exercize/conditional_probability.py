import numpy as np

p_disease_and_correct = (1.0/100000.0) * .99

p_no_disease_and_incorrect = (1-(1.0/100000.0))*(1-.99)

print(p_disease_and_correct)
print(p_no_disease_and_incorrect)
