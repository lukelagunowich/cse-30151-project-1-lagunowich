
# 2-SAT DPLL Solver

# Algorithm
    # Input(s): SAT in CNF form 
    # Output(s): Satisfiability boolean
def dpll(sat_cnf):
    while ((l := get_clause_lengths(sat_cnf)) != 0): 
        sat_cnf = unit_propogate(l, sat_cnf) # Unit propogation: https://en.wikipedia.org/wiki/Unit_propagation
    while ((l := check_pure_literal(sat_cnf)) != 0):
        sat_cnf = pure_literal_assign(l, sat_cnf) # pure literal elimination
    if len(sat_cnf) == 0:
        return True # satisfiable 
    if any([len(c)==0 for c in sat_cnf]):
        return False # unsatisfiable
    l = select_literal(get_literals(sat_cnf)) # select literal (room for optimization here)
    return dpll(assign_true(l, sat_cnf)) or dpll(assign_true(-l, sat_cnf)) # recursion

# Helper functions

# Returns literal from unit clauses
    # Input(s): SAT in CNF form
    # Output(s): Literal from first occurence of unit clause or 0 if no unit clauses
def get_clause_lengths(sat_cnf):
    for clause in sat_cnf:
        if len(clause) == 1:
            return clause[0]
    return 0

# Unit propogation 
    # Input(s): literal, SAT in CNF form
    # Output(s): Modified SAT in CNF form (clauses with l removed (aaign true), -l removed from clauses (assign false))
def unit_propogate(l, sat_cnf):
    new_sat_cnf = []
    for clause in sat_cnf:
        if l in clause:
            continue
        elif -l in clause:
            new_clause = clause[:]
            while -l in new_clause:
                new_clause.remove(-l)
            if new_clause is not None:
                new_sat_cnf.append(new_clause)
            else:
                new_sat_cnf.append([])
        else:
            new_sat_cnf.append(clause)
    return new_sat_cnf

# Checks for pure literals in wff
    # Input(s): SAT in CNF form 
    # Output(s): First occurence of pure literal or 0 if no pure literals
def check_pure_literal(sat_cnf):
    literals = get_literals(sat_cnf)
    for l in literals:
        if -l in literals:
            continue
        return l 
    return 0


# Remove clauses with pure literal (assign true to pure literal)
    # Input(s): literal, SAT in CNF form
    # Output(s): Modified SAT in CNF form with clauses with pure literal l removed (assign truth to pure literal l)
def pure_literal_assign(l, sat_cnf):
    new_sat_cnf = []
    for clause in sat_cnf:
        if l in clause:
            continue
        else:
            new_sat_cnf.append(clause)
    return new_sat_cnf

# Select literal from SAT_CNF
    # Input(s): Set of literals
    # Output(s): literal from set
def select_literal(literals):
    return literals.pop() 

# Get set of literals from wff
    # Input(s): SAT in CNF form
    # Output(s): Set of literals            
def get_literals(sat_cnf):
    literals = []
    for clause in sat_cnf:
        for l in clause:
            literals.append(l)
    literals = set(literals)
    return literals

# Assign truth to selected literal l (remove clauses with literal l, remove -l from clauses)
    # Input(s): literal, SAT in CNF form
    # Output(s): Modified SAT in CNF form
def assign_true(l, sat_cnf):
    new_sat_cnf = []
    for clause in sat_cnf:
        if l in clause:
            continue
        elif -l in clause:
            new_clause = clause[:]
            while -l in new_clause:
                new_clause.remove(-l)
            if new_clause is not None:
                new_sat_cnf.append(new_clause)
            else:
                new_sat_cnf.append([])
        else:
            new_sat_cnf.append(clause)
    return new_sat_cnf
