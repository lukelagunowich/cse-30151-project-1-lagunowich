import time

from data_ingestor_lagunowich import read_sat_cnf_csv
from code_dpll_lagunowich import dpll

# Initialize output file for storing DPLL performance
output_file = open('output_time_dpll_lagunowich.csv', 'w')
s = 'sat?'+','+'num_variables'+','+'num_clauses'+','+'time' # stores satisfiability, number of variables, number of clauses, and time
output_file.write(s)
output_file.write('\n')

# Utilize read_sat_cnf_csv generator function to generate test cases from data file (for performance testing)
for sat_cnf in read_sat_cnf_csv('data_file_lagunowich.cnf.csv'):
    _, variables, clauses, curr_sat_cnf = sat_cnf[0], sat_cnf[1], sat_cnf[2], sat_cnf[3]
    start = time.time() # Start timer
    flag = dpll(curr_sat_cnf) # Solve 2-SAT problem, determine satisfiability
    end = time.time() # End timer
    exec_time=int((end-start)*1e6)
    if flag:
        result = 'S'
    else:
        result = 'U'
    s = result+','+str(variables)+','+str(clauses)+','+str(exec_time) # store result in output file
    output_file.write(s)
    output_file.write('\n')

output_file.close()
