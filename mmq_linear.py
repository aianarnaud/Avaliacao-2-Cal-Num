x_pontos = [8, 9, 10, 11, 12]
y_pontos = [2.1, 2.8, 3.1, 4.0, 4.8]
x_prever = 13


def mmq_linear(x_pts, y_pts):
    n = len(x_pts)

    soma_x  = 0.0
    soma_y  = 0.0
    soma_x2 = 0.0
    soma_xy = 0.0

    for i in range(n):
        soma_x  += x_pts[i]
        soma_y  += y_pts[i]
        soma_x2 += x_pts[i] ** 2
        soma_xy += x_pts[i] * y_pts[i]

    print(f"\n  Somatórios:")
    print(f"    n     = {n}")
    print(f"    Σx    = {soma_x}")
    print(f"    Σy    = {soma_y}")
    print(f"    Σx²   = {soma_x2}")
    print(f"    Σ(xy) = {soma_xy}")

    
    det = soma_x2 * n - soma_x * soma_x

    a = (soma_xy * n   - soma_y  * soma_x) / det
    b = (soma_x2 * soma_y - soma_x * soma_xy) / det

    return a, b


def calcular_r2(x_pts, y_pts, a, b):
    n = len(y_pts)
    media_y = sum(y_pts) / n

    ss_res = 0.0
    ss_tot = 0.0
    for i in range(n):
        y_pred = a * x_pts[i] + b
        ss_res += (y_pts[i] - y_pred) ** 2
        ss_tot += (y_pts[i] - media_y) ** 2

    return 1 - ss_res / ss_tot


# execução

print("=" * 55)
print("  AJUSTE DE CURVAS — MMQ LINEAR")
print("=" * 55)
print(f"  Dados: x={x_pontos}")
print(f"         y={y_pontos}")
print(f"  Prever em x={x_prever}")
print("-" * 55)

a, b = mmq_linear(x_pontos, y_pontos)
r2   = calcular_r2(x_pontos, y_pontos, a, b)
prev = a * x_prever + b

print("-" * 55)
sinal_b = "+" if b >= 0 else "-"
print(f"  Equação: P1(x) = {a:.6f}x {sinal_b} {abs(b):.6f}")
print(f"  R²     = {r2:.6f}  (1.0 = ajuste perfeito)")
print(f"  Previsão às {x_prever}h: {prev:.6f} mil acessos")
print("=" * 55)