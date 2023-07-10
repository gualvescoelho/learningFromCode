import pickle

# Carregar o modelo e o vocabulário salvos
with open("model.pkl", "rb") as f:
    loaded_model = pickle.load(f)
    
with open("vocab.pkl", "rb") as f:
    loaded_vocab = pickle.load(f)

# Função para gerar sugestões de código
def generate_code_suggestions(input_sequence):
    input_tokens = input_sequence.split()
    suggestions = []
 
    for token in loaded_vocab:
        if token.startswith(input_tokens[0]):
            suggestions = loaded_model.get(input_tokens[0], [])
    
    return suggestions

# Loop de interação com o usuário
while True:
    input_sequence = input("Digite o início do código: ")
    if input_sequence.lower() == "sair":
        break

    suggestions = generate_code_suggestions(input_sequence)

    print("Sugestões de código:")
    for suggestion in suggestions:
        print(suggestion)
