"""
*SISTEMA ACADÊMICO*
PROGRAMADORA: Rayssa Bravin
ULTIMA MODIFICAÇÃO: 05/12/2025, 16:30
"""
#listas globais para conferir se cadastros foram feitos
laluno_cadastrado=[]
ldisciplina_cadastrada=[]
lnota_cadastrada=[]

# Listas que guardam os nomes das disciplinas
ldisciplina1=[]
ldisciplina2=[]
ldisciplina3=[]
ldisciplina4=[]
ldisciplina5=[]

# Listas que guardam as notas das disciplinas
lnota1=[]
lnota2=[]
lnota3=[]
lnota4=[]
lnota5=[]

# Variáveis globais que serão preenchidas pelo cadastro
nome_do_aluno=None
situacao1=None
situacao2=None
situacao3=None
situacao4=None
situacao5=None

# Variáveis auxiliares
reprovacoes=0
resultado=None

# Dados completos do aluno
nome=None
nascimento=None
sexo=None
nacionalidade=None
cpf=None
email=None
telefone=None
telefone2=None

"""Cadastro do estudante"""
def cadastro_estudante():
    global laluno_cadastrado
    # Confere se já existe aluno cadastrado
    if laluno_cadastrado:    
        print("Já existe um aluno cadastrado")
        print("==================================================")
        menu()
    else:
        print("==================================================")
        print("              CADASTRO DO ESTUDANTE              ")
        print("==================================================")
        print("        Insira as informações do estudante      ")
        
        # Variáveis globais
        global nome, nascimento, sexo, nacionalidade, cpf, email, telefone, telefone2
        
        #Valida o nome
        print("--------------------------------------------------")
        nome = input("Nome completo: ").strip()
        while len(nome) < 3 or len(nome.split()) < 2:
            print(" ")
            print("Nome inválido. Digite o nome completo.")
            nome = input("Nome completo: ").strip()
        global nome_do_aluno
        nome_do_aluno = nome

        #Valida a data de nascimento
        print("--------------------------------------------------")
        nascimento = input("Data de nascimento (DD/MM/AAAA): ").strip()
        dia = nascimento[0:2]
        mes = nascimento[3:5]
        ano = nascimento[6:10]
        while (len(nascimento) != 10 or nascimento[2] != "/" or nascimento[5] != "/" or not dia.isdigit() or not mes.isdigit() or not ano.isdigit() or int(dia) < 1 or int(dia) > 31 or int(mes) < 1 or int(mes) > 12 or len(ano) != 4):
            print(" ")
            print("Data inválida. Use o formato DD/MM/AAAA.")
            nascimento = input("Data de nascimento (DD/MM/AAAA): ").strip()
            dia = nascimento[0:2]
            mes = nascimento[3:5]
            ano = nascimento[6:10]

        #Valida o sexo do estudante
        print("--------------------------------------------------")
        sexo = input("Sexo (Masculino/Feminino/Outro): ").strip().upper()
        while sexo not in ["MASCULINO", "FEMININO", "OUTRO"]:
            print(" ")
            print("Sexo inválido. Digite Masculino/Feminino/Outro.")
            sexo = input("Sexo (Masculino/Feminino/Outro): ").strip().upper()

        #inserir a nacionalidade
        print("--------------------------------------------------")
        nacionalidade = str(input("Nacionalidade: "))
        while len(nacionalidade)< 3:
            print(" ")
            print("Nacionalidade inválida.")
            nacionalidade = str(input("Nacionalidade: "))
        
        #Valida o CPF
        print("--------------------------------------------------")
        cpf = input("CPF (XXX.XXX.XXX-XX): ").strip()

        # Tenta até ser válido
        cpf_limpo = ''.join(filter(str.isdigit, cpf))
        while True:
            cpf_limpo = ''.join(filter(str.isdigit, cpf))
            valido = True
            # Verifica tamanho
            if len(cpf_limpo) != 11:
                valido = False
            # Verifica repetição
            elif cpf_limpo == cpf_limpo[0] * 11:
                valido = False
            else:
                # Primeiro dígito
                soma = 0
                for i in range(9):
                    soma += int(cpf_limpo[i]) * (10 - i)
                resto = soma % 11
                digito1 = 0 if resto < 2 else 11 - resto
                if digito1 != int(cpf_limpo[9]):
                    valido = False
                # Segundo dígito
                if valido:
                    soma = 0
                    for i in range(10):
                        soma += int(cpf_limpo[i]) * (11 - i)
                    resto = soma % 11
                    digito2 = 0 if resto < 2 else 11 - resto
                    if digito2 != int(cpf_limpo[10]):
                        valido = False
            if valido:
                # sai do loop substituindo pelo próprio cpf válido
                break
            else:
                print(" ")
                print("CPF inválido. Digite novamente.")
                cpf = input("CPF: ").strip()

        #Valida o e-mail
        print("--------------------------------------------------")
        email = str(input("E-mail: "))
        while "@" not in email or "." not in email:
            print(" ")
            print("E-mail inválido.")
            email = input("E-mail: ")
        
        #Valida o telefone 1
        print("--------------------------------------------------")
        telefone=input("Telefone para contato: ").strip()
        while len(telefone) < 8:
            print(" ")
            print("Telefone inválido.")
            telefone = input("Telefone para contato: ").strip()
        
        #Valida o telefone 2
        print("--------------------------------------------------")
        telefone2=input("Telefone para contato (2° opção): ").strip()
        while len(telefone2) < 8:
            print(" ")
            print("Telefone inválido.")
            telefone2 = input("Telefone para contato (2° opção): ").strip()
        
        print("--------------------------------------------------")
        print(" ")
        print("          Aluno cadastrado com sucesso!           ")
        print(" ")
        print("==================================================")
        print("||||||||||||||||||||||||||||||||||||||||||||||||||")
        #Confirma que o aluno foi cadastrado
        laluno_cadastrado.append(1)
        #chama o MENU
        menu()
    
