
#====================================================================



def show_menu():
    
    menu = """
        Seja bem vinda(o) ao New Age Banking! O seu banco do futuro!
        Por gentileza, informe a operação:
        [1] - DEPÓSITO
        [2] - SAQUE
        [3] - EXTRATO
        [4] - NOVO USUÁRIO
        [5] - NOVA CONTA
        [6] - LISTAR CONTAS
        [7] - SAIR
    """
    return menu

def deposit(balance,extract,deposit_value_daily,/): # Passagem dos parâmetros por posição
    
    while deposit_value_daily <= 0.0:
        print("Você precisa inserir um valor maior que zero!")
        deposit_value_daily = float(input("Informe o valor a ser depositado:"))
        balance += deposit_value_daily

    balance += deposit_value_daily
    extract += f"Você Depositou: R${deposit_value_daily:.2f}\n"
    print(f"O valor R${deposit_value_daily} foi depositado com sucesso!")

    return balance, extract

def withdrawl(*,balance,extract,limit,number_of_withdrawl,limit_of_withdrawl_daily):  # Passagem dos parâmetros por nome
    
    if number_of_withdrawl < limit_of_withdrawl_daily: 
        withdrawl_value_daily = float(input("Informe o valor a ser sacado:"))
        
        if balance == 0.0 or balance < withdrawl_value_daily:
            print("Você não tem saldo suficiente para realizar o saque!")
            show_menu()
            
        elif withdrawl_value_daily > limit:
            print("Você ultrapassou o limite de saque!")
            show_menu()
            
        elif balance > 0:
            balance -= withdrawl_value_daily
            number_of_withdrawl += 1
            extract += f"Você Sacou: R${withdrawl_value_daily:.2f}\n"
            print(f"O saque de R${withdrawl_value_daily:.2f} foi realizado com sucesso!")               
    else:
        print("Você excedeu o número de saques por dia!")   
    
    return balance,extract,number_of_withdrawl

def show_extract_account(balance,/,*,extract):
    
    if extract == "":
        print("Não foram realizadas movimentações!")
        
    else:
        text_extract = " EXTRATO DA CONTA "
        text_transactions = " MOVIMENTAÇÕES DA CONTA "
        print(text_extract.center(40, "#"))
        print(f"Saldo em conta: R${balance:.2f}\n")
        print(text_transactions.center(40, "#"))
        print(extract)   

def create_user(users):
    
    cpf = input("Informe o seu cpf(Apenas números): ")
    user = user_filter(cpf,users)
    
    if user:
        print("Já existe um usuário cadastrado com O CPF informado!")
        return
    
 
    name = input("Informe o seu nome completo: ")
    date_of_birth = input("Informe a sua data de nascimento(dd-mm-aaaa): ")
    address = input("Informe o seu endereço (Logradouro, nro - Bairro - Cidade/Estado): ")
    
    users.append({"name": name, "date_of_birth":date_of_birth, "address":address,"cpf":cpf})
    
    print("Usuário cadastrado com sucesso!")
 
def user_filter(cpf,users):
    
    users_filtered = [user for user in users if user["cpf"] == cpf]
    
    return users_filtered[0] if users_filtered else None
    
def create_account(agency, account_number,users):
    cpf = input("Informe o seu cpf(Apenas números): ")
    user = user_filter(cpf,users)
    
    if user:
        print("A conta foi criada com sucesso! ")
        return {"agency": agency, "account_number": account_number, "user": user}
    
    print("\n O usuário não foi encontrado!")
    
def show_list_accounts(accounts):
    for account in accounts:
        line = f"""
            \nAgência: {account['agency']}
            \nConta Corrente: {account['account_number']}
            \nTitular: {account['user']['name']} 
        """
        print("=" * 30)
        print (line)

def main():
    
    balance = 0
    number_of_withdrawl = 0
    WITHDRAWL_DAILY = 3
    limit = 500
    extract = ""
    users = []
    accounts = []
    AGENCY = "0001"
    
    while True:
        option = int(input(show_menu()))
        
        if option == 1:            
            deposit_value_daily = float(input("Informe o valor a ser depositado:"))
            
            balance,extract = deposit(balance,extract,deposit_value_daily)

        elif option == 2:
            balance,extract,number_of_withdrawl = withdrawl(balance=balance,extract=extract,limit=limit,number_of_withdrawl=number_of_withdrawl,limit_of_withdrawl_daily=WITHDRAWL_DAILY)
            
        elif option == 3:
            show_extract_account(balance,extract=extract)
            
        elif option == 4:
            create_user(users)
            
        elif option == 5:  
            account_number = len(accounts) + 1
            account = create_account(AGENCY,account_number,users)
            
            if account:
                accounts.append(account)
                
        elif option == 6:
            show_list_accounts(accounts)
                                
        elif option == 7:
            break    

main()
