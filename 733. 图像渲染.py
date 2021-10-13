class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def dfs(image, sr, sc, newColor, old_color):
            if newColor == old_color:
                return
            if sr < 0 or sc < 0 or sr >= len(image) or sc >= len(image[0]) or image[sr][sc] != old_color:
                return
            image[sr][sc] = newColor
            dfs(image, sr - 1, sc, newColor, old_color)
            dfs(image, sr + 1, sc, newColor, old_color)
            dfs(image, sr, sc - 1, newColor, old_color)
            dfs(image, sr, sc + 1, newColor, old_color)

        dfs(image, sr, sc, newColor, image[sr][sc])
        return image