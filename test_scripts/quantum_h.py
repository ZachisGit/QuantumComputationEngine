import numpy as np

in_vec = np.array([1.0,0])
h_matrix = np.array([[1.0,1],[1,-1]])/np.sqrt(2.0)

print np.abs(np.matmul(h_matrix,np.matmul(in_vec,h_matrix)))**2

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
compute_steps = 100000

# Graph => ----H--
step_0_out = np.zeros([compute_steps,2],dtype=np.float32)
for i in range(compute_steps):
    step_0_out[i] = run_prob(in_vec)

step_1_out = np.zeros([compute_steps,2],dtype=np.float32)
for i in range(compute_steps):
    vec = run_prob(np.matmul(h_matrix,step_0_out[i]))
    step_1_out[i] = vec

for i in range(compute_steps):
    out_vec = step_1_out[i]
    if out_vec[0] == 1.:
        prob_0 += 1
    else:
        prob_1 += 1

final_vec = np.array([prob_0,prob_1])/float(prob_0+prob_1)
print 'Final Probs:',final_vec
