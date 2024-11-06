panel = [
            ["C", "B", "C"],
            ["A", "A", "E"],
            ["D", "C", "C"]
        ]

coder_code = int(input("Coder code: "))

def show():
    for i in panel:
        for j in i:
            print(j + " ", end="")
        print()


def change_color(color):
    color_sequence = ["A", "B", "C", "D", "E"]
    return color_sequence[((color_sequence.index(color) + 1)%5)]


def sphere_1():
    panel[0][0] = change_color(panel[0][0])
    panel[0][1] = change_color(panel[0][1])
    panel[1][0] = change_color(panel[1][0])

def sphere_2():
    panel[0][0] = change_color(panel[0][0])
    panel[0][1] = change_color(panel[0][1])
    panel[0][2] = change_color(panel[0][2])
    panel[1][0] = change_color(panel[1][0])
    panel[1][1] = change_color(panel[1][1])
    panel[1][2] = change_color(panel[1][2])

def sphere_3():
    panel[0][2] = change_color(panel[0][2])
    panel[1][2] = change_color(panel[1][2])
    panel[1][1] = change_color(panel[1][1])

def sphere_4():
    panel[1][0] = change_color(panel[1][0])
    panel[1][1] = change_color(panel[1][1])

def sphere_5():
    panel[1][0] = change_color(panel[1][0])
    panel[1][1] = change_color(panel[1][1])
    panel[1][2] = change_color(panel[1][2])
    panel[2][0] = change_color(panel[2][0])
    panel[0][2] = change_color(panel[0][2])

def sphere_6():
    panel[1][2] = change_color(panel[1][2])
    panel[1][1] = change_color(panel[1][1])
    
def sphere_7():
    panel[2][0] = change_color(panel[2][0])
    panel[1][0] = change_color(panel[1][0])

def sphere_8():
    panel[2][1] = change_color(panel[2][1])
    panel[1][0] = change_color(panel[1][0])
    panel[1][2] = change_color(panel[1][2])

def sphere_9():
    panel[2][2] = change_color(panel[2][2])
    panel[1][1] = change_color(panel[1][1])

show()
print()

for n in str(coder_code):
    if(n == '0'):
        continue
    
    change_patterns = [sphere_1,sphere_2,sphere_3,sphere_4,sphere_5,sphere_6,sphere_7,sphere_8,sphere_9]
    pattern_n = change_patterns[int(n)-1]
    pattern_n()

show()
print()

final_code = ""
for i in panel:
    final_code += "".join(i)
print(f"code: {final_code}")
