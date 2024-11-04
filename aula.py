import redis

# Conectando ao Redis
try:
    r = redis.Redis(host='localhost', port=6379, db=0)
    # Testando conexão
    r.ping()
    print("Conectado ao Redis com sucesso!")
except redis.ConnectionError:
    print("Erro: não foi possível conectar ao Redis.")
    exit()

# Nome da lista de tarefas no Redis
nome_da_lista_de_tarefas = 'lista_de_tarefas'

def adicionar_tarefa():
    tarefa = input("Digite a tarefa a ser adicionada: ").strip()
    if tarefa:
        r.rpush(nome_da_lista_de_tarefas, tarefa)
        print("Tarefa adicionada!")
    else:
        print("Tarefa vazia. Tente novamente.")

def listar_tarefas():
    tarefas = r.lrange(nome_da_lista_de_tarefas, 0, -1)
    if tarefas:
        print("\nTarefas na lista:")
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"{i}. {tarefa.decode('utf-8')}")
    else:
        print("A lista de tarefas está vazia.")

def remover_primeira_tarefa():
    primeira_tarefa = r.lpop(nome_da_lista_de_tarefas)
    if primeira_tarefa:
        print("Primeira tarefa removida:", primeira_tarefa.decode('utf-8'))
    else:
        print("A lista está vazia.")

def remover_ultima_tarefa():
    ultima_tarefa = r.rpop(nome_da_lista_de_tarefas)
    if ultima_tarefa:
        print("Última tarefa removida:", ultima_tarefa.decode('utf-8'))
    else:
        print("A lista está vazia.")

def menu():
    while True:
        print("\nMenu:")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Remover primeira tarefa")
        print("4. Remover última tarefa")
        print("5. Sair")
        escolha = input("Escolha uma opção: ").strip()

        if escolha == '1':
            adicionar_tarefa()
        elif escolha == '2':
            listar_tarefas()
        elif escolha == '3':
            remover_primeira_tarefa()
        elif escolha == '4':
            remover_ultima_tarefa()
        elif escolha == '5':
            confirmacao = input("Tem certeza de que deseja sair? (s/n): ").strip().lower()
            if confirmacao == 's':
                print("Saindo...")
                break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
