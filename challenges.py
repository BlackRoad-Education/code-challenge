#!/usr/bin/env python3
"""BlackRoad Code Challenges — competitive programming meets education"""
CHALLENGES = [
  {"id":1,"title":"Two Sum","difficulty":"easy","desc":"Find two numbers that add to target",
   "fn":"def two_sum(nums, target):\n    pass",
   "tests":[([2,7,11,15],9,[0,1]),([3,2,4],6,[1,2])]},
  {"id":2,"title":"Palindrome Check","difficulty":"easy","desc":"Check if string is a palindrome",
   "fn":"def is_palindrome(s):\n    pass",
   "tests":[("racecar",True),("hello",False),("",True)]},
  {"id":3,"title":"FizzBuzz","difficulty":"easy","desc":"Classic FizzBuzz",
   "fn":"def fizzbuzz(n):\n    pass",
   "tests":[(15,"FizzBuzz"),(3,"Fizz"),(5,"Buzz"),(7,"7")]},
  {"id":4,"title":"Fibonacci","difficulty":"medium","desc":"Return nth Fibonacci number",
   "fn":"def fib(n):\n    pass",
   "tests":[(0,0),(1,1),(10,55),(20,6765)]},
  {"id":5,"title":"Binary Search","difficulty":"medium","desc":"Find target in sorted array",
   "fn":"def binary_search(arr, target):\n    pass",
   "tests":[([1,3,5,7,9],5,2),([1,3,5,7,9],4,-1)]},
  {"id":6,"title":"Reverse Linked List","difficulty":"medium","desc":"Reverse a singly linked list",
   "fn":"def reverse_list(head):\n    pass",
   "tests":[]},
  {"id":7,"title":"Valid Parentheses","difficulty":"medium","desc":"Check if brackets are balanced",
   "fn":"def is_valid(s):\n    pass",
   "tests":[("()",True),("()[]{}",True),("(]",False),("([)]",False)]},
  {"id":8,"title":"Merge Sort","difficulty":"hard","desc":"Implement merge sort",
   "fn":"def merge_sort(arr):\n    pass",
   "tests":[([3,1,4,1,5],[1,1,3,4,5]),([],[])]},
  {"id":9,"title":"LRU Cache","difficulty":"hard","desc":"Implement least recently used cache",
   "fn":"class LRUCache:\n    def __init__(self, cap): pass\n    def get(self, key): pass\n    def put(self, key, val): pass",
   "tests":[]},
  {"id":10,"title":"Amundson Sequence","difficulty":"hard","desc":"Compute G(n) = n^(n+1)/(n+1)^n for large n",
   "fn":"def amundson_g(n):\n    pass  # Should converge to 1/e",
   "tests":[(1,0.5),(10,0.385543),(100,0.369024)]},
]

def list_challenges():
    for c in CHALLENGES:
        print(f"  #{c['id']:2d} [{c['difficulty']:6s}] {c['title']}")

def show(cid):
    c = next((x for x in CHALLENGES if x["id"] == cid), None)
    if not c: print("Not found"); return
    print(f"\n# {c['title']} ({c['difficulty']})\n{c['desc']}\n\n{c['fn']}\n")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2 or sys.argv[1] == "list": list_challenges()
    elif sys.argv[1] == "show": show(int(sys.argv[2]))
    else: print("Usage: challenges.py [list|show N]")
