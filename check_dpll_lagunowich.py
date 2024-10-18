from data_ingestor_lagunowich import read_sat_cnf_csv
from code_dpll_lagunowich import dpll


# Need output for checks?
for sat_cnf in read_sat_cnf_csv('check_file_lagunowich.cnf.csv'):
    sat, _, _, curr_sat_cnf = sat_cnf[0], sat_cnf[1], sat_cnf[2], sat_cnf[3]
    if dpll(curr_sat_cnf) == True:
        result = 'S'
    else:
        result = 'U'
    assert result == sat, "Check failed."

print('All checks passed.')
    