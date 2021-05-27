from mcprbatl import formula_loader

formula_file = "experiment/data/example1.formulas"
loader = formula_loader.FormulaLoader(formula_file)
fs = loader.load()
for f in fs:
    print(f.to_string())
