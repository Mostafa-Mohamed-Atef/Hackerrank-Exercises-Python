n_english = int(input())
students_en = set(map(int,input().strip().split()))
n_french = int(input())
students_fr = set(map(int,input().strip().split()))
intersection = students_en.intersection(students_fr)
print(len(intersection))