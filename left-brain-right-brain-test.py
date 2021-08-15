an1, an2, an3, an4, an5, an6, an7 = "", "", "", "", "", "", ""
err = "1 혹은 2를 입력해서 선택하세요."

print("좌뇌형인지 우뇌형인지에 따라 장단점과 사고방식이 다르다고 하는데 당신은 좌뇌형일까요? 우뇌형일까요?\n")
print("해당 검사는 총 7문항이 나오며 문항마다 바로 떠오르는 것을 체크하시면 됩니다.\n\n\n\n")

print("➀  양손 깍지를 꼈을 때 어느 손 엄지손가락이 위로 올라가나요?\n\n")
print("1. 오른쪽 2. 왼쪽\n\n")
while an1 != "1" or an1 != "2":
    if an1 != "":
        print(err)
    an1 = input("1, 2 중 선택: ")
    if an1 == "1" or an1 == "2":
        break

print("\n\n\n\n➁  책상이 정돈되어 있을 때 집중이 잘 되나요? 아니면 물건이 흐트러져 있을 때 집중이 더 잘 되나요?\n")
print("1. 정돈되어 있을 때 2. 흐트러져 있을 때\n\n")
while an2 != "1" or an2 != "2":
    if an2 != "":
        print(err)
    an2 = input("1, 2 중 선택: ")
    if an2 == "1" or an2 == "2":
        break

print("\n\n\n\n➂  팔짱을 꼈을 때 어느 쪽 팔이 위로 올라가나요?\n")
print("1. 오른팔 2. 왼팔\n\n")
while an3 != "1" or an3 != "2":
    if an3 != "":
        print(err)
    an3 = input("1, 2 중 선택: ")
    if an3 == "1" or an3 == "2":
        break

print("\n\n\n\n➃  노래를 들을 때 더 관심이 가는 부분은 무엇인가요?\n")
print("1. 가사 2. 멜로디\n\n")
while an4 != "1" or an4 != "2":
    if an4 != "":
        print(err)
    an4 = input("1, 2 중 선택: ")
    if an4 == "1" or an4 == "2":
        break

print("\n\n\n\n➄  어렸을 때 당신은 왼손잡이였나요. 아니면 오른손잡이였나요?\n")
print("1. 오른손잡이 2. 왼손잡이\n\n")
while an5 != "1" or an5 != "2":
    if an5 != "":
        print(err)
    an5 = input("1, 2 중 선택: ")
    if an5 == "1" or an5 == "2":
        break

print("\n\n\n\n➅  다리를 꼬았을 때 올라가는 다리는?\n")
print("1. 오른쪽 2. 왼쪽\n\n")
while an6 != "1" or an6 != "2":
    if an6 != "":
        print(err)
    an6 = input("1, 2 중 선택: ")
    if an6 == "1" or an6 == "2":
        break

print("\n\n\n\n➆  한쪽씩 코를 막고 숨을 쉬어 보세요.\n어느 방향으로 숨을 쉬었을 때 더 시원하게 느껴지시나요?\n")
print("1. 오른쪽 코를 막고 왼쪽으로 숨을 쉬었을 때 시원하다 2.왼쪽 코를 막고 오른쪽 코로 숨을 쉬었을 때 시원하다\n\n")
while an7 != "1" or an7 != "2":
    if an7 != "":
        print(err)
    an7 = input("1, 2 중 선택: ")
    if an7 == "1" or an7 == "2":
        break

data = [an1, an2, an3, an4, an5, an6, an7]
left = data.count("1")
right = data.count("2")

print(f"\n\n\n\n\n\n\n\n\n\n======= [ 응답 결과 ] =======\n1번 응답: {left}번 | 2번 응답: {right}번\n\n")

if left > right:
    print("당신은 <좌뇌 우세형 인간> 입니다.\n")
    print("<좌뇌 우세형 인간>은 논리력/수리력/추리력/언어표현 능력 등이 뛰어나 분석적이면서 계획적이고 현실적인 것을 선호하는 특징이 있습니다.")
    print("다만 창의적인 부분이 조금 부족하고 계산적이기 때문에 자칫하면 이기적인 인간으로 보일 수 있다는 단점이 있다고 합니다.")
else:
    print("당신은 <우뇌 우세형 인간> 입니다.\n")
    print("<우뇌 우세형 인간>은 상상력이 풍부하고 감상적이어서 미술과 음악 같은 예체능 계열에 두각을 보이며, 긍정적인 성격을 가진다는 특징이 있습니다.")
    print("하지만 계획이 없어 즉흥적으로 행동하는 습성이 있으며 다소 덜렁대는 단점이 있다고 합니다.")

input()
