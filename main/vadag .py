from import_VADAG import*

def login():
    try:
        print('┌───── •≈≈≈≈• ─────┐')
        print("     【 LOGIN 】")
        print('└───── •≈≈≈≈• ─────┘')
        logiin=int(int(input('''1.Login
2.Cadastrar novo funcionário
3.Lista de funcionários
4.Excluir funcionário
5.Pesquisar funcionário
6.Área de Cargo
0.Encerrar programa
—» ''')))
    except:
        print("╭─━━━━━━━━━━━━atenção━━━━━━━━━━━━━─╮")
        print("          Opção inexistente!")
        print("⸻⸻⸻⸻⸻⸻" * 15)
        login()
    else:
        if logiin == 1:
            login_funcionario()
        elif logiin == 2:
            cadastrar_funcionario()
        elif logiin == 3:
            listar_funcionarios()
        elif logiin == 4:
            excluir_funcionario()
        elif logiin == 5:
            pesquisar_funcionario()
        elif logiin == 6:
            menu_cargo()
        elif logiin == 0:
            print("Encerrado...")
            banco.close()
        else:
            print("╭─━━━━━━━━━━━━atenção━━━━━━━━━━━━━─╮")
            print("          Opção inexistente!")
            print("⸻⸻⸻⸻⸻⸻" * 15)
            login()

def login_funcionario():
    try:
        certo = 0
        cursor = banco.cursor()
        comando_sql = "select * from funcionarios"
        cursor.execute(comando_sql)
        print("⸻⸻⸻⸻⸻⸻" * 15)
        email = input("Insira seu email: ")
        senha = input("Insira sua senha: ")
    except:
        print("╭─━━━━━━━━━━━━atenção━━━━━━━━━━━━━─╮")
        print("          Opção inexistente!")
        print("⸻⸻⸻⸻⸻⸻" * 15)
        login()
    else:
        valores_lidos = cursor.fetchall()
        for i in valores_lidos:
            if i[2] == email and i[3] == senha:
                print("⸻⸻⸻⸻⸻⸻" * 15)
                certo = 1
                escopo_global()
            if certo == 0:
                print("╭─━━━━━━━━━━━━atenção━━━━━━━━━━━━━─╮")
                print("          Dados incorreto!")
                print("⸻⸻⸻⸻⸻⸻" * 15)
                login()

def cadastrar_funcionario():
    try:
        cursor = banco.cursor()
        comando_sql = "INSERT INTO funcionarios (nome_funcionario,email,senha,fk_cod_cargo) values (%s,%s,%s,%s)"
        nome=input("Insira o nome : ")
        email=input("Insira o email: ")
        senha=input("Insira a senha: ")
        cargo=int(input("Insira o código do cargo: "))
        print("⸻⸻⸻⸻⸻⸻" * 15)
    except:
        print("╭─━━━━━━━━━━━━atenção━━━━━━━━━━━━━─╮")
        print("          Opção inexistente!")
        print("⸻⸻⸻⸻⸻⸻" * 15)
        login()
    else:
        dados = (nome,email,senha,cargo)
        cursor.execute(comando_sql,dados)
        banco.commit()
        login()

def listar_funcionarios():
    cursor = banco.cursor()
    comando_sql = "select cod_funcionario,nome_funcionario,email,senha,fk_cod_cargo,cod_cargo,nome_cargo from funcionarios as f inner join cargos as c on f.fk_cod_cargo = c.cod_cargo"
    cursor.execute(comando_sql)
    valores = cursor.fetchall()
    for i in valores:
        print("Código: ", i[0])
        print("Nome: ", i[1])
        print("Email: ", i[2])
        print("Cargo: ", i[6])
        print("⸻⸻⸻⸻⸻⸻" * 15)
    login()

def excluir_funcionario():
    try:
        certo = 0
        cursor = banco.cursor()
        comando_sqla = "select cod_funcionario from funcionarios"
        cod = int(input("Insira o código do funcionário: "))
        cursor.execute(comando_sqla)
    except:
        print("╭─━━━━━━━━━━━━atenção━━━━━━━━━━━━━─╮")
        print("          Opção inexistente!")
        print("⸻⸻⸻⸻⸻⸻" * 15)
        login()
    else:
        valores = cursor.fetchall()
        for i in valores:
            if i[0] == cod:
                print("⸻⸻⸻⸻⸻⸻" * 15)
                print("Realizado com sucesso")
                comando_sql = "DELETE from funcionarios where cod_funcionario = {}".format(cod)
                cursor.execute(comando_sql)
                banco.commit()
                print("⸻⸻⸻⸻⸻⸻" * 15)
                login()
                certo = 1
        if certo == 0:
            print("╭─━━━━━━━━━━━━atenção━━━━━━━━━━━━━─╮")
            print("          Dados incorreto!")
            print("⸻⸻⸻⸻⸻⸻" * 15)
            login()

