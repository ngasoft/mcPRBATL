import mcprbatl.model_loader as model_loader
import mcprbatl.formula_loader as formula_loader

model_file = "data/twoff.model"
formulas_file = "data/twoff.formulas"
loader = model_loader.ModelLoader(model_file)
m = loader.load()
print(m)

loader = formula_loader.FormulaLoader(formulas_file)
fs = loader.load()
for f in fs:
    s = f.sat(m)
    print(s)

