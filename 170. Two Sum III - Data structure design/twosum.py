class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.dict[number] = self.dict.get(number, 0) + 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for k in self.dict.keys():
            if value - k in self.dict:
                if value - k == k and self.dict[k] <= 1:
                    continue
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
