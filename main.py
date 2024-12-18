tarefas = []

def adicionarTarefas(nome, descricao, prioridade, categoria):
    tarefa = {
        "nome": nome,
        "descrição": descricao,
        "prioridade": prioridade,
        "categoria": categoria,
        "concluída": False
    }
    tarefas.append(tarefa)
    print(f"Tarefa '{nome}' adicionada com sucesso!")

def listaDeTarefas():
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
    for i, tarefa in enumerate(tarefas):
        status = "Concluída" if tarefa['concluída'] else "Pendente"
        print(f"{i + 1}. {tarefa['nome']} (Prioridade: {tarefa['prioridade']}, Categoria: {tarefa['categoria']}, Status: {status})")

def completarTarefas(numero_da_tarefa):
    if 0 < numero_da_tarefa <= len(tarefas):
        tarefas[numero_da_tarefa - 1]['concluída'] = True
        print(f"Tarefa '{tarefas[numero_da_tarefa - 1]['nome']}' marcada como concluída!")
    else:
        print("Número de tarefa inválido.")

def tarefasPorPrioridade(prioridade):
    filtrar_tarefas = [tarefa for tarefa in tarefas if tarefa['prioridade'] == prioridade]
    if not filtrar_tarefas:
        print(f"Nenhuma tarefa encontrada com prioridade '{prioridade}'.")
    for i, tarefa in enumerate(filtrar_tarefas):
        status = "Concluída" if tarefa['concluída'] else "Pendente"
        print(f"{i + 1}. {tarefa['nome']} (Categoria: {tarefa['categoria']}, Status: {status})")

def tarefasPorCategoria(categoria):
    filtrar_tarefas = [tarefa for tarefa in tarefas if tarefa['categoria'] == categoria]
    if not filtrar_tarefas:
        print(f"Nenhuma tarefa encontrada na categoria '{categoria}'.")
    for i, tarefa in enumerate(filtrar_tarefas):
        status = "Concluída" if tarefa['concluída'] else "Pendente"
        print(f"{i + 1}. {tarefa['nome']} (Prioridade: {tarefa['prioridade']}, Status: {status})")

def menu():
    while True:
        print("\nMenu de Comandos:")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Marcar Tarefa como Concluída")
        print("4. Exibir Tarefas por Prioridade")
        print("5. Exibir Tarefas por Categoria")
        print("6. Sair")

        menu = input("Escolha uma opção: ")
        
        if menu == "1":
            nome = input("Nome da tarefa: ")
            descricao = input("Descrição da tarefa: ")
            prioridade = input("Prioridade da tarefa: ")
            categoria = input("Categoria da tarefa: ")
            adicionarTarefas(nome, descricao, prioridade, categoria)
        elif menu == "2":
            listaDeTarefas()
        elif menu == "3":
            numero_da_tarefa = int(input("Número da tarefa para concluir: "))
            completarTarefas(numero_da_tarefa)
        elif menu == "4":
            prioridade = input("Prioridade: ")
            tarefasPorPrioridade(prioridade)
        elif menu == "5":
            categoria = input("Categoria: ")
            tarefasPorCategoria(categoria)
        elif menu == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()