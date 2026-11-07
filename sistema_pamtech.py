import sqlite3

conexao = sqlite3.connect("pamtech.db")
cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        telefone TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        senha TEXT NOT NULL
    )
""")

try:
    cursor.execute("INSERT INTO usuarios (username, senha) VALUES ('admin', '1234')")
    conexao.commit()
except sqlite3.IntegrityError:
    pass

def cadastrar_cliente():
    print("\n--- CADASTRO DE CLIENTE (PAM TECH) ---")
    nome = input("Digite o nome completo: ")
    telefone = input("Digite o telefone/WhatsApp: ")
    email = input("Digite o e-mail: ")

    try:
        cursor.execute("INSERT INTO clientes (nome, telefone, email) VALUES (?, ?, ?)", (nome, telefone, email))
        conexao.commit()
        print(f"Sucesso! Cliente {nome} cadastrado com sucesso no banco de dados.")
    except sqlite3.IntegrityError:
        print("Erro: Este e-mail já está cadastrado no sistema.")

def realizar_login():
    print("\n--- LOGIN NO SISTEMA PAM TECH ---")
    usuario_digitado = input("Usuário ou E-mail: ")
    senha_digitada = input("Senha: ")

    cursor.execute("SELECT * FROM usuarios WHERE username = ? AND senha = ?", (usuario_digitado, senha_digitada))
    resultado = cursor.fetchone()

    if resultado:
        print(f"\n[LOGIN APROVADO] Bem-vindo ao sistema da PAM TECH, {usuario_digitado}!")
        return True
    else:
        print("\n[ACESSO NEGADO] Usuário ou senha incorretos.")
        return False

def main():
    while True:
        print("\n==============================")
        print("   SISTEMA INTEGRADO PAM TECH ")
        print("==============================")
        print("1. Fazer Login")
        print("2. Cadastrar Novo Cliente")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            realizar_login()
        elif opcao == "2":
            cadastrar_cliente()
        elif opcao == "3":
            print("A encerrarem o sistema da PAM TECH. Até logo!")
            conexao.close()
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()