"""Cadastro das disciplinas"""
def cadastro_das_disciplinas():
    global ldisciplina_cadastrada
    #Confere se existe aluno cadastrado
    if not laluno_cadastrado:   
        print("Nenhum cadastro de aluno foi encontrado")
        print("==================================================")
        menu()
    # Confere se já existem disciplinas cadastradas
    elif ldisciplina_cadastrada:    
        print("Já existem disciplinas cadastradas")
        print("==================================================")
        menu()
    #recebe as disciplinas 
    else:
        print("==================================================")
        print("             CADASTRO DAS DISCIPLINAS             ")
        print("==================================================")
        print(" ")
        print("--------------------------------------------------")
        disciplina1 = str(input("Cadastre a primeira disciplina: "))
        print("--------------------------------------------------")
        disciplina2 = str(input("Cadastre a segunda disciplina: "))
        print("--------------------------------------------------")
        disciplina3 = str(input("Cadastre a terceira disciplina: "))
        print("--------------------------------------------------")
        disciplina4 = str(input("Cadastre a quarta disciplina: "))
        print("--------------------------------------------------")
        disciplina5 = str(input("Cadastre a quinta disciplina: "))
        print("--------------------------------------------------")
        print(" ")
        print("        Disciplinas cadastradas com sucesso!  ")
        print(" ")
        print("==================================================")
        print("||||||||||||||||||||||||||||||||||||||||||||||||||")
        #Confirma que as disciplinas foram cadastradas
        global ldisciplina1
        global ldisciplina2
        global ldisciplina3
        global ldisciplina4
        global ldisciplina5
        ldisciplina_cadastrada.append(1)
        ldisciplina1.append(disciplina1)
        ldisciplina2.append(disciplina2)
        ldisciplina3.append(disciplina3)
        ldisciplina4.append(disciplina4)
        ldisciplina5.append(disciplina5)
        #Chama o menu
        menu()

