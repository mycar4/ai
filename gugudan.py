def print_all_gugudan():
    for dan in range(2, 10):
        print(f"--- {dan}단 ---")
        for i in range(1, 10):
            print(f"{dan} x {i} = {dan * i}")
        print()

if __name__ == "__main__":
    print_all_gugudan()
