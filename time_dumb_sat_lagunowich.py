import time

from data_ingestor_lagunowich import read_sat_cnf_csv

# SOURCE: DumbSAT.py
def check(Wff,Nvars,Nclauses,Assignment):
# Run thru all possibilities for assignments to wff
# Starting at a given Assignment (typically array of Nvars+1 0's)
# At each iteration the assignment is "incremented" to next possible
# At the 2^Nvars+1'st iteration, stop - tried all assignments
    Satisfiable=False
    while (Assignment[Nvars+1]==0):
        # Iterate thru clauses, quit if not satisfiable
        for i in range(0,Nclauses): #Check i'th clause
            Clause=Wff[i]
            Satisfiable=False
            for j in range(0,len(Clause)): # check each literal
                Literal=Clause[j]
                if Literal>0: Lit=1
                else: Lit=0
                VarValue=Assignment[abs(Literal)] # look up literal's value
                if Lit==VarValue:
                    Satisfiable=True
                    break
            if Satisfiable==False: break
        if Satisfiable==True: break # exit if found a satisfying assignment
        # Last try did not satisfy; generate next assignment)
        for i in range(1,Nvars+2):
            if Assignment[i]==0:
                Assignment[i]=1
                break
            else: Assignment[i]=0
    return Satisfiable

# SOURCE: DumbSAT.py
def test_wff(wff,Nvars,Nclauses):
    Assignment=list((0 for x in range(Nvars+2)))
    start = time.time() # Start timer
    SatFlag=check(wff,Nvars,Nclauses,Assignment)
    end = time.time() # End timer
    exec_time=int((end-start)*1e6)
    return [wff,Assignment,SatFlag,exec_time]

# Initialize output file for storing DumbSat performance
output_file = open('output_time_dumb_sat_lagunowich.csv', 'w')
s = 'sat?'+','+'num_variables'+','+'num_clauses'+','+'time'
output_file.write(s)
output_file.write('\n')

# Utilize read_sat_cnf_csv generator function to generate test cases from data file (for performance testing)
for sat_cnf in read_sat_cnf_csv('data_file_lagunowich.cnf.csv'):
    _, variables, clauses, curr_sat_cnf = sat_cnf[0], sat_cnf[1], sat_cnf[2], sat_cnf[3]
    results = test_wff(curr_sat_cnf, variables, clauses) # Solve 2-SAT problem
    _, _, flag, exec_time = results[0], results[1], results[2], results[3] # Get results
    if flag: # Determine satisfiability
        result = 'S'
    else:
        result = 'U'
    s = result+','+str(variables)+','+str(clauses)+','+str(exec_time) # store result in output file
    output_file.write(s)
    output_file.write('\n')

output_file.close()

