from PIL import Image, ImageColor

cat = Image.new('RGBA', (100, 100))

a = [(0,0,0,255)]*100
a[49] = (555,0,0,255)
a[25] = (255,255,0,255)
a[75] = (25, 0, 122,255)
a[95] = (0,255,0,255)
a[4] = (0,0,255,255)


rows = [a]

def rule(i, j):
    neighbors = rows[i][j-1:j+2]
    red = sum(n[0] for n in neighbors)/3 + 2*i -j
    green = sum(n[1] for n in neighbors)/2.99 * i/j
    blue = sum(n[2] for n in neighbors)/2.99 + +j/(i+1)
    alpha = sum(n[3] for n in neighbors)/2.99
    return (int(red),int(green),int(blue),255)

for i in range(1,100):
    new_row = [(0,0,0,255)]*100
    for j in range(1,99):
        new_row[j] = rule(i-1, j)
    rows.append(new_row)
    
for x in range(100):
    for y in range(100):
        cat.putpixel((x, y), rows[y][x])
        
    
cat.save('pic.png')
