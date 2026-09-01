import sys
import io
import builtins
import re

def testar_exercicio_2(funcao_aluno):
    saida_capturada = io.StringIO()
    saida_original = sys.stdout
    sys.stdout = saida_capturada
    
    try:
        funcao_aluno()
    except Exception as e:
        sys.stdout = saida_original
        print(f"❌ Ocorreu um erro no seu código: {e}")
        return
    finally:
        sys.stdout = saida_original
    
    resultado_aluno = saida_capturada.getvalue().strip().split()
    
    gabarito = [str(i) for i in range(50, -1, -1)]
    
    if not resultado_aluno:
        print("⚠️ Seu programa não imprimiu nada. Lembre-se de usar a função print().")
    elif resultado_aluno == gabarito:
        print("✅ Parabéns! A contagem regressiva está perfeitamente correta.")
    else:
        print("❌ O resultado impresso não é exatamente o esperado.")

def testar_exercicio_3(funcao_aluno):
    respostas_simuladas = ['2', '1000', '2000']
    
    def mock_input(prompt=""):
        if respostas_simuladas:
            return respostas_simuladas.pop(0)
        return "0"

    saida_capturada = io.StringIO()
    saida_original = sys.stdout
    input_original = builtins.input
    
    sys.stdout = saida_capturada
    builtins.input = mock_input 
    
    try:
        funcao_aluno()
    except Exception as e:
        sys.stdout = saida_original
        builtins.input = input_original
        print(f"❌ Ocorreu um erro no seu código: {e}")
        return
    finally:
        sys.stdout = saida_original
        builtins.input = input_original

    texto_saida = saida_capturada.getvalue()
    
    texto_limpo = texto_saida.replace(',', '.')
    numeros_encontrados = re.findall(r'\b\d+(?:\.\d+)?\b', texto_limpo)
    numeros_float = [float(n) for n in numeros_encontrados]
    
    acertou_1075 = any(abs(n - 1075.0) < 0.1 for n in numeros_float)
    acertou_2150 = any(abs(n - 2150.0) < 0.1 for n in numeros_float)

    if acertou_1075 and acertou_2150:
        print("✅ Excelente! Os cálculos de reajuste (7,5%) estão corretos.")
    else:
        print("❌ Os valores impressos não bateram com o esperado.")

def rodar_com_mock(funcao, inputs_simulados=None):
    """Executa a função do aluno, injeta inputs e captura os prints."""
    saida = io.StringIO()
    old_stdout = sys.stdout
    old_input = builtins.input
    
    sys.stdout = saida
    
    def mock_input(prompt=""):
        if inputs_simulados and len(inputs_simulados) > 0:
            return str(inputs_simulados.pop(0))
        return "0"
    
    builtins.input = mock_input
    erro = None
    
    try:
        funcao()
    except Exception as e:
        erro = e
    finally:
        sys.stdout = old_stdout
        builtins.input = old_input
        
    return saida.getvalue().strip(), erro

def testar_ex4_e_9(funcao_aluno):
    # Ex 4 e 9: múltiplos de 4 do 1 ao 100
    saida, erro = rodar_com_mock(funcao_aluno)
    if erro: return print(f"❌ Ocorreu um erro: {erro}")
    
    nums = re.findall(r'\b\d+\b', saida)
    esperado = [str(i) for i in range(4, 101, 4)]
    
    if nums == esperado:
        print("✅ Perfeito! Todos os múltiplos de 4 foram impressos corretamente.")
    else:
        print("❌ Incorreto. Verifique a sua lógica do loop e do 'if'.")

def testar_ex5(funcao_aluno):
    # Ex 5: range com list() de 6 a 84 de 3 em 3
    saida, erro = rodar_com_mock(funcao_aluno)
    if erro: return print(f"❌ Ocorreu um erro: {erro}")
    
    nums = re.findall(r'\b\d+\b', saida)
    esperado = [str(i) for i in range(6, 85, 3)]
    
    if nums == esperado:
        print("✅ Excelente! O uso do list() e range() está perfeito.")
    else:
        print("❌ Incorreto. Lembre-se: range(início, fim, passo).")

