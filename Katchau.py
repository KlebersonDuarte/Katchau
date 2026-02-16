# Dicionários com os produtos e preços
perifericos = {
    1: ("Teclado", 150),
    2: ("Mouse", 75),
    3: ("Scanner", 300),
    4: ("Microfone", 250),
    5: ("Webcam", 500),
    6: ("Joystick", 175),
    7: ("Leitor de código de barras", 750),
    8: ("Leitor biométrico", 1000),
    9: ("Mesa digitalizadora", 2500),
    10: ("Controle de videogame", 378),
    11: ("Monitor", 3200),
    12: ("Impressora", 300),
    13: ("Caixas de som", 450),
    14: ("Projetor multimídia", 600),
    15: ("Fones de ouvido", 100),
    16: ("Touchscreen", 5000),
    17: ("Modem", 55),
    18: ("HD externo", 800),
    19: ("Pen drive", 35),
    20: ("Multifuncional", 4500)
}

hardware = {
    1: ("Placa-mãe", 550),
    2: ("Processador", 700),
    3: ("Memória RAM", 300),
    4: ("Placa de vídeo", 3500),
    5: ("Placa de som", 50),
    6: ("Placa de rede", 55),
    7: ("HD", 400),
    8: ("SSD", 599),
    9: ("Fonte de alimentação", 550),
    10: ("Cooler", 200),
    11: ("Drive DVD/Blu-ray", 30),
    12: ("Teclado", 599.90),
    13: ("Mouse", 350),
    14: ("Monitor", 2200),
    15: ("Caixas de som", 367),
    16: ("Webcam", 150),
    17: ("Microfone", 200),
    18: ("Impressora", 489),
    19: ("Pen drive", 67),
    20: ("Scanner", 7800)
}

# Lista de itens no carrinho
carrinho = []

# Loop principal
while True:
    print('\nBEM VINDO AO KATCHAU!')
    print('Selecione uma opção:')
    print('0 - Sair')
    print('1 - Periféricos')
    print('2 - Hardware')
    print('3 - Manutenção')
    print('4 - Ver carrinho / Remover item')
    print('5 - Finalizar compra')

    try:
        opcao = int(input('Digite o número da opção desejada: '))

        if opcao == 1:
            print('\n--- PERIFÉRICOS ---')
            for numero, (nome, preco) in perifericos.items():
                print(f"{numero} - {nome} - R${preco:.2f}")
            escolha = int(input("\nDigite o número do produto para adicionar ao carrinho: "))
            produto = perifericos.get(escolha)
            if produto:
                carrinho.append(produto)
                print(f'"{produto[0]}" adicionado ao carrinho por R${produto[1]:.2f}!')
            else:
                print("Produto não encontrado.")

        elif opcao == 2:
            print('\n--- HARDWARE ---')
            for numero, (nome, preco) in hardware.items():
                print(f"{numero} - {nome} - R${preco:.2f}")
            escolha = int(input("\nDigite o número do produto para adicionar ao carrinho: "))
            produto = hardware.get(escolha)
            if produto:
                carrinho.append(produto)
                print(f'"{produto[0]}" adicionado ao carrinho por R${produto[1]:.2f}!')
            else:
                print("Produto não encontrado.")

        elif opcao == 3:
            print('\n--- MANUTENÇÃO ---')
            print('Entre em contato conosco:')
            print('Email: katchau@gmail.com')
            print('Telefone: +55 11 99999-9999')

        elif opcao == 0:
            print('Tchau! Obrigado por visitar o KATCHAU.')
            break

        elif opcao == 4:
            print('\n--- CARRINHO DE COMPRAS ---')
            if not carrinho:
                print('Seu carrinho está vazio.')
            else:
                total = 0
                for i, (nome, preco) in enumerate(carrinho, 1):
                    print(f"{i}. {nome} - R${preco:.2f}")
                    total += preco
                print(f"\nTotal: R${total:.2f}")

                remover = input("\nDeseja remover algum item? (s/n): ").strip().lower()
                if remover == 's':
                    try:
                        num_remover = int(input("Digite o número do item que deseja remover: "))
                        if 1 <= num_remover <= len(carrinho):
                            item_removido = carrinho.pop(num_remover - 1)
                            print(f'Item "{item_removido[0]}" removido do carrinho.')
                        else:
                            print("Número inválido.")
                    except ValueError:
                        print("Entrada inválida. Digite um número.")

        elif opcao == 5:
            print('\n--- FINALIZANDO COMPRA ---')
            if not carrinho:
                print('Seu carrinho está vazio. Adicione itens antes de finalizar.')
            else:
                total = 0
                print('Você comprou os seguintes itens:')
                for i, (nome, preco) in enumerate(carrinho, 1):
                    print(f"{i}. {nome} - R${preco:.2f}")
                    total += preco
                print(f"\nTotal da compra: R${total:.2f}")
                print('Compra finalizada! Obrigado pela preferência.')
                carrinho.clear()
                break

        else:
            print('Opção não encontrada.')

    except ValueError:
        print("Entrada inválida. Digite um número.")
