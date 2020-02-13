import mcprbatl.model_loader as model_loader
import mcprbatl.formula_loader as formula_loader

model_file = "data/journal-ex2.model"
formulas_file = "data/journal-ex2-test1.formulas"
#formulas_file = "data/journal-ex2-test2.formulas"
#formulas_file = "data/journal-ex2-test3.formulas"
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

#print("Table 1 in IJCAI'19 paper")
f = fs[0]
print(f.path_formula.pr_max(m, f.agents, f.bound)['q0'])

#print("Table 2 in IJCAI'19 paper")
#f = fs[14]
#print(f.path_formula.pr_max(m, f.agents, f.bound)['q0'])