def testar_ex10(funcao_aluno):
    # Ex 10: 10 notas, imprimir quantas >= 6
    notas_teste = [5, 6, 7, 4, 8, 9, 10, 3, 2, 6] # São 6 notas maiores ou iguais a 6
    saida, erro = rodar_com_mock(funcao_aluno, notas_teste)
    if erro: return print(f"❌ Ocorreu um erro: {erro}")
    
    # Busca o último número impresso na tela
    nums = re.findall(r'\b\d+\b', saida)
    if nums and nums[-1] == '6':
        print("✅ Parabéns! O seu contador funcionou perfeitamente.")
    else:
        print(f"❌ A contagem falhou. Para as notas de teste, esperávamos 6 aprovações.")

def testar_ex11(funcao_aluno):
    # Ex 11: Média de 10 notas com 2 casas decimais
    notas_teste = [10, 10, 10, 10, 5, 5, 5, 5, 0, 0] # Média exata é 6.00
    saida, erro = rodar_com_mock(funcao_aluno, notas_teste)
    if erro: return print(f"❌ Ocorreu um erro: {erro}")
    
    # Verifica se imprimiu 6.00 ou 6,00
    if '6.00' in saida or '6,00' in saida:
        print("✅ Tudo certo! O acumulador e a formatação (2 casas decimais) estão perfeitos.")
    else:
        print("❌ Erro no cálculo da média ou na formatação das casas decimais (.2f).")

def testar_ativ1(funcao_aluno):
    saida, erro = rodar_com_mock(funcao_aluno)
    esperado = [str(i) for i in range(10, -1, -1)]
    nums = re.findall(r'\b\d+\b', saida)
    if nums == esperado:
        print("✅ Correto! Contagem regressiva de 10 a 0 perfeita.")
    else:
        print("❌ Incorreto. Verifique se o loop vai de 10 até 0 inclusive.")

def testar_ativ2(funcao_aluno):
    inputs = [5, -6, -1, 0, 90, -45, 10, -8, 23, 11]
    saida, erro = rodar_com_mock(funcao_aluno, inputs)
    if '4' in saida:
        print("✅ Parabéns! O contador de números negativos (4) funcionou.")
    else:
        print("❌ Incorreto. Para os dados de teste, esperava-se encontrar 4 negativos.")

def testar_ativ3(funcao_aluno):
    inputs = [3, -1, 5, -9]
    saida, erro = rodar_com_mock(funcao_aluno, inputs)
    if '2' in saida:
        print("✅ Excelente! A leitura de N e o contador de negativos estão corretos.")
    else:
        print("❌ Incorreto. Para N=3 e entradas -1, 5, -9, esperava-se 2 negativos.")

def testar_ativ4(funcao_aluno):
    saida, erro = rodar_com_mock(funcao_aluno)
    esperado = [str(i) for i in range(0, 70, 7)]
    nums = re.findall(r'\b\d+\b', saida)
    if nums[:10] == esperado:
        print("✅ Muito bem! Os múltiplos de 7 estão corretos.")
    else:
        print(f"❌ Falhou. Esperado: {esperado}")

def testar_ativ5(funcao_aluno):
    saida, erro = rodar_com_mock(funcao_aluno, [11])
    if '165' in saida and '55' in saida:
        print("✅ Lógica dos acumuladores correta! Sucessores=165, Antecessores=55.")
    else:
        print("❌ Incorreto. Verifique a soma dos 10 sucessores e antecessores.")

def testar_ativ6_e_7(funcao_aluno, tipo):
    saida, erro = rodar_com_mock(funcao_aluno)
    nums = re.findall(r'\b\d+\b', saida)
    if (tipo == 6 and '40' in nums):
        print("✅ Perfeito! São 40 anos para a árvore B atingir a A.")
    elif (tipo == 7 and '35' in nums):
        print("✅ Cálculos de taxa de natalidade corretos.")
    else:
        print("❌ O tempo calculado não está de acordo com o gabarito.")

def testar_ativ8(funcao_aluno):
    saida, erro = rodar_com_mock(funcao_aluno, [5, 5, 5, 8, 8])
    if ('6.8' in saida or '6,8' in saida) and ('Aprovado' in saida or 'aprovado' in saida):
        print("✅ Média ponderada calculada e situação do aluno corretas.")
    else:
        print("❌ Erro na ponderação. A divisão final deve ser por 30 (soma dos pesos).")

