from datetime import datetime

s = input("Enter a single line: ").strip()
if s:
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now():%Y-%m-%d %H:%M:%S} - {s}\n")
    print("Appended to log.txt")

