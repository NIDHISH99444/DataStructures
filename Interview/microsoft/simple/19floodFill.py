def fill(image,sr,sc,newColor,old):
    if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]) or image[sr][sc] == newColor or image[sr][sc] != old:
        return

    image[sr][sc] = newColor
    fill(image, sr - 1, sc, newColor, old)
    fill(image, sr, sc + 1, newColor, old)
    fill(image, sr + 1, sc, newColor, old)
    fill(image, sr, sc - 1, newColor, old)

def floodfill(image, sr, sc, newColor):
    if image[sr][sc] == newColor:
        return image
    old = image[sr][sc]
    fill(image, sr, sc, newColor, old)
    return image


image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr = 1
sc = 1
newColor = 2
print(floodfill(image,sr,sc,newColor))