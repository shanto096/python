import os

# Make sure the 'tables' directory exists
os.makedirs("tables", exist_ok=True)

def genaretnamota(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} x {i} = {n*i}\n"

    # Move file writing outside the loop
    with open(f"tables/table_{n}.txt", "w") as f:
        f.write(table)

for i in range(2, 101):
    genaretnamota(i)
