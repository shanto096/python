

word = "doonky"

with open('file.txt')as f:
    content = f.read()
    replaceContent = content.replace(word,'######')
with open("file.txt",'w')as f:
    f.write(replaceContent)