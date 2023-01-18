import random
 
<<<<<<< HEAD
width = 150
height = 150

 
node = {
    'wallCountdown': 25000,
    'padding': 4,
=======
width = 64
height = 64

 
node = {
    'wallCountdown': 3600,
    'padding': 2,
>>>>>>> 8b87b22 (six months of work)
    'x': int( width / 2 ),
    'y': int( height / 2 )
}
 
def getLevelRow():
    return ['#'] * width
 
level = [getLevelRow() for _ in range(height)]
 
while node['wallCountdown'] >= 0:
    x = node['x']
    y = node['y']
    
    if level[y][x] == '#':
        level[y][x] = ' '
        level[y+1][x] = ' ' #above
        level[y-1][x] = ' ' #below
        level[y][x-1] = ' ' #left
        level[y][x+1] = ' ' #right
        level[y-1][x-1] = ' ' #topleft
        level[y-1][x+1] = ' ' #topright
        level[y+1][x-1] = ' ' #bottomleft
        level[y+1][x+1] = ' ' #bottomright
        node['wallCountdown'] -= 9
    
    roll = random.randint(1, 4)
    
    if roll == 1 and x > node['padding']:
        node['x'] -= 1
    
    if roll == 2 and x < width - 1 - node['padding']:
        node['x'] += 1
    
    if roll == 3 and y > node['padding']:
        node['y'] -= 1
    
    if roll == 4 and y < height - 1 - node['padding']:
        node['y'] += 1
 
for row in level:
    print( ''.join(row) )

input("DONE!")
