def main(num):
    if num >= 90:
        print("A")
    elif 80 <= num < 90:
        print("B")
    elif 70 <= num < 80:
        print("C")
    elif 60 <= num < 70:
        print("D")
    else:
        print("F")

num = 100
main(num)