import sys
sys = sys.stdin.readline
n = int(input())
human_log = dict()
for _ in range(n):
    human, log = input().split()
    if(log == 'enter'):
        if(human not in human_log):
            human_log[human] = 1
    else:
        del human_log[human]

for name in sorted(human_log.keys(), reverse=True):
    print(name)
