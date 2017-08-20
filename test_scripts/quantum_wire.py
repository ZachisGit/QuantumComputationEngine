import numpy as np

in_vec = np.array([1.0,0])
h_matrix = np.array([[1.0,1],[1,-1]])/np.sqrt(2.0)

print "in_vec:",in_vec
print "H_Matrix:",h_matrix

def run_prob(qbit):
    length_0_comp = np.abs(qbit[0])**2.0
    if np.random.uniform() < length_0_comp:
        return np.array([1.,0])
    else:
        return np.array([0,1.])


prob_0 = 0
prob_1 = 0
compute_steps = 10000

# Graph => ----
for i in range(compute_steps):
    out_vec = run_prob(in_vec)
    if out_vec[0] == 1.:
        prob_0 += 1
    else:
        prob_1 += 1

final_vec = np.array([prob_0,prob_1])/float(prob_0+prob_1)
print 'Final Probs:',final_vec
