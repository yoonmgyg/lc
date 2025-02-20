# Use array as map, and use modulo with key to use index as location of map
class MyHashMap:
    def __init__(self):
        self.map = []
        for _ in range(1000):
            self.map.append(Node())

    def put(self, key: int, value: int) -> None:
        cur = self.map[self.hash(key)]

        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return
                
            cur = cur.next

        cur.next = Node(key, value)

    def get(self, key: int) -> int:
        cur = self.map[self.hash(key)]

        while cur.next:
            if cur.next.key == key:
                return cur.next.val
            cur = cur.next

        return -1
        
    def remove(self, key: int) -> None:
        cur = self.map[self.hash(key)]

        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return

            cur = cur.next

    def hash(self, key):
        return key % len(self.map)        