def pesquisar_funcionario():
    achei = 0
    cursor = banco.cursor()
    comando_sql = "select cod_funcionario,nome_funcionario,email,senha,fk_cod_cargo,cod_cargo,nome_cargo from funcionarios as f inner join cargos as c on f.fk_cod_cargo = c.cod_cargo"
    cursor.execute(comando_sql)
    print("⸻⸻⸻⸻⸻⸻" * 15)
    nome=input("Insira o nome do funcionário: ")
    valores_lidos = cursor.fetchall()
    for i in valores_lidos:
        if i[1] == nome:
            print("Código: ", i[0])
            print("Nome: ", i[1])
            print("Email: ", i[2])
            print("Cargo: ", i[6])
            print("⸻⸻⸻⸻⸻⸻" * 15)
            achei = 1
    if achei == 0:
        print("Funcionário não encontrado!")
        print("⸻⸻⸻⸻⸻⸻" * 15)
    banco.commit()
    login()

'------------------------------------------------'

def menu_cargo():
    try:
        print('╔═══════════════════════╗')
        print("   〘 Menu de Cargo 〙")
        print('╚═══════════════════════╝')
        MG = int(int(input('''1.Listar 
2.Cadastrar
3.Editar
4.Excluir
5.Pesquisar
0.Voltar para area de login
—»''')))
    except:
        print("╭─━━━━━━━━━━━━atenção━━━━━━━━━━━━━─╮")
        print("          Opção inexistente!")
        print("⸻⸻⸻⸻⸻⸻" * 15)
        menu_cargo()
    else:
        if MG == 1:
            listar_cargos()
        elif MG == 2:
            cadastrar_cargo()
        elif MG == 3:
            editar_cargo()
        elif MG == 4:
            excluir_cargo()
        elif MG == 5:
            pesquisar_cargo()
        elif MG == 0:
            login()
        else:
            print("╭─━━━━━━━━━━━━atenção━━━━━━━━━━━━━─╮")
            print("          Opção inexistente!")
            print("⸻⸻⸻⸻⸻⸻" * 15)
            menu_cargo()

def listar_cargos():
    cursor = banco.cursor()
    comando_sql = "select * from cargos"
    cursor.execute(comando_sql)
    valores = cursor.fetchall()
    for i in valores:
        print("⸻⸻⸻⸻⸻⸻" * 15)
        print("Código: ", i[0])
        print("Cargo: ", i[1])
        print("⸻⸻⸻⸻⸻⸻" * 15)
    menu_cargo()

def cadastrar_cargo():
    try:
        cursor = banco.cursor()
        comando_sql = "INSERT INTO cargos (cod_cargo,nome_cargo)values (%s,%s)"
        cod_cargo=int(input("Insira o código: "))
        cargo=input("Insira nome: ")
        print("⸻⸻⸻⸻⸻⸻" * 15)
    except:
        print("╭─━━━━━━━━━━━━atenção━━━━━━━━━━━━━─╮")
        print("          Opção inexistente!")
        print("⸻⸻⸻⸻⸻⸻" * 15)
        menu_cargo()
    else:
        dados = (cod_cargo,cargo)
        cursor.execute(comando_sql,dados)
        banco.commit()
        menu_cargo()

def editar_cargo():
    try:
        certo = 0
        cursor = banco.cursor()
        comando_sqla = "select cod_cargo,nome_cargo from cargos"
        cod = int(input("Insira o código do cargo: "))
        nome = input("Insira o novo nome do cargo: ")
        cursor.execute(comando_sqla)
    except:
        print("╭─━━━━━━━━━━━━atenção━━━━━━━━━━━━━─╮")
        print("          Opção inexistente!")
        print("⸻⸻⸻⸻⸻⸻" * 15)
        menu_cargo()
    else:
        valores = cursor.fetchall()
        for i in valores:
            if i[1] != nome and i[0] == cod:
                print("⸻⸻⸻⸻⸻⸻" * 15)
                print("Realizado com sucesso")
                comando_sql = "UPDATE cargos set nome_cargo = %s where cod_cargo = %s"
                dados=(nome,cod)
                cursor.execute(comando_sql,dados)
                banco.commit()
                print("⸻⸻⸻⸻⸻⸻" * 15)
                menu_cargo()
                certo = 1
        if certo == 0:
            print("╭─━━━━━━━━━━━━atenção━━━━━━━━━━━━━─╮")
            print("          Dados incorreto!")
            print("⸻⸻⸻⸻⸻⸻" * 15)
            menu_cargo()

def excluir_cargo():
    try:
        certo = 0
        cursor = banco.cursor()
        comando_sqla = "select cod_cargo from cargos"
        cod = int(input("Insira o código do cargo: "))
        cursor.execute(comando_sqla)
    except:
        print("╭─━━━━━━━━━━━━atenção━━━━━━━━━━━━━─╮")
        print("          Opção inexistente!")
        print("⸻⸻⸻⸻⸻⸻" * 15)
        menu_cargo()
    else:
        valores = cursor.fetchall()
        for i in valores:
            if i[0] == cod:
                print("⸻⸻⸻⸻⸻⸻" * 15)
                print("Realizado com sucesso")
                comando_sql = "DELETE from cargos where cod_cargo = {}".format(cod)
                cursor.execute(comando_sql)
                banco.commit()
                print("⸻⸻⸻⸻⸻⸻" * 15)
                menu_cargo()
                certo = 1
        if certo == 0:
            print("╭─━━━━━━━━━━━━atenção━━━━━━━━━━━━━─╮")
            print("          Dados incorretos!")
            print("⸻⸻⸻⸻⸻⸻" * 15)
            menu_cargo()

