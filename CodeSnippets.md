Tasks made simple with minimal code snippets. Some of them might be useful for coding challenges:

1. Check balanced Brackets

        import re
        s=re.sub(r'[^\[\]\(\)]','',input())
        p=''
        while not s==p:p=re.sub(r'\[\]|\(\)','',s);s=p
        print(str(s==''))
