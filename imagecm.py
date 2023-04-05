from PIL import Image, ImageDraw
import numpy as np
from random import randint, choice
import operator

class I3d:
    im: Image
    
    def __init__(self, im: Image):
        self.im = im
    
    def left(self, k):
        for i in range(self.im.size[0] - k):
            for j in range(self.im.size[1]):
                x = tuple((np.array(self.im.getpixel((i, j))) + np.array(self.im.getpixel((i + k, j))) // 2))
                self.im.putpixel([i, j], x)
        return self

    def right(self, k):
        for i in reversed(range(k, self.im.size[0])):
            for j in range(self.im.size[1]):
                x = tuple((np.array(self.im.getpixel((i, j))) + np.array(self.im.getpixel((i - k, j))) // 2))
                self.im.putpixel([i, j], x)
        return self

    def up(self, k):
        for i in range(self.im.size[0]):
            for j in range(self.im.size[1] - k):
                x = tuple((np.array(self.im.getpixel((i, j))) + np.array(self.im.getpixel((i, j + k))) // 2))
                self.im.putpixel([i, j], x)
        return self

    def down(self, k):
        for i in range(self.im.size[0]):
            for j in reversed(range(k, self.im.size[1])):
                x = tuple((np.array(self.im.getpixel((i, j))) + np.array(self.im.getpixel((i, j - k))) // 2))
                self.im.putpixel([i, j], x)
        return self
    
    def show(self):
        self.im.show()
    
    def save(self, path):
        self.im.save(path)

def bright(im: Image, bright):
    width, height = im.size;
    for x in range(width):
        for y in range(height):
            r, g, b = im.getpixel((x, y));
            im.putpixel((x, y), (int(r * bright * 0.01), int(g * bright * 0.01),
            int(b * bright * 0.01)));
    return im

def network(w: int, h: int, c: int):
    im = Image.new('RGB', (w, h), 'white');
    draw = ImageDraw.Draw(im);
    dots = []

    for i in range(c):
        dots.append((randint(0, w), randint(0, h)));

    for i in dots:
        for j in dots:
            if i != j:
                draw.line((i[0], i[1], j[0], j[1]), fill = 'black', width = 1);

    return im

def rainbow_network(w: int, h: int, c: int):
    colors = ['black', 'red', 'orange', 'yellow', 'green', 'blue', 'violet']
    im = Image.new('RGB', (w, h), 'white')
    draw = ImageDraw.Draw(im)
    dots = []

    for i in range(c):
        dots.append((randint(0, w), randint(0, h)))

    for i in dots:
        for j in dots:
            if i != j:
                draw.line((i[0], i[1], j[0], j[1]), fill = choice(colors), width = 1)

    return im

def noise(w, h):
    im = Image.new('RGB', (w, h), 'white')
    
    for i1 in range(w):
        for i2 in range(h):
            im.putpixel((i1,i2), (randint(0, 255), randint(0, 255), randint(0, 255)))
    
    return im

def gray_noise(w, h):
    im = Image.new('RGB', (w, h), 'white')
    for i1 in range(w):
        for i2 in range(h):
            c = randint(0, 255)
            im.putpixel((i1,i2), (c, c, c))
    
    return im

def tree(w, h):
    im = Image.new(size = (w, h), mode = "RGB", color = "white")
    dw = ImageDraw.Draw(im)

    m1 = [(randint(1, w), randint(1, h))]
    
    o = [[0, 5], [-5, 0], [-5, 5], [5, 0], [5, 5], [0, -5], [-5, -5], [5, -5]]
    while m1 != []:
        m2 = []
        for j in m1:
            try:
                for k in range(2):
                    st = False
                    o_ = []
                    while st == False:
                        ti = choice(o)
                        o_.append(ti)
                        if [i in o for i in o_] == [True] * 8:
                            break
                        
                        if True not in [j[l] + ti[l] < 0 for l in range(2)]:
                            m3 = []
                            for m in range(2):
                                if ti[m] == -5: m3.append([j[m] - l for l in range(1, 6)])
                                if ti[m] == 5: m3.append([j[m] + l for l in range(1, 6)])
                                if ti[m] == 0: m3.append([j[m]] * 5)

                            for l in range(5):
                                if (im.getpixel((m3[0][l], m3[1][l])) != (255, 255, 255) or
                                   im.getpixel((m3[0][l], m3[1][l] + 1)) == (0, 0, 0)):
                                    n = False
                                    break
                                else:
                                    n = True

                            if n == True:
                                dw.line((j, (m3[0][-1], m3[1][-1])), fill = 0)
                                m2.append((m3[0][-1], m3[1][-1]))
                                st = True

            except Exception as e:
                continue

        m1 = m2.copy()

    return im

def get_grid(w, h, s):
    a = [[[i, j] for j in range(100, 100 + w * s + 1, s)] for i in range(100, 100 + h * s + 1, s)]
    
    im = Image.new(size = (a[-1][-1][0] + 100, a[-1][-1][1] + 100), mode = 'RGB', color = 'white')
    dw = ImageDraw.Draw(im)
    
    for i in range(h + 1):
        dy = randint(-10, 10)
        for j in range(w + 1):
            a[i][j][1] += dy
            
    for i in range(w + 1):
        dx = randint(-2, 2)
        for j in range(h + 1):
            a[i][j][0] += randint(-2, 2)
    
    x = eval(str(a).replace('[', '(').replace(']', ')'))
    
    for i in range(len(x)):
        dw.line(xy = [j for j in x[i]], fill = 'black')
    for i in range(len(x[0])):
        dw.line(xy = [j[i] for j in x], fill = 'black')
            
    return im