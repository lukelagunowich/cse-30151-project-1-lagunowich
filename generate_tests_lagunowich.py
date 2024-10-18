import random
import time

# SOURCE: DumbSat.py
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

# SOURCE: DumbSat.py
def build_wff(Nvars,Nclauses,LitsPerClause):
    wff=[]
    for i in range(1,Nclauses+1):
        clause=[]
        for j in range(1,LitsPerClause+1):
            var=random.randint(1,Nvars)
            if random.randint(0,1)==0: var=-var
            clause.append(var)
        wff.append(clause)
    return wff

# SOURCE: DumbSat.py
def test_wff(wff,Nvars,Nclauses):
    Assignment=list((0 for x in range(Nvars+2)))
    start = time.time() # Start timer
    SatFlag=check(wff,Nvars,Nclauses,Assignment)
    end = time.time() # End timer
    exec_time=int((end-start)*1e6)
    return [wff,Assignment,SatFlag,exec_time]

def generate_check_file(testCases, ProbNum):
    check_file = open('check_file_lagunowich.cnf.csv', 'w') # open check file for test cases, must store satisfiability for checking
    for i in range(0,len(testCases)):
        TestCase=testCases[i]
        Nvars=TestCase[0]
        NClauses=TestCase[1]
        LitsPerClause=TestCase[2]
        Ntrials=TestCase[3]
        for j in range(0,Ntrials):
            random.seed(ProbNum)
            wff = build_wff(Nvars,NClauses,LitsPerClause)
            results=test_wff(wff,Nvars,NClauses)
            wff=results[0]
            if results[2]: # get satisfiability
                y='S'
            else:
                y='U'
            #Add wff to cnf file
            x="c"+","+str(ProbNum)+","+str(LitsPerClause)+","+y+"\n"
            check_file.write(x)
            x="p"+","+"cnf"+","+str(Nvars)+","+str(NClauses)+"\n"
            check_file.write(x)
            for i in range(0,len(wff)):
                clause=wff[i]
                x=""
                for j in range(0,len(clause)):
                    x=x+str(clause[j])+","
                x=x+"0\n"
                check_file.write(x)
            #Increment problem number for next iteration
            ProbNum=ProbNum+1
            check_file.close

def generate_data_file(testCases, ProbNum): 
    data_file = open('data_file_lagunowich.cnf.csv', 'w') # open check file for test cases, do not store satisfiability (many cases for timing, would take too long to generate)
    for i in range(0,len(testCases)):
        TestCase=testCases[i]
        Nvars=TestCase[0]
        NClauses=TestCase[1]
        LitsPerClause=TestCase[2]
        Ntrials=TestCase[3]
        for j in range(0,Ntrials):
            random.seed(ProbNum)
            wff = build_wff(Nvars,NClauses,LitsPerClause)
            y = '?'
            #Add wff to cnf file
            x="c"+","+str(ProbNum)+","+str(LitsPerClause)+","+y+"\n"
            data_file.write(x)
            x="p"+","+"cnf"+","+str(Nvars)+","+str(NClauses)+"\n"
            data_file.write(x)
            for i in range(0,len(wff)):
                clause=wff[i]
                x=""
                for j in range(0,len(clause)):
                    x=x+str(clause[j])+","
                x=x+"0\n"
                data_file.write(x)
            #Increment problem number for next iteration
            ProbNum=ProbNum+1
            data_file.close

# SOURCE: DumbSat.py
# Test cases (check)
testCasesCheck = [
    [4,10,2,10],
    [8,16,2,10],
    [12,24,2,10]
]

# SOURCE: DumbSat.py
# Timing cases (data)
testCasesData = [
    [4,9,2,10],
    [8,18,2,10],
    [12,20,2,10],
    [16,30,2,10],
    [18,32,2,10],
    [20,33,2,10],
    [22,38,2,10],
    [24,43,2,10],
    [26,45,2,10],
    [28,47,2,10]
]

# Generate check/data files
generate_check_file(testCasesCheck, ProbNum=3)
generate_data_file(testCasesData, ProbNum=3)