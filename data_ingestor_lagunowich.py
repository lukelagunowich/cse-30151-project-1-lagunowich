import csv

# Data ingestor for CSV file with SAT's in CNF form
    # Input(s): CSV file with SAT's in CNF form
    # Output(s): Generator that outputs satisfiability, number of variables, number of clauses, and SAT in CNF to be input into DPLL or DumbSat
def read_sat_cnf_csv(fname):
    with open(fname, mode='r', encoding='utf-8-sig') as f:
        csvf = csv.reader(f)
        curr_sat_cnf = None
        variables = None
        clauses = None
        sat = None
        for line in csvf:
            if line[0] == 'c':
                if curr_sat_cnf is not None:
                    yield sat, variables, clauses, curr_sat_cnf
                curr_sat_cnf = [] # Current SAT in CNF form (when c is read)
                sat = line[-1]
            elif line[0] == 'p': # Get SAT statistics *when p is read)
                variables = int(line[-2])
                clauses = int(line[-1])
            else:
                clause = [int(l) for l in line[0:2]] # Read clause
                curr_sat_cnf.append(clause) # Add clause to current SAT in CNF form
        yield sat, variables, clauses, curr_sat_cnf

if __name__ == '__main__':
    for tup in read_sat_cnf_csv('2SAT.cnf.csv'):
        print(tup)