def pesquisar_cargo():
    achei = 0
    cursor = banco.cursor()
    comando_sql = "select * from cargos"
    cursor.execute(comando_sql)
    print("⸻⸻⸻⸻⸻⸻" * 15)
    nome=input("Insira o nome do cargo: ")
    valores_lidos = cursor.fetchall()
    for i in valores_lidos:
        if i[1] == nome:
            print("Código: ", i[0])
            print("Nome: ", i[1])
            print("⸻⸻⸻⸻⸻⸻" * 15)
            achei = 1
    if achei == 0:
        print("Cargo não encontrado!")
        print("⸻⸻⸻⸻⸻⸻" * 15)
    banco.commit()
    menu_cargo()

'-------------------------------------------------'

def escopo_global():
    try:
        print('╔═══════════════════════╗')
        print("   〘 Menu de opções 〙")
        print('╚═══════════════════════╝')
        EG = int(int(input('''1.Área de controle de estoque
2.Área do fornecedor
3.Área do cliente
4.Área controle vendas
0.voltar para area de login
—»''')))
        print("⸻⸻⸻⸻⸻⸻" * 15)
    except:
        print("╭─━━━━━━━━━━━━atenção━━━━━━━━━━━━━─╮")
        print("          Opção inexistente!")
        print("⸻⸻⸻⸻⸻⸻" * 15)
        escopo_global()
    else:
        if EG == 1:
            sistema_estoque()
        elif EG == 2:
            sistema_fornecedor()
        elif EG == 3:
            sistema_cliente()
        elif EG == 4:
            sistema_de_vendas()
        elif EG == 0:
            login()
        else:
            print("╭─━━━━━━━━━━━━atenção━━━━━━━━━━━━━─╮")
            print("          Opção inexistente!")
            print("⸻⸻⸻⸻⸻⸻" * 15)
            escopo_global()

'-------------------------------------------------'

def sistema_estoque():
    try:
        print(" ▂▃▄▅▆▇█▓▒░ Sistema de estoque ░▒▓█▇▆▅▄▃▂ ")
        op=int(input('''1.Listar 
2.Cadastrar 
3.Editar
4.Excluir
5.Pesquisar 
6.Área de Categorias
0.Voltar para menu de opções
—» '''))
        print("⸻⸻⸻⸻⸻⸻" * 15)
    except:
        print("╭─━━━━━━━━━━━━atenção━━━━━━━━━━━━━─╮")
        print("          Opção inexistente!")
        print("⸻⸻⸻⸻⸻⸻" * 15)
        sistema_estoque()
    else:
        if op == 1:
            listar_produto()
        elif op == 2:
            cadastrar_produto()
        elif op == 3:
            editar_produto()
        elif op == 4:
            excluir_produto()
        elif op == 5:
            pesquisar_produto()
        elif op == 6:
            menu_categoria()
        elif op == 0:
            escopo_global()
        else:
            print("╭─━━━━━━━━━━━━atenção━━━━━━━━━━━━━─╮")
            print("          Opção inexistente!")
            print("⸻⸻⸻⸻⸻⸻" * 15)
            sistema_estoque()

def listar_produto():
    cursor = banco.cursor()
    comando_sql = "select * from produtos"
    cursor.execute(comando_sql)
    valores = cursor.fetchall()
    for i in valores:
        print("⸻⸻⸻⸻⸻⸻" * 15)
        print("Código produto: ", i[0])
        print("Código categoria: ", i[1])
        print("Código fornecedor: ", i[2])
        print("Nome: ", i[3])
        print("Marca: ", i[4])
        print("Descrição: ", i[5])
        print("Quantidade: ", i[6])
        print("Custo medio: ", i[7])
        print("Valor de Venda: ", i[8])
        print("⸻⸻⸻⸻⸻⸻" * 15)
    sistema_estoque()

def cadastrar_produto():
    try:
        cursor = banco.cursor()
        comando_sql = "INSERT INTO produtos (nome_produto,marca,descricao,quantidade,custo_medio,valor_de_venda,fk_cod_categoria,fk_cod_fornecedor)values (%s,%s,%s,%s,%s,%s,%s,%s)"
        nome=input("Insira o nome do produto: ")
        marca=input("Insira a marca: ")
        descricao=input("Insira a descrição do produto: ")
        quantidade=int(input("Insira quantidade: "))
        custo_medio=float(input("Insira custo medio: "))
        valor_de_venda=float(input("Insira o valor de venda: "))
        cod1=int(input("Insira o código da categoria: "))
        cod2=int(input("Insira o código do fornecedor: "))
        print("⸻⸻⸻⸻⸻⸻" * 15)
    except:
        print("╭─━━━━━━━━━━━━atenção━━━━━━━━━━━━━─╮")
        print("          Opção inexistente!")
        print("⸻⸻⸻⸻⸻⸻" * 15)
        sistema_estoque()
    else:
        dados = (nome,marca,descricao,quantidade,custo_medio,valor_de_venda,cod1,cod2)
        cursor.execute(comando_sql,dados)
        banco.commit()
        sistema_estoque()

