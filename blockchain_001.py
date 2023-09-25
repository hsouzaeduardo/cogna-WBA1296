# Importando as bibliotecas necessárias
import hashlib
import time

# Definindo a classe Block para representar cada bloco no blockchain
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index  # Índice do bloco na cadeia
        self.timestamp = timestamp # Timestamp de quando o bloco foi criado
        self.data = data # Dados armazenados no bloco
        self.previous_hash = previous_hash  # Hash do bloco anterior na cadeia

# Função para calcular o hash de um bloco
def calculate_hash(block):
    block_string = f"{block.index}{block.timestamp}{block.data}{block.previous_hash}"
    return hashlib.sha256(block_string.encode()).hexdigest()

# Função para adicionar um novo bloco ao blockchain
def add_block(data, blockchain):
    last_block = blockchain[-1] # Obtém o último bloco na cadeia
    new_index = last_block.index + 1 # Calcula o índice para o novo bloco
    new_timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()) # Obtém o timestamp atual
    new_block = Block(new_index, new_timestamp, data, calculate_hash(last_block)) # Cria um novo bloco
    blockchain.append(new_block) # Adiciona o novo bloco à cadeia

# Função para validar a integridade do blockchain
def is_chain_valid(blockchain):
    for i in range(1, len(blockchain)):
        if blockchain[i].previous_hash != calculate_hash(blockchain[i-1]):
            return False # Retorna falso se a cadeia for inválida
    return True # Retorna verdadeiro se a cadeia for válida

# Crie o Bloco Gênesis
genesis_block = Block(0, "2023-01-01 00:00:00", "Genesis Block", "0")
blockchain = [genesis_block] # Inicializa o blockchain com o bloco gênesis

# Adicione alguns blocos
add_block("Block 1 Data", blockchain)
add_block("Block 2 Data", blockchain)
add_block("Block 3 Data", blockchain)

#Valide o blockchain
if is_chain_valid(blockchain):
    print("Blockchain é válido")
else:
    print("Blockchain não é válido")

# Imprima o blockchain
for block in blockchain:
    print(f"Índice: {block.index}, Timestamp: {block.timestamp}, Data: {block.data}, Hash anterior: {block.previous_hash}")
