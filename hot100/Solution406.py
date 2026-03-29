# 高个子先排好，他们的相对顺序不会再被矮个子影响；

# 矮个子插入时，只需根据自己的 k 位置插入，因为他们不会影响比自己高的人的“前面有多少个更高的人”计数。



class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        sorted_people = sorted(people, key=lambda x: (-x[0], x[1]))
        queue = []
        for people in sorted_people:
            queue.insert(people[1],people)
        return queue