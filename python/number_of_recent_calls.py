from copy import copy

class RecentCounter:

    def __init__(self):
        self.requests = []      

    def ping(self, t: int) -> int:
        self.requests.append(t)
        curr = self.requests.copy()
        for elem in self.requests:
            if (t - 3000) > elem:
                curr.remove(elem)
        self.requests = curr
        return len(self.requests)
        