import mcprbatl.model_loader as model_loader
import mcprbatl.formula_loader as formula_loader
import mcprbatl.formula

model_file = "experiment/data/journal-ex2.model"
formulas_file = "experiment/data/journal-ex2-test1.formulas"
#formulas_file = "experiment/data/journal-ex2-test2.formulas"
#formulas_file = "experiment/data/journal-ex2-test3.formulas"
loader = model_loader.ModelLoader(model_file)
m = loader.load()
# print(m)

loader = formula_loader.FormulaLoader(formulas_file)
fs = loader.load()
for f in fs:
    print(f.to_string())
    s = f.sat(m)
    print(" is satisfied in ")
    print(s)

def matrix_2D_X(X,n):
    ret = ''
    ks = sorted(X)
    i = 0
    #n= 7
    for k in ks:
        i += 1
        ret += str(k) + ':' + str(X[k]) + (', ' if i % n != 0 else '\n')
    return ret


#print("Table 1 in IJCAI'19 paper")
f = fs[0]
X = f.path_formula.pr_max(m, f.agents, f.bound)['q0']
print(matrix_2D_X(X,7))
print("State counter: ", mcprbatl.formula.Formula.state_counter)
print("Transition counter: ", mcprbatl.formula.Formula.transition_counter)

#print("Table 2 in IJCAI'19 paper")
#f = fs[14]
#print(f.path_formula.pr_max(m, f.agents, f.bound)['q0'])