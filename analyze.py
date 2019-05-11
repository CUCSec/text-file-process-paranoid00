
find = open('log_files/201811123027.log',encoding='utf8')
count = 0
for line in find:
    str = line.split(',')[1].split('：')[1]
    
    if str == '201811123027':
        count=count+1
print(count)
    
    

