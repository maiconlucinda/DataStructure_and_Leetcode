import time
import os

# ============================================================
#  SIMULAÇÃO VISUAL — Merge Sorted Array (Two Pointers)
#  Rode com: python3 two_pointers_visual.py
# ============================================================

SLOW = 1.5  # segundos entre cada passo (ajuste se quiser mais rápido/lento)

# Cores ANSI para o terminal
RED    = "\033[91m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
BLUE   = "\033[94m"
CYAN   = "\033[96m"
BOLD   = "\033[1m"
DIM    = "\033[2m"
RESET  = "\033[0m"

def clear():
    os.system("clear" if os.name == "posix" else "cls")

def draw(nums1, nums2, m, n, last, step, action, highlight_idx=None, source=None):
    clear()

    print(f"{BOLD}{'='*60}{RESET}")
    print(f"{BOLD}  MERGE SORTED ARRAY — Simulação Passo a Passo{RESET}")
    print(f"{BOLD}{'='*60}{RESET}")
    print()

    # ---- nums1 ----
    print(f"  {BOLD}nums1:{RESET}  ", end="")
    for i, val in enumerate(nums1):
        if highlight_idx is not None and i == highlight_idx:
            print(f" {GREEN}{BOLD}[{val}]{RESET}", end="")  # valor recém-escrito
        elif val == 0 and i >= m + n - (len(nums2) - n):
            print(f" {DIM}[{val}]{RESET}", end="")  # espaço vazio (zero)
        else:
            print(f" [{val}]", end="")
    print()

    # ---- ponteiros de nums1 ----
    print("          ", end="")
    for i in range(len(nums1)):
        if i == m - 1 and m > 0:
            print(f" {RED}{BOLD} m↑ {RESET}", end="")
        elif i == last:
            print(f" {YELLOW}{BOLD} L↑ {RESET}", end="")
        else:
            print("     ", end="")
    print()

    # ---- nums2 ----
    print(f"  {BOLD}nums2:{RESET}  ", end="")
    for i, val in enumerate(nums2):
        if i == n - 1 and n > 0:
            print(f" {CYAN}{BOLD}[{val}]{RESET}", end="")  # ponteiro ativo
        else:
            print(f" {DIM}[{val}]{RESET}", end="")
    print()

    # ---- ponteiro de nums2 ----
    print("          ", end="")
    for i in range(len(nums2)):
        if i == n - 1 and n > 0:
            print(f" {CYAN}{BOLD} n↑ {RESET}", end="")
        else:
            print("     ", end="")
    print()

    # ---- legenda ----
    print()
    print(f"  {RED}m{RESET} = ponteiro de nums1 (posição {m-1 if m > 0 else '—'})")
    print(f"  {CYAN}n{RESET} = ponteiro de nums2 (posição {n-1 if n > 0 else '—'})")
    print(f"  {YELLOW}L{RESET} = last — onde vou escrever (posição {last})")
    print()
    print(f"  {BOLD}Passo {step}:{RESET} {action}")
    print()
    print(f"{'='*60}")


def run():
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    m = 3
    n = 3
    last = m + n - 1
    step = 0

    # ---- Estado inicial ----
    draw(nums1, nums2, m, n, last, step,
         f"Estado inicial.\n"
         f"           nums1 tem {m} valores reais + {n} espaços vazios.\n"
         f"           nums2 tem {n} valores.\n"
         f"           Vamos preencher nums1 {BOLD}de trás pra frente{RESET}.")
    input(f"\n  {DIM}[Pressione ENTER para o próximo passo]{RESET}")

    while m > 0 and n > 0:
        step += 1

        val_m = nums1[m - 1]
        val_n = nums2[n - 1]

        # ---- Mostrar comparação ----
        compare_text = (
            f"Comparo: nums1[{m-1}]={RED}{val_m}{RESET}  vs  nums2[{n-1}]={CYAN}{val_n}{RESET}\n"
        )

        if val_m > val_n:
            compare_text += (
                f"           {RED}{val_m}{RESET} > {CYAN}{val_n}{RESET} "
                f"→ copio {RED}{BOLD}{val_m}{RESET} para posição {YELLOW}{last}{RESET}\n"
                f"           Recuo {RED}m{RESET} (m -= 1) e {YELLOW}last{RESET} (last -= 1).\n"
                f"           {CYAN}n NÃO se move.{RESET}"
            )
            draw(nums1, nums2, m, n, last, step, compare_text)
            input(f"\n  {DIM}[Pressione ENTER para aplicar]{RESET}")

            nums1[last] = val_m
            m -= 1
            draw(nums1, nums2, m, n, last, step, compare_text, highlight_idx=last, source="m")
            last -= 1
            time.sleep(0.5)

        else:
            compare_text += (
                f"           {CYAN}{val_n}{RESET} >= {RED}{val_m}{RESET} "
                f"→ copio {CYAN}{BOLD}{val_n}{RESET} para posição {YELLOW}{last}{RESET}\n"
                f"           Recuo {CYAN}n{RESET} (n -= 1) e {YELLOW}last{RESET} (last -= 1).\n"
                f"           {RED}m NÃO se move.{RESET}"
            )
            draw(nums1, nums2, m, n, last, step, compare_text)
            input(f"\n  {DIM}[Pressione ENTER para aplicar]{RESET}")

            nums1[last] = val_n
            n -= 1
            draw(nums1, nums2, m, n, last, step, compare_text, highlight_idx=last, source="n")
            last -= 1
            time.sleep(0.5)

        input(f"\n  {DIM}[Pressione ENTER para o próximo passo]{RESET}")

    # ---- Se sobraram elementos em nums2 ----
    while n > 0:
        step += 1
        action = (
            f"Sobrou elemento em nums2: {CYAN}{BOLD}{nums2[n-1]}{RESET}\n"
            f"           Copio para posição {YELLOW}{last}{RESET}.\n"
            f"           Recuo {CYAN}n{RESET} e {YELLOW}last{RESET}."
        )
        draw(nums1, nums2, m, n, last, step, action)
        input(f"\n  {DIM}[Pressione ENTER para aplicar]{RESET}")

        nums1[last] = nums2[n - 1]
        n -= 1
        last -= 1

    # ---- Resultado final ----
    step += 1
    clear()
    print(f"{BOLD}{'='*60}{RESET}")
    print(f"{BOLD}  MERGE SORTED ARRAY — RESULTADO FINAL{RESET}")
    print(f"{BOLD}{'='*60}{RESET}")
    print()
    print(f"  {BOLD}nums1:{RESET}  ", end="")
    for val in nums1:
        print(f" {GREEN}{BOLD}[{val}]{RESET}", end="")
    print()
    print()
    print(f"  {GREEN}{BOLD}✓ Merge completo!{RESET} Array ordenado: {nums1}")
    print()
    print(f"  {BOLD}O que aconteceu:{RESET}")
    print(f"  • Usamos 3 ponteiros: {RED}m{RESET}, {CYAN}n{RESET}, {YELLOW}last{RESET}")
    print(f"  • A cada passo, comparamos e {BOLD}só um ponteiro de dados andou{RESET}")
    print(f"  • O ponteiro {YELLOW}last{RESET} (onde escrever) andou {BOLD}sempre{RESET}")
    print(f"  • Preenchemos de trás pra frente → sem sobrescrever nada")
    print()
    print(f"{'='*60}")
    print()


if __name__ == "__main__":
    run()
