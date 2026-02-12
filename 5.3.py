'''3.	WAP to input a list of scores for N students in a list data type.
 Find the score of the runner-up and print the output.
Sample Input
N = 5
Scores= 2 3 6 6 5
Sample output
5
Note: Given list is [2, 3, 6, 6, 5]. The maximum score is 6, second maximum is 5. Hence, we print 5 as the runner-up score.
'''
n = int(input("Enter the number of students: "))
scores = []
for i in range(n):
    score = float(input("Enter the score of student {}: ".format(i+1)))
    scores.append(score)
unique_scores = list(set(scores))
unique_scores.sort()

if len(unique_scores) < 2:
    print("There is no runner-up score.")
else:
    runner_up_score = unique_scores[-2]
    print("The runner-up score is: {}".format(runner_up_score))
