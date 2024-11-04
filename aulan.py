import redis 

# Conectando ao Redis 
r = redis.Redis(host='localhost', port=6379, db=0) 

# Nome da lista de tarefas no Redis 
nome_da_lista_de_tarefas = 'lista_de_tarefas' 

def adicionar_tarefa(): 
    tarefa = input("Digite a tarefa a ser adicionada: ") 
    r.rpush(nome_da_lista_de_tarefas, tarefa) 
    print("Tarefa adicionada!") 

def listar_tarefas(): 
    tarefas = r.lrange(nome_da_lista_de_tarefas, 0, -1) 
    print('Tarefas na lista:') 
    for tarefa in tarefas: 
        print(tarefa.decode('utf-8')) 

def remover_primeira_tarefa(): 
    primeira_tarefa = r.lpop(nome_da_lista_de_tarefas) 
    if primeira_tarefa: 
        print('Primeira tarefa removida:', primeira_tarefa.decode('utf-8')) 
    else: 
        print("A lista está vazia.") 

def remover_ultima_tarefa(): 
    ultima_tarefa = r.rpop(nome_da_lista_de_tarefas) 
    if ultima_tarefa: 
        print('Última tarefa removida:', ultima_tarefa.decode('utf-8')) 
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
        escolha = input("Escolha uma opção: ") 

        if escolha == '1': 
            adicionar_tarefa() 
        elif escolha == '2': 
            listar_tarefas() 
        elif escolha == '3': 
            remover_primeira_tarefa() 
        elif escolha == '4': 
            remover_ultima_tarefa() 
        elif escolha == '5': 
            print("Saindo...") 
            break 
        else: 
            print("Opção inválida. Tente novamente.") 

if __name__ == "__main__": 
    menu()
