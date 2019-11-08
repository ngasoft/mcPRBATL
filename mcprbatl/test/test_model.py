import mcprbatl.model as model

model_file = "data/example1.model"
m = model.ModelLoader(model_file)
m.load()
print(m)