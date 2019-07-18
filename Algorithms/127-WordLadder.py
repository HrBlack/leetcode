# 方法一：基本的BFS，改进在于没有显式地将字母替换为a-z，而是替换成了_
from collections import deque  # 双向队列，从两侧pop元素都是O(1)复杂度

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def process_word_list(wordList):
            # 先处理词表，把词表所能表示的所有情况都列出来
            d = {}
            for word in wordList:
                for i in range(len(word)):
                    s = word[:i] + '_' + word[i+1:]
                    d[s] = d.get(s, []) + [word]
            return d
        
        def bfs(begin, end, d):
            queue = deque([(begin, 1)])  # 要把队列中的信息存成结构体：(value，index)
            visited = set()  # visited应该存的是单词，不能存带'_'的
            while queue:
                item, step = queue.popleft()
                if item not in visited:
                    visited.add(item)
                else:
                    continue
                if item == end:
                    return step
                for i in range(len(item)):
                    word = item[:i] + '_' + item[i+1:]
                    if word in d.keys():
                        for v in d[word]:
                            queue.append((v, step+1))
            return 0
        
        d = process_word_list(set(wordList))
        return bfs(beginWord, endWord, d)
            
# 方法二：最基本的BFS，但是超时了;
# 相比于上面的方法，它选择将a-z分别替换在word里，复杂度提升了26倍
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue, visited = [(beginWord, 1)], set()
        while queue:
            word, step = queue.pop(0)
            if word not in visited:
                visited.add(word)
            else:
                continue
            for i in range(len(word)):
                for letter in 'abcdefghijklmnopqrstuvwxyz':
                    item = word[:i] + letter + word[i+1:]
                    if item in wordList and item == endWord:
                        return step + 1  # 注意题目的要求，即step的定义
                    if item in wordList and item not in visited:
                        queue.append((item, step+1))
        return 0

# 方法三：双向BFS
# 当起止点都已知的时候，可以用双向BFS提升速度：每次都从需要遍历数目少的那个方向开始找
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 一定注意，endWord必须在wordList里面，这是题目规则
	# 上次在这里被卡了好久
        if endWord not in wordList:
            return 0
        forward = {beginWord}
        backward = {endWord}
        wordList = set(wordList) - forward
        step = 2
        # wordList.discard(beginWord)
        while forward:
            # 三个for循环叠加，需要注意顺序！
            forward = wordList & {word[:i] + letter + word[i+1:] for word in forward for i in range(len(word)) for letter in 'abcdefghigklmnopqrstuvwxyz'}
            if forward & backward:
                return step
            # 优化的核心：谁的数目少就从谁那里开始遍历
            if len(forward) > len(backward):
                forward, backward = backward, forward
            step += 1
            wordList -= forward
        return 0
