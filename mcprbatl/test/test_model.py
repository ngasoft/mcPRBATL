import mcprbatl.model_loader as model_loader

model_file = "data/example1.model"
loader = model_loader.ModelLoader(model_file)
m = loader.load()
print(m)
