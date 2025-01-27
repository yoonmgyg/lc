class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        mentions = [0] * numberOfUsers
        userOnline = {i: [True, 0] for i in range(numberOfUsers)}
        
        def mentionOnline(time, id):
            if userOnline[id][0] or userOnline[id][1] + 60 <= time:
                mentions[id] += 1 

        events.sort(key=lambda x: (int(x[1]), 0 if x[0] == "OFFLINE" else 1))

            
        for event in events:
            message = event[0]
            timestamp = int(event[1])
            mentions_string = event[2]
            if message == "OFFLINE":
                userOnline[int(event[2])] = [False, timestamp]
            else:
                if mentions_string == "ALL":
                    for i in range(numberOfUsers):
                        mentions[i] += 1
                elif mentions_string == "HERE":
                    for user in userOnline.keys():
                        mentionOnline(timestamp, user)
                else:
                    tokens = mentions_string.split()
                    for token in tokens:
                        user = int(token[2:])
                        mentionOnline(timestamp, user)
        return mentions
                