def editar_produto():
    cursor = banco.cursor()
    comando_sql = "UPDATE produtos set nome_produto,marca = %s where cod_produto = %s"
    cod = int(input("Insira o código do produto: "))
    nome = input("Insira o novo nome do produto: ")
    marca = input("Insira marca: ")
    print("⸻⸻⸻⸻⸻⸻" * 15)
    dados = (nome,marca,cod)
    cursor.execute(comando_sql,dados)
    banco.commit()
    sistema_estoque()

def excluir_produto():
    try:
        certo = 0
        cursor = banco.cursor()
        comando_sqla = "select cod_produto from produtos"
        cod=int(input("insira o código do produto: "))
        cursor.execute(comando_sqla)
    except:
        print("╭─━━━━━━━━━━━━atenção━━━━━━━━━━━━━─╮")
        print("          Opção inexistente!")
        print("⸻⸻⸻⸻⸻⸻" * 15)
        sistema_estoque()
    else:
        valores = cursor.fetchall()
        for i in valores:
            if i[0] == cod:
                print("⸻⸻⸻⸻⸻⸻" * 15)
                print("Realizado com sucesso")
                comando_sql = "DELETE from produtos where cod_produto = {}".format(cod)
                cursor.execute(comando_sql)
                banco.commit()
                print("⸻⸻⸻⸻⸻⸻" * 15)
                sistema_estoque()
                certo = 1
        if certo == 0:
            print("╭─━━━━━━━━━━━━atenção━━━━━━━━━━━━━─╮")
            print("          Produto inexistente!")
            print("⸻⸻⸻⸻⸻⸻" * 15)
            sistema_estoque()

def pesquisar_produto():
    achei = 0
    cursor = banco.cursor()
    comando_sql = "select cod_produto,fk_cod_categoria,fk_cod_fornecedor,nome_produto,marca,descricao,quantidade,custo_medio,valor_de_venda,cod_fornecedor,nome_fornecedor,cep,cnpj,logradouro,numero,bairro,cidade,estado,telefone,cod_categoria,nome_categoria from produtos as p inner join fornecedor as f on p.fk_cod_fornecedor = f.cod_fornecedor inner join categorias as g on p.fk_cod_categoria = g.cod_categoria"
    cursor.execute(comando_sql)
    nome=input("Insira o nome do produto: ")
    valores_lidos = cursor.fetchall()
    for i in valores_lidos:
        if i[3] == nome:
            print("Código produto: ", i[0])
            print("Código Categoria: ", i[1])
            print("Código Fornecedor: ", i[2])
            print("Nome: ", i[3])
            print("Marca: ", i[4])
            print("Descrição: ", i[5])
            print("Quantidade: ", i[6])
            print("Custo medio: ", i[7])
            print("Valor da venda: ", i[8])
            print("Fornecedor: ", i[10])
            print("categoria: ", i[20])
            print("⸻⸻⸻⸻⸻⸻" * 15)
            achei = 1
    if achei == 0:
        print("Produto não encontrado!")
        print("⸻⸻⸻⸻⸻⸻" * 15)
    banco.commit()
    sistema_estoque()

'-------------------------------------------------'

def menu_categoria():
    try:
        print('╔═══════════════════════╗')
        print("   〘 Menu de Categoria 〙")
        print('╚═══════════════════════╝')
        EG = int(int(input('''1.Listar 
2.Cadastrar
3.Editar
4.Excluir
5.Pesquisar
0.Voltar para sistema de estoque
—»''')))
        print("⸻⸻⸻⸻⸻⸻" * 15)
    except:
        print("╭─━━━━━━━━━━━━atenção━━━━━━━━━━━━━─╮")
        print("          Opção inexistente!")
        print("⸻⸻⸻⸻⸻⸻" * 15)
        menu_categoria()
    else:
        if EG == 1:
            listar_categria()
        elif EG == 2:
            cadastrar_categoria()
        elif EG == 3:
            editar_categoria()
        elif EG == 4:
            excluir_categoria()
        elif EG == 5:
            pesquisar_categoria()
        elif EG == 0:
            sistema_estoque()
        else:
            print("╭─━━━━━━━━━━━━atenção━━━━━━━━━━━━━─╮")
            print("          Opção inexistente!")
            print("⸻⸻⸻⸻⸻⸻" * 15)
            menu_categoria()

def listar_categria():
    cursor = banco.cursor()
    comando_sql = "select * from categorias"
    cursor.execute(comando_sql)
    valores = cursor.fetchall()
    for i in valores:
        print("⸻⸻⸻⸻⸻⸻" * 15)
        print("Código: ", i[0])
        print("Nome: ", i[1])
        print("⸻⸻⸻⸻⸻⸻" * 15)
    menu_categoria()

