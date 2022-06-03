import numpy as np
p_positive_given_disease = .99 #positively given disease

p_disease = (1.0/100000) # disease probability


p_positive = .00001+.01


p_disease_given_positive = (p_positive_given_disease*p_disease)/p_positive

print(p_disease_given_positive)
