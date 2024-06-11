questions = [
    ["What is my name ?:- ", "Satyam", "None", "Aniket", "Ankit", 1],
    ["What is my age ?:- ", 12, 16, 18, 21, 4],
    ["which city i live in ?:- ", "prayagraj", "None", "kanpur", "Delhi", 1],
    ["Which course i study currently ?:- ", "Bsc", "None", "B.tech", "MBA", 3],
    ["Which phone i use ?:- ", "Mi", "None", "Aplle", "Poco", 4],
    ["Which college i study ?:- ", "AITD", "None", "AITH", "IIT", 1],
    ["which bank account i have ?:- ", "BOB", "None", "SBI", "CANARA", 1],
]


levels = [1000, 2000, 3000, 4000, 5000, 10000, 50000]
money = 0
for i in range(0, len(questions)):
    question = questions[i]
    print(f"question for ₹ {levels[i]} is --")
    print(f"\n{question[0]}")
    print(f"a.{question[1]}  b.{question[2]}  c.{question[3]}  d.{question[4]}")
    reply = int(input(("Choose your answer from above options(1-4): ")))
    if reply == question[5]:
        print("************************Coreect answer!!*************************")
        print(f"total_money = {levels[i]}\n")
        if i == 3:
            money = 4000
        elif i == 5:
            money = 10000
        elif i == 6:
            money = 50000

    else:
        print("***************************looser********************************\n")
        print(f"total_money = {levels[i-1]}\n")
        break

print(f"Your take home money is {money}")
