import re

def assembler_interpreter(inp):
    
    d,i,stack = dict(),0,re.sub('\n{2,}','\n',inp).split('\n')[1:-1]
    
    while i<len(stack):
        func,var,val = map(lambda s: s.replace(',',''),(stack[i].lstrip(' ')+' _ _').split()[:3])
        
        if func == 'mov':      d[var] = d.get(val) if val.isalpha() else int(val)        
        elif func == 'dec':    d[var]-=1   
        elif func == 'inc':    d[var]+=1
        elif func == 'sub':    d[var]-=int(val) if not val.isalpha() else d[val]
        elif func == 'add':    d[var]+=int(val) if not val.isalpha() else d[val]
        elif func == 'mul':    d[var]*=int(val) if not val.isalpha() else d[val]
        elif func == 'div':    d[var]//=int(val) if not val.isalpha() else d[val]

        elif func == 'jmp':
            if stack[i][0]!=' ': idx = i
            i=stack.index(var+':')
        elif func == 'cmp':
            a,b = d[var] if var in d else int(var),d[val] if val in d else int(val)
        elif func == 'jne':
            if a!=b:
                if stack[i][0]!=' ': idx = i
                i = stack.index(var+':')
        elif func == 'je':
            if a==b:
                if stack[i][0]!=' ': idx = i
                i = stack.index(var+':')
        elif func == 'jg':
            if a>b:
                if stack[i][0]!=' ': idx = i
                i = stack.index(var+':')
        elif func == 'jge':
            if a>=b:
                if stack[i][0]!=' ': idx = i
                i = stack.index(var+':')
        elif func == 'jl':
            if a<b:
                if stack[i][0]!=' ': idx = i
                i = stack.index(var+':')
        elif func == 'jle':
            if a<=b:
                if stack[i][0]!=' ': idx = i
                i = stack.index(var+':')
        elif func == 'call':
            if stack[i][0]!=' ': idx = i
            i = stack.index(var+':')
        elif func == 'ret':
            try:    i=idx; del idx
            except: pass
        elif func == 'msg':
            msg = (eval(j) if j[0]=='\'' else str(d.get(j,'')) for j in re.findall(r'\'[^\']*\'|.',re.sub(r';.*$','',stack[i][4:])))
        elif func == 'end':    i = ''; break           
        i+=1
     
    return ''.join(msg) if i=='' else -1
