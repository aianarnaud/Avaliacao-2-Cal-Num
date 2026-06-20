t_pontos = [0.0, 0.5, 1.0, 1.5, 2.0]
v_pontos = [0, 40, 65, 80, 90]

def trapezios_repetida(x_pts, y_pts):
    n = len(x_pts)
    h = x_pts[1] - x_pts[0]  # passo (uniforme)

    soma = y_pts[0] + y_pts[n - 1]
    for i in range(1, n - 1):
        soma += 2 * y_pts[i]

    resultado = (h / 2) * soma
    return resultado, h


def simpson_1_3(x_pts, y_pts):
    n = len(x_pts)
    if (n - 1) % 2 != 0:
        raise ValueError("Simpson 1/3 requer número par de intervalos (n-1 par).")

    h = x_pts[1] - x_pts[0]

    soma = y_pts[0] + y_pts[n - 1]
    for i in range(1, n - 1):
        if i % 2 == 0:
            soma += 2 * y_pts[i]
        else:
            soma += 4 * y_pts[i]

    resultado = (h / 3) * soma
    return resultado, h


#execução

print("=" * 55)
print("  INTEGRAÇÃO — TRAPÉZIOS E SIMPSON 1/3")
print("=" * 55)
print(f"  Dados: t={t_pontos}")
print(f"         v={v_pontos}  (km/h)")
print("-" * 55)

res_trap, h_trap = trapezios_repetida(t_pontos, v_pontos)
res_simp, h_simp = simpson_1_3(t_pontos, v_pontos)

print(f"\n  Trapézios Repetida:")
print(f"    h = {h_trap}")
print(f"    I = h/2 × [f0 + 2(f1+f2+f3) + f4]")
print(f"      = {h_trap}/2 × [{v_pontos[0]} + 2×({v_pontos[1]}+{v_pontos[2]}+{v_pontos[3]}) + {v_pontos[4]}]")
print(f"    Distância ≈ {res_trap:.6f} km")

print(f"\n  Simpson 1/3 Repetida:")
print(f"    h = {h_simp}")
print(f"    I = h/3 × [f0 + 4f1 + 2f2 + 4f3 + f4]")
print(f"      = {h_simp}/3 × [{v_pontos[0]} + 4×{v_pontos[1]} + 2×{v_pontos[2]} + 4×{v_pontos[3]} + {v_pontos[4]}]")
print(f"    Distância ≈ {res_simp:.6f} km")

print("-" * 55)
print(f"  Trapézios : {res_trap:.6f} km")
print(f"  Simpson   : {res_simp:.6f} km")
print("=" * 55)