import pyperclip as pc
print(pc.paste())

text = pc.paste()

lines = text.split('\n')

for i in range(len(lines)):
    if len(lines[i].strip(' ')) == 0:
        continue
    else:
     lines[i] = '* ' + lines[i]


text = '\n'.join(lines)
pc.copy(text)

print(pc.paste())


