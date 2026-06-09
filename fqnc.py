t_pontos = [0, 2, 4, 6]
v_pontos = [10, 15, 12, 8]
h = 2

def simpson_3_8(y_pts, h_passo):
    n = len(y_pts)
    if n != 4:
        raise ValueError("A Regra 3/8 de Simpson requer exatamente 4 pontos.")

    f0, f1, f2, f3 = y_pts[0], y_pts[1], y_pts[2], y_pts[3]

    resultado = (3 * h_passo / 8) * (f0 + 3*f1 + 3*f2 + f3)
    return resultado

# execução

print("=" * 55)
print("  INTEGRAÇÃO — NEWTON-COTES (REGRA 3/8 DE SIMPSON)")
print("=" * 55)
print(f"  Dados: t={t_pontos}")
print(f"         v={v_pontos}  (MB/s)")
print(f"  h = {h} s")
print("-" * 55)

print(f"\n  Fórmula: I = (3h/8) * [f0 + 3f1 + 3f2 + f3]")
print(f"         = (3×{h}/8) × [{v_pontos[0]} + 3×{v_pontos[1]} + 3×{v_pontos[2]} + {v_pontos[3]}]")

total_mb = simpson_3_8(v_pontos, h)

inner = v_pontos[0] + 3*v_pontos[1] + 3*v_pontos[2] + v_pontos[3]
print(f"         = {3*h/8:.4f} × {inner}")
print("-" * 55)
print(f"  Total de dados transferidos: {total_mb:.6f} MB")
print("=" * 55)