def cadastrar_categoria():
    try:
        cursor=banco.cursor()
        comando_sql = "INSERT INTO categorias(cod_categoria,nome_categoria)values (%s,%s)"
        print("⸻⸻⸻⸻⸻⸻" * 15)
        cod = int(input("Insira o código da categoria: "))
        nome = (input("Insira o nome categoria: "))
        print("⸻⸻⸻⸻⸻⸻" * 15)
    except:
        print("╭─━━━━━━━━━━━━atenção━━━━━━━━━━━━━─╮")
        print("          Opção inexistente!")
        print("⸻⸻⸻⸻⸻⸻" * 15)
        menu_categoria()
    else:
        dados = (cod,nome)
        cursor.execute(comando_sql, dados)
        banco.commit()
        menu_categoria()

def editar_categoria():
    try:
        certo = 0
        cursor = banco.cursor()
        comando_sqla = "select cod_categoria,nome_categoria from categorias"
        cod = int(input("Insira o código do categoria: "))
        nome = input("Insira o novo nome do categoria: ")
        cursor.execute(comando_sqla)
    except:
        print("╭─━━━━━━━━━━━━atenção━━━━━━━━━━━━━─╮")
        print("          Opção inexistente!")
        print("⸻⸻⸻⸻⸻⸻" * 15)
        menu_cargo()
    else:
        valores = cursor.fetchall()
        for i in valores:
            if i[1] != nome and i[0] == cod:
                print("⸻⸻⸻⸻⸻⸻" * 15)
                print("Realizado com sucesso")
                comando_sql = "UPDATE categorias set nome_categoria = %s where cod_categoria = %s"
                dados=(nome,cod)
                cursor.execute(comando_sql,dados)
                banco.commit()
                print("⸻⸻⸻⸻⸻⸻" * 15)
                menu_categoria()
                certo = 1
        if certo == 0:
            print("╭─━━━━━━━━━━━━atenção━━━━━━━━━━━━━─╮")
            print("          Dados incorretos!")
            print("⸻⸻⸻⸻⸻⸻" * 15)
            menu_categoria()

def excluir_categoria():
    try:
        certo=0
        cursor = banco.cursor()
        comando_sqla = "select cod_categoria from categorias"
        cod=int(input("Insira o código da categoria: "))
        cursor.execute(comando_sqla)
    except:
        print("╭─━━━━━━━━━━━━atenção━━━━━━━━━━━━━─╮")
        print("          Opção inexistente!")
        print("⸻⸻⸻⸻⸻⸻" * 15)
        menu_categoria()
    else:
        valores = cursor.fetchall()
        for i in valores:
            if i[0] == cod:
                print("⸻⸻⸻⸻⸻⸻" * 15)
                print("Realizado com sucesso")
                comando_sql = "DELETE from categorias where cod_categoria = {}".format(cod)
                cursor.execute(comando_sql)
                banco.commit()
                print("⸻⸻⸻⸻⸻⸻" * 15)
                menu_categoria()
                certo = 1
        if certo == 0:
            print("╭─━━━━━━━━━━━━atenção━━━━━━━━━━━━━─╮")
            print("          Dados incorretos!")
            print("⸻⸻⸻⸻⸻⸻" * 15)
            menu_categoria()

def pesquisar_categoria():
    achei = 0
    cursor = banco.cursor()
    comando_sql = "select * from categorias"
    cursor.execute(comando_sql)
    nome=input("Insira o nome do categoria: ")
    valores_lidos = cursor.fetchall()
    for i in valores_lidos:
        if i[1] == nome:
            print("Código: ", i[0])
            print("Nome: ", i[1])
            print("⸻⸻⸻⸻⸻⸻" * 15)
            achei = 1
    if achei == 0:
        print("Categoria não encontrado!")
        print("⸻⸻⸻⸻⸻⸻" * 15)
    banco.commit()
    menu_categoria()

'-----------------------------------------------------------'

def sistema_fornecedor():
    try:
        print("▂▃▄▅▆▇█▓▒░ Sistema de Fornecedor ░▒▓█▇▆▅▄▃▂")
        ip=int(input('''1.Listar 
2.Cadastrar 
3.Excluir
4.Pesquisar 
0.Voltar para menu de opções
—» '''))
        print("⸻⸻⸻⸻⸻⸻" * 15)
    except:
        print("╭─━━━━━━━━━━━━atenção━━━━━━━━━━━━━─╮")
        print("          Opção inexistente!")
        print("⸻⸻⸻⸻⸻⸻" * 15)
        sistema_fornecedor()
    else:
        if ip == 1:
            listar_fornecedores()
        elif ip == 2:
            cadastrar_fornecedores()
        elif ip == 3:
            excluir_fornecedore()
        elif ip == 4:
            pesquisar_por_fornecedores()
        elif ip == 0:
            escopo_global()
        else:
            print("╭─━━━━━━━━━━━━atenção━━━━━━━━━━━━━─╮")
            print("          Opção inexistente!")
            print("⸻⸻⸻⸻⸻⸻" * 15)
            sistema_fornecedor()

