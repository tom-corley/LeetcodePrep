class RecentCounter:

    def __init__(self):
        self.recent_reqs = []
        

    def ping(self, t: int) -> int:
        self.recent_reqs.append(t)
        while self.recent_reqs[0] < t - 3000:
            del self.recent_reqs[0]
        return len(self.recent_reqs)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)