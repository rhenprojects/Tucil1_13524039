import itertools
import time
import os

# Pembacaan file & validasi 
current_dir = os.path.dirname(__file__)
case_folder = os.path.join(current_dir, "..", "test", "test_cases")

files = [f for f in os.listdir(case_folder)]

if not files:
    print("Tidak ada file test case ditemukan.")
    exit()

print("Daftar Test Case yang Tersedia:")
for i, file in enumerate(files, start=1):
    print(f"{i}. {file}")

while True:
    try:
        choice = int(input("Pilih nomor test case yang ingin dijalankan: "))
        if 1 <= choice <= len(files):
            selected_file = files[choice - 1]
            break
        else:
            print("Pilihan tidak valid.")
    except ValueError:
        print("Masukkan angka yang valid.")

file_path = os.path.join(case_folder, selected_file)

color = []

with open(file_path, "r") as f:
    for line in f:
        clean_line = line.strip()
        if clean_line:
            color.append(list(clean_line))

if len(color) == 0:
    print("File kosong.")
    exit()

N = len(color)
if any(len(row) != N for row in color):
    print("Input tidak valid: Matriks harus berbentuk persegi (N x N).")
    exit()

live_update_input = input("Aktifkan live update? (Ya/Tidak): ").strip().lower()
live_update = live_update_input == "ya"

# Utility untuk memeriksa kolom diagonal dan warna
def check_color(arr):
    used_colors = set()
    for col in range(N):
        r = arr[col]
        c = color[r][col]
        if c in used_colors:
            return False
        used_colors.add(c)
    return True

def check_diagonal(arr):
    for col in range(N - 1):
        if abs(arr[col] - arr[col + 1]) == 1:
            return False
    return True

# Algoritma Brute-Force
iteration_count = 0
start_time = time.time()
last_update_time = time.time()
solution = None

for perm in itertools.permutations(range(N)):
    iteration_count += 1

    if live_update:
        current_time = time.time()
        if current_time - last_update_time >= 0.02:
            elapsed = int((current_time - start_time) * 1000)
            print(f"Iteration: {iteration_count} | Time: {elapsed} ms")
            last_update_time = current_time

    if check_color(perm) and check_diagonal(perm):
        solution = perm
        break

time_count = int((time.time() - start_time) * 1000)

# Handler Output Solusi
if solution:
    result_board = [row.copy() for row in color]
    for c in range(N):
        result_board[solution[c]][c] = '#'

    for row in result_board:
        print(''.join(row))

    print(f"Waktu pencarian: {time_count} ms")
    print(f"Banyak kasus yang ditinjau: {iteration_count} kasus")

    save = input("Apakah Anda ingin menyimpan solusi? (Ya/Tidak): ").strip().lower()
    if save == 'ya':
        current_dir = os.path.dirname(__file__)
        solution_folder = os.path.join(current_dir, "..", "test", "test_solutions")
        os.makedirs(solution_folder, exist_ok=True)
        base_name = os.path.splitext(selected_file)[0]
        solution_filename = f"solusi_{base_name}.txt"

        solution_path = os.path.join(solution_folder, solution_filename)

        with open(solution_path, "w") as f:
            for row in result_board:
                f.write(''.join(row) + '\n')

        print(f"Solusi tersimpan di '{solution_filename}'.")

else:
    print("Tidak ditemukan solusi.")
    print(f"Banyak kasus yang ditinjau: {iteration_count} kasus")
    print(f"Waktu pencarian: {time_count} ms")
