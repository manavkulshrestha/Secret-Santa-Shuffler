import random

PARTICIPANT_COUNT = 11

participants = list(range(1,PARTICIPANT_COUNT+1))
participants_copy = participants[:]
final = {}

for i, participant in enumerate(participants):
	reciever_index = random.randint(0,len(participants_copy)-1)
	final[participant] = participants_copy[reciever_index]
	participants_copy.pop(reciever_index)

print('\n'.join(f'{k}: {v}' for k, v in final.items()))