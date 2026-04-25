
anime = ["Dandadan", "Jujutsu Kaisen", "Spy x Family"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

data = [
    [2, 3, 1, 2, 4],
    [1, 0, 2, 1, 0],
    [0, 1, 2, 1, 3]
]

def print_all():
    for i in range(len(anime)):
        print(f"{anime[i]:15} - {data[i]}")

def select_anime():
    for i, name in enumerate(anime):
        print(f"[{i}] {name}")
    choice = int(input("Enter choice: "))
    if 0 <= choice < len(anime):
        print(f"\n{anime[choice]:15} - {data[choice]}")

def update_data():
    for i, name in enumerate(anime):
        print(f"[{i}] {name}")
    r = int(input("Enter choice: "))
    for i, day in enumerate(days):
        print(f"[{i}] {day}")
    c = int(input("Enter choice: "))
    new_val = int(input("Enter new data: "))
    data[r][c] = new_val
    print(f"\nUpdating number of episodes of {anime[r]} watched on {days[c]} to {new_val}")
    print(f"Updated data: {anime[r]} - {data[r]}")

def summarize():
    for i, row in enumerate(data):
        total = sum(row)
        avg = total / len(row)
        mn = min(row)
        mx = max(row)
        print(f"{anime[i]:15} - Total Episodes Watched: {total:<3} | Average: {avg:.1f} | Min: {mn} | Max: {mx}")

while True:
    print("\n[1] Print all data")
    print("[2] Select anime")
    print("[3] Update data")
    print("[4] Summarize data")
    print("[5] Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        print_all()
    elif choice == "2":
        select_anime()
    elif choice == "3":
        update_data()
    elif choice == "4":
        summarize()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
