import time, subprocess
a1 = '''
---sssssssSSS0
'''
a2 = '''
   ---sssssssSSS0
'''
a3 = '''
    ---sssssssSSS0
'''
a4 = '''
         ---sssssssSSS0
'''
while True:
    print(a1), time.sleep(1), subprocess.run('clear')
    print(a2), time.sleep(1), subprocess.run('clear')
    print(a3), time.sleep(1), subprocess.run('clear')
    print(a4), time.sleep(1), subprocess.run('clear')