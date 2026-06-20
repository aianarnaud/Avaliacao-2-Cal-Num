def f(x):
    return 5*x**3 + x**2 - 12*x + 4


def raiz_quadrada(n, tolerancia=1e-12):
    if n < 0:
        raise ValueError("Raiz de número negativo.")
    if n == 0:
        return 0.0
    x = n
    for _ in range(100):
        x_novo = (x + n / x) / 2
        if abs(x_novo - x) < tolerancia:
            return x_novo
        x = x_novo
    return x

def quadratura_gauss(funcao, a, b, n_pontos):
    sqrt3 = raiz_quadrada(3)
    sqrt_3_5 = raiz_quadrada(3 / 5)

    tabela = {
        2: {
            "pontos": [-1 / sqrt3, 1 / sqrt3],
            "pesos":  [1.0, 1.0]
        },
        3: {
            "pontos": [-sqrt_3_5, 0.0, sqrt_3_5],
            "pesos":  [5/9, 8/9, 5/9]
        }
    }

    if n_pontos not in tabela:
        raise ValueError("Apenas n=2 ou n=3 suportados.")

    pts = tabela[n_pontos]["pontos"]
    wts = tabela[n_pontos]["pesos"]

    fator = (b - a) / 2
    meio  = (a + b) / 2

    soma = 0.0
    print(f"\n  Pontos de Gauss (n={n_pontos}) no intervalo [{a}, {b}]:")
    for i in range(n_pontos):
        t_i = pts[i]
        x_i = fator * t_i + meio
        f_i = funcao(x_i)
        contrib = wts[i] * f_i
        soma += contrib
        print(f"    t_{i} = {t_i:+.8f}  →  x_{i} = {x_i:+.8f}  "
              f"f(x)={f_i:+.6f}  w={wts[i]:.4f}  contrib={contrib:+.6f}")

    resultado = fator * soma
    return resultado


#execução

a, b = -1, 1

print("=" * 60)
print("  INTEGRAÇÃO — QUADRATURA DE GAUSS (FQG)")
print("=" * 60)
print(f"  f(x) = 5x³ + x² - 12x + 4")
print(f"  Intervalo: [{a}, {b}]")
print("-" * 60)

res_n2 = quadratura_gauss(f, a, b, n_pontos=2)

print("-" * 60)
print(f"  Resultado (n=2): ∫f(x)dx ≈ {res_n2:.6f}")
print()

# Valor analítico para conferência
# ∫(5x³+x²-12x+4)dx = 5x⁴/4 + x³/3 - 6x² + 4x  de -1 a 1
# = (5/4 + 1/3 - 6 + 4) - (5/4 - 1/3 - 6 - 4)
# = 2*(1/3) + 2*4 = 2/3 + 8 → simplificando...
def antiderivada(x):
    return (5/4)*x**4 + (1/3)*x**3 - 6*x**2 + 4*x

analitico = antiderivada(1) - antiderivada(-1)
print(f"  Valor analítico exato : {analitico:.6f}")
print(f"  Erro absoluto (n=2)   : {abs(res_n2 - analitico):.2e}")
print("=" * 60)