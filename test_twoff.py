import mcprbatl.model_loader as model_loader
import mcprbatl.formula_loader as formula_loader

model_file = "experiment/data/twoff.model"
formulas_file = "experiment/data/twoff.formulas"
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

print("Table 1 in IJCAI'19 paper")
f = fs[5]
print(f.path_formula.pr_max(m, f.agents, f.bound)['q0'])

print("Table 2 in IJCAI'19 paper")
f = fs[20]
print(f.path_formula.pr_max(m, f.agents, f.bound)['q0'])