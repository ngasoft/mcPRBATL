import mcprbatl.formula_loader as formula_loader

formula_file = "data/example1.formulas"
loader = formula_loader.FormulaLoader(formula_file)
fs = loader.load()
print(fs)