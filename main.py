mode = input('Which fysc mode? normal (n) or pygame (p) mode? ')
if mode == 'n':
    with open("FYSCv1.2.py", "r") as f:
        code = f.read()
    exec(code)
if mode == 'p':
    print('pygame mode not available now.')