def testar_ativ11(funcao_aluno):
    saida, erro = rodar_com_mock(funcao_aluno)
    if '20' in saida:
        print("✅ Correto! O programa encontrou exatas 20 vogais.")
    else:
        print("❌ Contagem incorreta. Lembre-se de contar vogais com acento (é).")

def testar_ativ12(funcao_aluno):
    saida, erro = rodar_com_mock(funcao_aluno, [987654321])
    if '9' in saida:
        print("✅ Excelente! A contagem de dígitos funcionou perfeitamente.")
    else:
        print("❌ Falhou ao contar a quantidade de dígitos inseridos.")

def testar_ativ9(funcao_aluno):
    saida, erro = rodar_com_mock(funcao_aluno, [12])
    if erro: return print(f"❌ Ocorreu um erro: {erro}")
    
    nums = re.findall(r'\b\d+\b', saida)
    if nums and nums[-1] == '6':
        print("✅ Excelente! O algoritmo identificou corretamente a quantidade de divisores.")
    else:
        print("❌ Incorreto. Testamos o seu código com o número 12.")
        print("   Esperávamos encontrar 6 divisores (1, 2, 3, 4, 6 e 12). Revise a lógica do loop e do módulo (%).")

def testar_ativ13(funcao_aluno):
    saida, erro = rodar_com_mock(funcao_aluno)
    if erro: return print(f"❌ Ocorreu um erro: {erro}")
    
    amostras_esperadas = [
        "1 x 1 = 1",
        "3 x 4 = 12",
        "5 x 5 = 25",
        "7 x 8 = 56",
        "9 x 9 = 81"
    ]
    
    saida_limpa = saida.replace(" ", "").lower()
    amostras_limpas = [a.replace(" ", "") for a in amostras_esperadas]
    
    todas_presentes = all(amostra in saida_limpa for amostra in amostras_limpas)
    
    if todas_presentes:
        print("✅ Sensacional! Os comandos de repetição aninhados geraram a tabuada perfeitamente.")
    else:
        print("❌ Incorreto ou incompleto. Verifique se os seus dois loops (interno e externo) estão indo de 1 até 9.")

def testar_ativ10(funcao_aluno):
    # Atividade 10: 3 cursos, 3 jogadores cada. Massa e Idade.[cite: 1]
    # Vamos fornecer 18 inputs simulados na seguinte ordem (Massa, Idade):
    # Curso 1: Todos com 60kg e 20 anos
    # Curso 2: Todos com 80kg e 22 anos
    # Curso 3: Todos com 100kg e 24 anos
    # Média Geral Esperada: 80kg e 22 anos.
    inputs_simulados = [
        60, 20, 60, 20, 60, 20,  # Jogadores do Curso 1
        80, 22, 80, 22, 80, 22,  # Jogadores do Curso 2
        100, 24, 100, 24, 100, 24 # Jogadores do Curso 3
    ]
    
    saida, erro = rodar_com_mock(funcao_aluno, inputs_simulados)
    
    # Tratamento caso o aluno tenha pedido "nomes" e nosso robô digitou números, quebrando o código
    if erro: 
        print(f"❌ Ocorreu um erro no seu código: {erro}")
        print("💡 Dica: Peça no input() APENAS a massa e a idade (exatamente nessa ordem).")
        print("Se você pediu o NOME do curso ou do jogador, o validador pode ter se confundido.")
        return
    
    # Extrai todos os números impressos
    nums = re.findall(r'\b\d+(?:\.\d+)?\b', saida.replace(',', '.'))
    
    # Verifica se as médias por curso (60, 80, 100 e 20, 22, 24) aparecem
    # e se a média geral (80 e 22) foi calculada e impressa corretamente.
    tem_medias_cursos = '60' in nums and '100' in nums and '24' in nums
    tem_media_geral = '80' in nums and '22' in nums
    
    if tem_medias_cursos and tem_media_geral:
        print("✅ Espetacular! As médias de cada curso e as médias gerais estão corretas.")
    elif tem_medias_cursos and not tem_media_geral:
        print("❌ Quase lá! Você acertou as médias de cada curso, mas errou (ou esqueceu) a média de TODOS os participantes.")
    else:
        print("❌ Incorreto. O resultado impresso não é o esperado.")
        print("   Testamos o seu código com jogadores de 60kg(20 anos), 80kg(22 anos) e 100kg(24 anos).")
        print("   Revise o local onde você está 'zerando' as variáveis de soma.")