def listar_fornecedores():
    cursor = banco.cursor()
    comando_sql = "select * from fornecedor"
    cursor.execute(comando_sql)
    valores = cursor.fetchall()
    for i in valores:
        print("⸻⸻⸻⸻⸻⸻" * 15)
        print("Código: ", i[0])
        print("Nome: ", i[1])
        print("CEP: ", i[2])
        print("CNPJ: ", i[3])
        print("Logradouro: ", i[4])
        print("Numero: ", i[5])
        print("Bairro: ", i[6])
        print("Cidade: ", i[7])
        print("Estado: ", i[8])
        print("Telefone: ", i[9])
        print("⸻⸻⸻⸻⸻⸻" * 15)
    sistema_fornecedor()

def cadastrar_fornecedores():
    try:
        cursor = banco.cursor()
        comando_sql = "INSERT INTO fornecedor (nome_fornecedor,cep,cnpj,logradouro,numero,bairro,cidade,estado,telefone) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        nome=input("Insira o nome do fornecedor: ")
        cep=input("Insira o CEP do fornecedor: ")
        cnpj=input("Insira o CNPJ do fornecedor: ")
        logradouro=input("Informe o logradouro do fornecedor: ")
        numero=input("Insira o numero do fornecedor: ")
        bairro=input("Insira o bairro do fornecedor: ")
        cidade=input("Informe a cidade do fornecedor: ")
        estado = input("Informe o estado do fornecedor: ")
        telefone = input("Insira o telefone do fornecedor: ")
        print("⸻⸻⸻⸻⸻⸻" * 15)
    except:
        print("╭─━━━━━━━━━━━━atenção━━━━━━━━━━━━━─╮")
        print("          Opção inexistente!")
        print("⸻⸻⸻⸻⸻⸻" * 15)
        sistema_fornecedor()
    else:
        dados = (nome,cep,cnpj,logradouro,numero,bairro,cidade,estado,telefone)
        cursor.execute(comando_sql,dados)
        banco.commit()
        sistema_fornecedor()

def excluir_fornecedore():
    try:
        certo=0
        cursor = banco.cursor()
        comando_sqla = "select cod_fornecedor from fornecedor"
        cod=int(input("Insira o código do fornecedor: "))
        cursor.execute(comando_sqla)
    except:
        print("╭─━━━━━━━━━━━━atenção━━━━━━━━━━━━━─╮")
        print("          Opção inexistente!")
        print("⸻⸻⸻⸻⸻⸻" * 15)
        sistema_fornecedor()
    else:
        valores = cursor.fetchall()
        for i in valores:
            if i[0] == cod:
                print("⸻⸻⸻⸻⸻⸻" * 15)
                print("Realizado com sucesso")
                comando_sql = "DELETE from fornecedor where cod_fornecedor = {}".format(cod)
                cursor.execute(comando_sql)
                banco.commit()
                print("⸻⸻⸻⸻⸻⸻" * 15)
                sistema_fornecedor()
                certo = 1
        if certo == 0:
            print("╭─━━━━━━━━━━━━atenção━━━━━━━━━━━━━─╮")
            print("          Dados incorretos!")
            print("⸻⸻⸻⸻⸻⸻" * 15)
            sistema_fornecedor()

def pesquisar_por_fornecedores():
    achei = 0
    cursor = banco.cursor()
    comando_sql = "select * from fornecedor"
    cursor.execute(comando_sql)
    nome=input("Insira o nome do fornecedor: ")
    valores_lidos = cursor.fetchall()
    for i in valores_lidos:
        if i[1] == nome:
            print("⸻⸻⸻⸻⸻⸻" * 15)
            print("Código: ", i[0])
            print("Nome: ", i[1])
            print("cep: ", i[2])
            print("CNPJ: ", i[3])
            print("Lagradouro: ", i[4])
            print("Numero: ", i[5])
            print("Bairro: ", i[6])
            print("Cidade: ", i[7])
            print("Estado: ", i[8])
            print("Telefone: ", i[9])
            print("⸻⸻⸻⸻⸻⸻" * 15)
            achei = 1
    if achei == 0:
        print("Fornecedor não encontrado!")
        print("⸻⸻⸻⸻⸻⸻" * 15)
    banco.commit()
    sistema_fornecedor()

'-------------------------------------------------'

def sistema_cliente():
    try:
        print("▂▃▄▅▆▇█▓▒░ Sistema de clientes ░▒▓█▇▆▅▄▃▂")
        lp=int(input('''1.Listar
2.Cadastrar 
3.Excluir 
4.Pesquisar 
0.Voltar para menu de opções
—» '''))
        print("⸻⸻⸻⸻⸻⸻" * 15)
    except:
        print("╭─━━━━━━━━━━━━atenção━━━━━━━━━━━━━─╮")
        print("          Opção inexistente!")
        print("⸻⸻⸻⸻⸻⸻" * 15)
        sistema_cliente()
    else:
        if lp == 1:
            listar_cliente()
        elif lp == 2:
            cadastrar_cliente()
        elif lp == 3:
            excluir_cliente()
        elif lp == 4:
            pesquisar_por_cliente()
        elif lp == 0:
            escopo_global()
        else:
            print("╭─━━━━━━━━━━━━atenção━━━━━━━━━━━━━─╮")
            print("          Opção inexistente!")
            print("⸻⸻⸻⸻⸻⸻" * 15)
            sistema_cliente()

