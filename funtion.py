def welcome():
    print("="*50)
    print("Welcome to the grade calculator")
    print("="*50)

def get_test_scores():
    score1 = float(input("Enter 1st test score: "))
    score2 = float(input("Enter 2nd test score: "))
    score3 = float(input("Enter 3rd test score: "))
    return score1, score2, score3


def average(score1, score2, score3):
    average = score1+score2+score3/3
    print(f"The average of {score1}, {score2}, and {score3} is: {average: .2f}")
    return average


def lettergra(average):
    if average >= 90:
        print("You got an A!")
    elif average >= 80:
        print("You got a B!")
    elif average >= 70:
        print("You got a C!")
    elif average >= 60:
        print("You got a D!")
    else:
        print("You failed this test go take it again!")


def main():
    welcome()
    score1 , score2, score3 = get_test_scores()
    avg = average(score1,score2,score3)
    lettergra(avg)

main()