"""Cadastro das notas de cada discliplina"""
def cadastro_das_notas():
    global lnota_cadastrada
    #Confere se existe aluno e materias cadastradas
    if not laluno_cadastrado or not ldisciplina_cadastrada:   
        print("Nenhum cadastro de aluno ou disciplina foi")
        print("encontrado")
        print("==================================================")
        menu()
    #Confere se existem notas cadastradas cadastradas
    elif lnota_cadastrada:    
        print("Já existem notas cadastradas")
        print("==================================================")
        menu()
    #Recebe as notas e confere se elas são válidas
    else:  
        print("==================================================")
        print("                CADASTRO DAS NOTAS                ")
        print("==================================================")
        print(" ")
        print("--------------------------------------------------")
        print(ldisciplina1[0])
        nota1 = float(input(" NOTA: "))
        while nota1<0 or nota1>10:
            print(" ")
            print("Nota inválida. Digite novamente.")
            nota1 = float(input(" NOTA: "))
        print("--------------------------------------------------")
        print(ldisciplina2[0])
        nota2 = float(input(" NOTA: "))
        while nota2<0 or nota2>10:
            print(" ")
            print("Nota inválida. Digite novamente.")
            nota2 = float(input(" NOTA: "))
        print("--------------------------------------------------")
        print(ldisciplina3[0])
        nota3 = float(input(" NOTA: "))
        while nota3<0 or nota3>10:
            print(" ")
            print("Nota inválida. Digite novamente.")
            nota3 = float(input(" NOTA: "))
        print("--------------------------------------------------")
        print(ldisciplina4[0])
        nota4 = float(input(" NOTA: "))
        while nota4<0 or nota4>10:
            print(" ")
            print("Nota inválida. Digite novamente.")
            nota4 = float(input(" NOTA: "))
        print("--------------------------------------------------")
        print(ldisciplina5[0])
        nota5 = float(input(" NOTA: "))
        while nota5<0 or nota5>10:
            print(" ")
            print("Nota inválida. Digite novamente.")
            nota5 = float(input(" NOTA: "))
        print("--------------------------------------------------")
        print(" ")
        print("           Notas cadastradas com sucesso!  ")
        print(" ")
        print("==================================================")
        print("||||||||||||||||||||||||||||||||||||||||||||||||||")
        #Confirma que as notas foram cadastradas
        lnota_cadastrada.append(1)
        lnota1.append(nota1)
        lnota2.append(nota2)
        lnota3.append(nota3)
        lnota4.append(nota4)
        lnota5.append(nota5)

        # Determina situação de cada disciplina
        global situacao1, situacao2, situacao3, situacao4, situacao5
        if nota1==10:
            situacao1="Aprovado com distinção"
        elif nota1>=6:
            situacao1="Aprovado"
        else:
            situacao1="Reprovado"

        if nota2==10:
            situacao2="Aprovado com distinção"
        elif nota2>=6:
            situacao2="Aprovado"
        else:
            situacao2="Reprovado"

        if nota3==10:
            situacao3="Aprovado com distinção"
        elif nota3>=6:
            situacao3="Aprovado"
        else:
            situacao3="Reprovado"

        if nota4==10:
            situacao4="Aprovado com distinção"
        elif nota4>=6:
            situacao4="Aprovado"
        else:
            situacao4="Reprovado"

        if nota5==10:
            situacao5="Aprovado com distinção"
        elif nota5>=6:
            situacao5="Aprovado"
        else:
            situacao5="Reprovado"

        # Conta quantas reprovações houve
        global reprovacoes
        reprovacoes = sum([
            situacao1=="Reprovado",
            situacao2=="Reprovado",
            situacao3=="Reprovado",
            situacao4=="Reprovado",
            situacao5=="Reprovado"
        ])

        # Resultado final do aluno
        global resultado
        if reprovacoes == 0:
            resultado = "PASSOU DE ANO DIRETO"
        elif reprovacoes <= 2:
            resultado = "PASSOU DE ANO COM DEPENDÊNCIA"
        else:
           resultado = "RETIDO"
           
        #Chama o menu
        menu()
        
