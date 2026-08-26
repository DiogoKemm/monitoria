import builtins
import io
import re
from contextlib import redirect_stdout

def test_exercicio_3(user_func):
    def rodar(entradas):
        saida = io.StringIO()
        it = iter(entradas)
        orig = builtins.input
        builtins.input = lambda *args, **kwargs: str(next(it))
        try:
            with redirect_stdout(saida):
                user_func()
        finally:
            builtins.input = orig
        return saida.getvalue()

    def extrair_nums(texto):
        return [float(n.replace(',', '.')) for n in re.findall(r'\b\d+(?:[\.,]\d+)?\b', texto)]

    try:
        s1 = rodar(["2", "1000", "2000"])
        n1 = extrair_nums(s1)
        assert any(abs(n - 1075.0) < 0.01 for n in n1), "Erro: Salário de 1000 corrigido (1075.0) não encontrado."
        assert any(abs(n - 2150.0) < 0.01 for n in n1), "Erro: Salário de 2000 corrigido (2150.0) não encontrado."

        s2 = rodar(["1", "3500"])
        n2 = extrair_nums(s2)
        assert any(abs(n - 3762.5) < 0.01 for n in n2), "Erro: Salário de 3500 corrigido (3762.5) não encontrado."

        print("✅ Todos os testes passaram!")
    except AssertionError as e:
        print(f"❌ Teste Falhou: {e}")
    except Exception as e:
        print(f"⚠️ Erro: {e}")