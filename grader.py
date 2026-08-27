import sys
import io

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
        print("❌ Quase lá! O resultado impresso não é exatamente o esperado.")

