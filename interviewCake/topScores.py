# https://www.interviewcake.com/question/python3/top-scores?utm_source=drip&utm_medium=email&utm_campaign=Our+7+most+important+coding+interview+tips+%281+a+day+for+a+week%2C+unsubscribe+any+time%29&utm_content=Patterns+for+breaking+down+questions+you+haven%27t+seen+before.

def sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE):
	scores = [0]*(HIGHEST_POSSIBLE_SCORE+1)

	for s in unsorted_scores:
		scores[s] += 1

	sorted_scores = []

	for i in range(HIGHEST_POSSIBLE_SCORE, -1, -1):
		if scores[i] > 0:
			sorted_scores.extend([i]*scores[i])

	return sorted_scores


unsorted_scores = [37, 37, 89, 41, 65, 91, 53]
HIGHEST_POSSIBLE_SCORE = 100

# Returns [91, 89, 65, 53, 41, 37, 37]
print(sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE))
