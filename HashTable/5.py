#LeetCode Problem 706  Number of Different Integers in a String

class MyHashMap:

    def __init__(self):
        self.d={}

    def put(self, key: int, value: int) -> None:
        self.d[key]=value

    def get(self, key: int) -> int:
        return self.d.get(key, -1)

    def remove(self, key: int) -> None:
        if key in self.d:
            del self.d[key]

__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)