def listar_cliente():
    cursor = banco.cursor()
    comando_sql = "select * from clientes"
    cursor.execute(comando_sql)
    valores = cursor.fetchall()
    for i in valores:
        print("⸻⸻⸻⸻⸻⸻" * 15)
        print("Código: ", i[0])
        print("Nome: ", i[1])
        print("Sexo: ", i[2])
        print("CEP: ", i[3])
        print("Logradouro: ", i[4])
        print("Numero: ", i[5])
        print("Bairro: ", i[6])
        print("Cidade: ", i[7])
        print("Cidade: ", i[8])
        print("Telefone: ", i[9])
        print("⸻⸻⸻⸻⸻⸻" * 15)
    sistema_cliente()

def cadastrar_cliente():
    try:
        cursor = banco.cursor()
        comando_sql = "INSERT INTO clientes (nome_cliente,sexo,cep,logradouro,numero,bairro,cidade,estado,telefone) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        nome=input("Insira o nome do cliente: ")
        sexo=input("Insira o sexo: ")
        cep=input("Insira o cep do cliente: ")
        lagradouro=(input("Informe o logradouro do cliente: "))
        numero=input("Insira o numero do cliente: ")
        bairro=input("Insira o bairro do cliente: ")
        cidade=input("Informe a cidade do cliente: ")
        estado = (input("Informe o estado do cliente: "))
        telefone = (input("Insira o telefone do cliente: "))
        print("⸻⸻⸻⸻⸻⸻" * 15)
    except:
        print("╭─━━━━━━━━━━━━atenção━━━━━━━━━━━━━─╮")
        print("          Opção inexistente!")
        print("⸻⸻⸻⸻⸻⸻" * 15)
        sistema_cliente()
    else:
        dados = (nome,sexo,cep,lagradouro,numero,bairro,cidade,estado,telefone)
        cursor.execute(comando_sql,dados)
        banco.commit()
        sistema_cliente()

def excluir_cliente():
    try:
        certo=0
        cursor = banco.cursor()
        comando_sqla = "select cod_cliente from clientes"
        cod=int(input("Insira o código do cliente: "))
        cursor.execute(comando_sqla)
    except:
        print("╭─━━━━━━━━━━━━atenção━━━━━━━━━━━━━─╮")
        print("          Opção inexistente!")
        print("⸻⸻⸻⸻⸻⸻" * 15)
        sistema_cliente()
    else:
        valores = cursor.fetchall()
        for i in valores:
            if i[0] == cod:
                print("⸻⸻⸻⸻⸻⸻" * 15)
                print("Realizado com sucesso")
                comando_sql = "DELETE from clientes where cod_cliente = {}".format(cod)
                cursor.execute(comando_sql)
                banco.commit()
                print("⸻⸻⸻⸻⸻⸻" * 15)
                sistema_cliente()
                certo = 1
        if certo == 0:
            print("╭─━━━━━━━━━━━━atenção━━━━━━━━━━━━━─╮")
            print("          Dados incorretos!")
            print("⸻⸻⸻⸻⸻⸻" * 15)
            sistema_cliente()

def pesquisar_por_cliente():
    achei = 0
    cursor = banco.cursor()
    comando_sql = "select * from clientes"
    cursor.execute(comando_sql)
    nome=input("Insira o nome do cliente: ")
    valores_lidos = cursor.fetchall()
    for i in valores_lidos:
        if i[1] == nome:
            print("⸻⸻⸻⸻⸻⸻" * 15)
            print("Código: ", i[0])
            print("Nome: ", i[1])
            print("Sexo: ", i[2])
            print("CEP: ", i[3])
            print("Logradouro: ", i[4])
            print("Numero: ", i[5])
            print("Bairro: ", i[6])
            print("Cidade: ", i[7])
            print("Cidade: ", i[8])
            print("Telefone: ", i[9])
            print("⸻⸻⸻⸻⸻⸻" * 15)
            achei = 1
    if achei == 0:
        print("Cliente não encontrado!")
    banco.commit()
    sistema_cliente()

'-------------------------------------------------'

def sistema_de_vendas():
    try:
        print("▂▃▄▅▆▇█▓▒░ Sistema de Vendas ░▒▓█▇▆▅▄▃▂")
        sv=int(input('''1.Vender produto
2.Relatorio de vendas
3.Pesquisa de vendas por data
4.Excluir uma venda
0.Voltar para menu de opções
—» '''))
        print("⸻⸻⸻⸻⸻⸻" * 15)
    except:
        print("╭─━━━━━━━━━━━━atenção━━━━━━━━━━━━━─╮")
        print("          Opção inexistente!")
        print("⸻⸻⸻⸻⸻⸻" * 15)
        sistema_de_vendas()
    else:
        if sv == 1:
            venda_de_produtos()
        elif sv == 2:
            relatorio_de_vendas()
        elif sv == 3:
            pesquisa_de_venda()
        elif sv == 4:
            excluir_venda()
        elif sv == 0:
            escopo_global()
        else:
            print("╭─━━━━━━━━━━━━atenção━━━━━━━━━━━━━─╮")
            print("          Opção inexistente!")
            print("⸻⸻⸻⸻⸻⸻" * 15)
            sistema_de_vendas()