""" MOSTRA SITUAÇÃO DAS DISCIPLINAS """
def situacao_das_disciplinas():
    #Confere se existe aluno, materias cadastradas e notas cadastradas
    if not laluno_cadastrado or not ldisciplina_cadastrada or not lnota_cadastrada:   
        print("Nenhum cadastro de aluno, disciplina ou nota foi ")
        print("encontrado")
        print("==================================================")
        menu()
    else:
        print("==================================================")
        print("            SITUAÇÃO DAS DISCIPLINAS                ")
        print("==================================================")
        global nome_do_aluno
        print(nome_do_aluno)
        print(" ")
        print("DISCIPLINA\t\tNOTA\t\tSITUAÇÃO")
        print("==================================================")
        print("%s\t\t%1.f\t\t%s"%(ldisciplina1[0], lnota1[0], situacao1))
        print("--------------------------------------------------")
        print("%s\t\t%1.f\t\t%s"%(ldisciplina2[0], lnota2[0], situacao2))
        print("--------------------------------------------------")
        print("%s\t\t%1.f\t\t%s"%(ldisciplina3[0], lnota3[0], situacao3))
        print("--------------------------------------------------")
        print("%s\t\t%1.f\t\t%s"%(ldisciplina4[0], lnota4[0], situacao4))
        print("--------------------------------------------------")
        print("%s\t\t%1.f\t\t%s"%(ldisciplina5[0], lnota5[0], situacao5))
        print("==================================================")
        sair_disciplina = input("Digite E para SAIR: ").strip().upper()
        while sair_disciplina not in ["E"]:
            print(" ")
            sair_disciplina = input("Digite E para SAIR: ").strip().upper()
        print("==================================================")
        print("||||||||||||||||||||||||||||||||||||||||||||||||||")
        menu()

""" SITUAÇÃO GERAL DO ESTUDANTE """     
def situacao_do_estudante():
    #Confere se existe aluno, materias cadastradas e notas cadastradas
    if not laluno_cadastrado or not ldisciplina_cadastrada or not lnota_cadastrada:   
        print("Nenhum cadastro de aluno, disciplina ou nota foi ")
        print("encontrado")
        print("==================================================")
        menu()
    else:
        print("==================================================")
        print("              SITUAÇÃO DO ESTUDANTE                ")
        print("==================================================")
        global nome_do_aluno
        print(nome_do_aluno)
        print(" ")
        print("DISCIPLINA\t\tSITUAÇÃO")
        print("==================================================")
        print("%s\t\t%s"%(ldisciplina1[0], situacao1))
        print("--------------------------------------------------")
        print("%s\t\t%s"%(ldisciplina2[0], situacao2))
        print("--------------------------------------------------")
        print("%s\t\t%s"%(ldisciplina3[0], situacao3))
        print("--------------------------------------------------")
        print("%s\t\t%s"%(ldisciplina4[0], situacao4))
        print("--------------------------------------------------")
        print("%s\t\t%s"%(ldisciplina5[0], situacao5))
        print("==================================================")
        global resultado
        print(" ")
        print("O ALUNO %s"%(resultado))
        print(" ")
        print("==================================================")
        sair_estudante = input("Digite E para SAIR: ").strip().upper()
        while sair_estudante not in ["E"]:
            print(" ")
            sair_estudante = input("Digite E para SAIR: ").strip().upper()
        print("==================================================")
        print("||||||||||||||||||||||||||||||||||||||||||||||||||")
        menu()

