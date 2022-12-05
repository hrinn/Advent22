from heapq import heappop, heappush, heapify

f = open("input", "r")
lines = f.readlines()

heap = []
heapify(heap)

current = 0

for line in lines:
    if line == "\n":
        heappush(heap, current * -1)
        current = 0
    else:
        current = current + int(line.strip())


top_3 = heappop(heap) + heappop(heap) + heappop(heap)
print(top_3 * -1)