def venda_de_produtos():
    try:
        cursor = banco.cursor()
        comando_sql = "INSERT INTO vendas(fk_cod_funcionario,fk_cod_cliente,fk_cod_produto,Data_," \
                  "quantidade,valor_unit,valor_total,desconto,acrescimo,valor_a_pagar)" \
                  "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        print("⸻⸻⸻⸻⸻⸻" * 15)
        cod_fun = int(input("Insira o código do funcionario: "))
        cod_cli = int(input("Insira o código do cliente: "))
        cod_pro = int(input("Insira o código do produto: "))
        data = input("Insira a data: ")
        quant = int(input("Insira o a quantidade: "))
        val_unit = float(input("Insira o valor por unidade: "))
        val_ttl = float(input("Insira o valor total da compra: "))
        descon = float(input("Insira o valor do desconto: "))
        acresci = float(input("Acrescimos da maquina: "))
        print("⸻⸻⸻⸻⸻⸻" * 15)
        val_pagar = val_ttl - descon + acresci
        print("Valor a pagar: ",val_pagar)
        print("⸻⸻⸻⸻⸻⸻" * 15)
        troco = float(input("Insira o valor pago: "))
        resu=troco-val_pagar
        print("Troco: ",resu)
    except:
        print("╭─━━━━━━━━━━━━atenção━━━━━━━━━━━━━─╮")
        print("          Opção inexistente!")
        print("⸻⸻⸻⸻⸻⸻" * 15)
        sistema_de_vendas()
    else:
        print("⸻⸻⸻⸻⸻⸻" * 15)
        dados = (cod_fun,cod_cli,cod_pro,data,quant,val_unit,val_ttl,descon,acresci,val_pagar)
        cursor.execute(comando_sql, dados)
        banco.commit()
        sistema_de_vendas()

def relatorio_de_vendas():
    cursor = banco.cursor()
    comando_sql = "select * from vendas"
    cursor.execute(comando_sql)
    valores = cursor.fetchall()
    for i in valores:
        print("⸻⸻⸻⸻⸻⸻" * 15)
        print("Código de venda: ", i[0])
        print("Código do funcionario: ", i[1])
        print("Código do cliente: ", i[2])
        print("Código do produto: ", i[3])
        print("Data da venda: ", i[4])
        print("Quantidade de produtos: ", i[5])
        print("Valor por unidade: ", i[6])
        print("Valor total: ", i[7])
        print("Desconto: ", i[8])
        print("Acrescimo do cartão: ", i[9])
        print("Valor total a pagar: ", i[10])
        print("⸻⸻⸻⸻⸻⸻" * 15)
    sistema_de_vendas()

def pesquisa_de_venda():
    achei = 0
    cursor = banco.cursor()
    comando_sql = "select * from vendas"
    cod = (input("Insira o código da venda: "))
    cursor.execute(comando_sql)
    valores_lidos = cursor.fetchall()
    for i in valores_lidos:
        if i[4] == cod:
            print("⸻⸻⸻⸻⸻⸻" * 15)
            print("Código de venda: ", i[0])
            print("Código do funcionario: ", i[1])
            print("Código do cliente: ", i[2])
            print("Código do produto: ", i[3])
            print("Data da venda: ", i[4])
            print("Quantidade de produtos: ", i[5])
            print("Valor por unidade: ", i[6])
            print("Valor total: ", i[7])
            print("Desconto: ", i[8])
            print("Acrescimo do cartão: ", i[9])
            print("Valor total a pagar: ", i[10])
            print("⸻⸻⸻⸻⸻⸻" * 15)
            achei = 1
    if achei == 0:
        print("Venda não encontrada!")
    banco.commit()
    sistema_de_vendas()

def excluir_venda():
    try:
        certo = 0
        cursor = banco.cursor()
        comando_sqla = "select cod_vendas from vendas"
        cod = int(input("Insira o código da venda: "))
        cursor.execute(comando_sqla)
    except:
        print("╭─━━━━━━━━━━━━atenção━━━━━━━━━━━━━─╮")
        print("          Opção inexistente!")
        print("⸻⸻⸻⸻⸻⸻" * 15)
        sistema_de_vendas()
    else:
        valores = cursor.fetchall()
        for i in valores:
            if i[0] == cod:
                print("⸻⸻⸻⸻⸻⸻" * 15)
                print("Realizado com sucesso")
                comando_sql = "DELETE from vendas where cod_vendas = {}".format(cod)
                cursor.execute(comando_sql)
                banco.commit()
                print("⸻⸻⸻⸻⸻⸻" * 15)
                sistema_de_vendas()
                certo = 1
        if certo == 0:
            print("╭─━━━━━━━━━━━━atenção━━━━━━━━━━━━━─╮")
            print("          Dados incorreto!")
            print("⸻⸻⸻⸻⸻⸻" * 15)
            sistema_de_vendas()
'-------------------------------------------------'



login()