""" RESULTADO FINAL COMPLETO """
def resultado_final():
    #Confere se existe aluno, materias cadastradas e notas cadastradas
    if not laluno_cadastrado or not ldisciplina_cadastrada or not lnota_cadastrada:   
        print("Nenhum cadastro de aluno, disciplina ou nota foi ")
        print("encontrado")
        print("==================================================")
        menu()
    else:
        print("==================================================")
        print("                 RESULTADO FINAL                ")
        print("==================================================")
        global nome
        global nascimento
        global sexo
        global nacionalidade
        global cpf
        global email
        global telefone
        global telefone2
        print(" ")
        print("                CADASTRO DO ALUNO")
        print("==================================================")
        print("NOME: ",nome)
        print("--------------------------------------------------")
        print("DATA DE NASCIMENTO: ",nascimento)
        print("--------------------------------------------------")
        print("SEXO: ",sexo)
        print("--------------------------------------------------")
        print("NACIONALIDADE: ",nacionalidade)
        print("--------------------------------------------------")
        print("CPF: ", cpf)
        print("--------------------------------------------------")
        print("E-MAIL: ", email)
        print("--------------------------------------------------")
        print("TELEFONE: ", telefone)
        print("--------------------------------------------------")
        print("TELEFONE2: ", telefone2)
        print("==================================================")
        print(" ")
        print("DISCIPLINA\t\tSITUAÇÃO")
        print("==================================================")
        print("%s\t\t%s"%(ldisciplina1[0], situacao1))
        print("--------------------------------------------------")
        print("%s\t\t%s"%(ldisciplina2[0], situacao2))
        print("--------------------------------------------------")
        print("%s\t\t%s"%(ldisciplina3[0], situacao3))
        print("--------------------------------------------------")
        print("%s\t\t%s"%(ldisciplina4[0], situacao4))
        print("--------------------------------------------------")
        print("%s\t\t%s"%(ldisciplina5[0], situacao5))
        print("==================================================")
        print(" ")
        print("SITUAÇÃO DO ALUNO:", resultado )
        print(" ")
        print("==================================================")
        sair_resultado = input("Digite E para SAIR: ").strip().upper()
        while sair_resultado not in ["E"]:
            print(" ")
            sair_resultado = input("Digite E para SAIR: ").strip().upper()
        print("==================================================")
        print("||||||||||||||||||||||||||||||||||||||||||||||||||")
        menu()
    
"""Define o MENU PRINCIPAL"""
def menu ():
    print("==================================================")
    print("                 SISTEMA ACADÊMICO                ")
    print("==================================================")
    print("                  Seja bem-vindo!                 ")
    print(" ")
    print("==================================================")
    print("                       MENU                       ")
    print("==================================================")
    print("- Digite 1 para CADASTRO DO ESTUDANTE")
    print("- Digite 2 para CADASTRO DAS DISCIPLINAS")
    print("- Digite 3 para CADASTRO DAS NOTAS")
    print("- Digite 4 para SITUAÇÃO DAS DISCIPLINAS")
    print("- Digite 5 para SITUAÇÃO DO ESTUDANTE")
    print("- Digite 6 para RESULTADO FINAL")
    print("- Digite 0 para SAIR")
    print("==================================================")
    opcao =int(input("Digite sua opção: "))
    #Confere se a opção existe
    while opcao not in [1,2,3,4,5,6,0]:
        print(" ")
        opcao =int(input("Opção inválida. Digite sua opção: "))
    print("==================================================")
    print("||||||||||||||||||||||||||||||||||||||||||||||||||")
    #envia o usuário para a opçao escolhida
    if opcao == 1:
        cadastro_estudante()
    elif opcao == 2:
        cadastro_das_disciplinas()
    elif opcao == 3:
        cadastro_das_notas()
    elif opcao == 4:
        situacao_das_disciplinas()
    elif opcao == 5:
        situacao_do_estudante()
    elif opcao == 6:
        resultado_final()
    else:
        exit()

teste_exp = 2 ** 3       
teste_resto = 10 % 3    

#Inicia o programa
menu()

