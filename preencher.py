import pickle

# Vocabulário padrão
vocab = ['print', 'for', 'if', 'else', 'def', 'import', 'return']

# Dados de exemplo
data = {
    'print': ['()', "(' \n')", '("")'],
    'for': ['range()', '(a in as):', '    print(i)'],
    'if': ['(a == b)', '(a != b)','() && ()','() || ()'],
    'else': [':', '    action'],
    'def': ['function_name:', '    action', '    return'],
    'import': ['module'],
    'return': ['value']
}

# Salvando o modelo e o vocabulário em arquivos
with open("model.pkl", "wb") as f:
    pickle.dump(data, f)
with open("vocab.pkl", "wb") as f:
    pickle.dump(vocab, f)