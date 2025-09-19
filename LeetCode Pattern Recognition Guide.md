# LeetCode Pattern Recognition Guide
## How to Identify Problem Patterns from Keywords

### 🎯 Two Pointers Pattern
**Keywords to Look For:**
- "sorted array/list"
- "pair", "triplet", "subarray"
- "target sum"
- "palindrome"
- "reverse"
- "in-place"
- "remove duplicates"
- "merge two arrays/lists"
- "container with water"

**Example Problems:**
- Two Sum (sorted array variant)
- 3Sum
- Valid Palindrome
- Container With Most Water

**When to Use:** Problems involving searching pairs/triplets in sorted arrays, or problems requiring comparison of elements from both ends.

---

### 🪟 Sliding Window Pattern
**Keywords to Look For:**
- "subarray", "substring"
- "contiguous"
- "window"
- "maximum/minimum length"
- "at most K", "exactly K"
- "longest", "shortest"
- "consecutive"

**Example Problems:**
- Longest Substring Without Repeating Characters
- Maximum Sum Subarray of Size K
- Minimum Window Substring

**When to Use:** Problems asking for optimal contiguous sequences with specific constraints.

---

### 🔄 Fast & Slow Pointers (Floyd's Cycle)
**Keywords to Look For:**
- "cycle", "loop"
- "linked list"
- "find middle"
- "happy number"
- "circular array"
- "detect duplicate"

**Example Problems:**
- Linked List Cycle
- Find Middle of Linked List
- Happy Number

**When to Use:** Cycle detection problems or finding specific positions in sequences.

---

### 🗺️ HashMap/HashSet Pattern
**Keywords to Look For:**
- "frequency", "count", "occurrence"
- "anagram"
- "group", "categorize"
- "duplicate", "unique"
- "first/last occurrence"
- "sum equals target"
- "complement"

**Example Problems:**
- Two Sum
- Group Anagrams
- Valid Anagram
- Contains Duplicate

**When to Use:** Problems requiring quick lookups, counting elements, or grouping by properties.

---

### 📚 Stack Pattern
**Keywords to Look For:**
- "parentheses", "brackets", "balanced"
- "nested"
- "valid expression"
- "next greater/smaller"
- "monotonic"
- "temperature", "stock span"
- "undo", "history"

**Example Problems:**
- Valid Parentheses
- Daily Temperatures
- Next Greater Element

**When to Use:** Problems involving matching pairs, maintaining order, or finding next significant element.

---

### 🌳 Tree/Graph Traversal (DFS/BFS)
**Keywords to Look For:**
- "path", "route"
- "connected", "islands"
- "tree depth", "height"
- "level", "layer"
- "shortest path" (BFS)
- "all paths" (DFS)
- "ancestor", "descendant"
- "serialize", "deserialize"

**Example Problems:**
- Number of Islands
- Binary Tree Level Order Traversal
- Maximum Depth of Binary Tree

**When to Use:** Problems involving exploring all possibilities, finding paths, or level-wise processing.

---

### 🎯 Binary Search Pattern
**Keywords to Look For:**
- "sorted"
- "rotated sorted array"
- "find position", "search"
- "kth smallest/largest"
- "minimize maximum", "maximize minimum"
- "square root", "peak element"
- "search space is sorted"

**Example Problems:**
- Search in Rotated Sorted Array
- Find Peak Element
- Kth Smallest Element

**When to Use:** Problems with sorted data or when you need to find optimal value in a range.

---

### 💰 Dynamic Programming Pattern
**Keywords to Look For:**
- "maximum/minimum ways"
- "count paths", "unique paths"
- "optimal", "best"
- "longest increasing/decreasing"
- "partition", "split"
- "knapsack", "coins"
- "can reach", "can achieve"
- "memoization"
- "overlapping subproblems"

**Example Problems:**
- Climbing Stairs
- Longest Increasing Subsequence
- Coin Change
- House Robber

**When to Use:** Optimization problems with overlapping subproblems and optimal substructure.

---

### 🔄 Backtracking Pattern
**Keywords to Look For:**
- "all combinations", "all permutations"
- "all possible solutions"
- "generate all"
- "subsets", "power set"
- "n-queens", "sudoku"
- "path sum"
- "partition"

**Example Problems:**
- Subsets
- Permutations
- N-Queens
- Combination Sum

**When to Use:** Problems requiring exploration of all possible solutions with constraints.

---

### 🏔️ Heap/Priority Queue Pattern
**Keywords to Look For:**
- "kth largest/smallest"
- "top k frequent"
- "median"
- "schedule", "meeting rooms"
- "merge k sorted"
- "priority"
- "streaming data"

**Example Problems:**
- Kth Largest Element
- Top K Frequent Elements
- Find Median from Data Stream

**When to Use:** Problems requiring repeated extraction of min/max or maintaining top K elements.

---

### 🔗 Union Find (Disjoint Set) Pattern
**Keywords to Look For:**
- "connected components"
- "groups", "provinces"
- "friends", "network"
- "redundant connection"
- "accounts merge"
- "islands" (alternative to DFS/BFS)

**Example Problems:**
- Number of Provinces
- Redundant Connection
- Accounts Merge

**When to Use:** Problems about grouping elements or finding connected components.

---

### 🎭 Greedy Pattern
**Keywords to Look For:**
- "minimum/maximum number of"
- "earliest/latest"
- "optimal at each step"
- "interval", "meeting rooms"
- "jump game"
- "gas station"
- "assign", "distribute"

**Example Problems:**
- Jump Game
- Meeting Rooms
- Task Scheduler

**When to Use:** Problems where local optimal choices lead to global optimal solution.

---

## 🎓 Quick Recognition Tips

1. **Multiple Keywords:** Problems often combine patterns. "Find all unique triplets in a sorted array that sum to target" → Two Pointers + HashSet

2. **Data Structure Hints:**
   - Array problems → Two Pointers, Sliding Window, Binary Search
   - String problems → Sliding Window, HashMap, Two Pointers
   - Tree/Graph → DFS, BFS, Recursion
   - Optimization → DP, Greedy

3. **Constraint Clues:**
   - O(1) space → Usually Two Pointers or Bit Manipulation
   - O(log n) time → Binary Search or Divide & Conquer
   - Large constraints (n > 10^5) → Need O(n) or O(n log n) solution

4. **Action Words:**
   - "Find" → Search pattern (Binary Search, DFS/BFS)
   - "Count" → DP or HashMap
   - "Generate" → Backtracking
   - "Optimize" → DP or Greedy
   - "Validate" → Stack or simulation

## 📝 Practice Recognition

When you see a new problem:
1. Identify keywords from the problem statement
2. Match keywords to patterns above
3. Consider data structure mentioned
4. Look at constraints for optimization hints
5. Start with pattern-specific approach

Remember: Many problems can be solved with multiple patterns. Start with the most intuitive one based on keywords, then optimize if needed.