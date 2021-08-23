number = float(input())
enter = input()
exits = input()

if enter == "mm":
    mm = enter
elif enter == "cm":
    cm = enter
else:
    m = enter

if enter == "mm" and exits == "cm":
    cm_sloved = 0.1 * number
    print(f"{cm_sloved:.3f}")
elif enter == "mm" and exits == "m":
    m_sloved = 0.001 * number
    print(f"{m_sloved:.3f}")
elif enter == "cm" and exits == "mm":
    mm_sloved = 10 * number
    print(f"{mm_sloved:.3f}")
elif enter == "cm" and exits == "m":
    m_sloved = 0.01 * number
    print(f"{m_sloved:.3f}")
elif enter == "m" and exits == "cm":
    cm_sloved = 100 * number
    print(f"{cm_sloved:.3f}")
else:
    mm_sloved = 1000 * number
    print(f"{mm_sloved:.3f}")