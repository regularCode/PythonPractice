# Leetcode 621
"""
You are given an array of CPU tasks, each represented by letters A to Z, and a cooling time, n.
Each cycle or interval allows the completion of one task. Tasks can be completed in any order, but there's a constraint:
    identical tasks must be separated by at least n intervals due to cooling time.

Input: tasks = ["A","A","A","B","B","B"], n = 2

Output: 8

Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.
"""
import collections
import heapq
from collections import Counter


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        task_counter = Counter(tasks)

        counter_task = [(-count, task) for task, count in task_counter.items()]
        heapq.heapify(counter_task)

        waitingQueue = collections.deque()
        time = 0
        ans = []
        while counter_task or waitingQueue:
            time += 1
            if counter_task:
                task_count, task = heapq.heappop(counter_task)
                ans.append(task)
                if task_count + 1 != 0:
                    waitingQueue.append((time + n, (task_count + 1, task)))
            else:
                ans.append("idle")

            if waitingQueue and waitingQueue[0][0] == time:
                temp, (task_count, task) = waitingQueue.popleft()
                heapq.heappush(counter_task, (task_count, task))

        print(ans)
        return ans

if __name__ == '__main__':
    s = Solution()
    s.leastInterval(["A","A","A","B","B","B"], 2)