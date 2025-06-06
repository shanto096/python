with open('./chapter_9/file.txt')as f:
    content=f.read()
    if('python' in content):
        count = content.count('python')
        print(f'acha : {count}')
    else:
        print('nai')
