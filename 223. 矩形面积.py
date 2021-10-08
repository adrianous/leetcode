class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        in_area_x1 = max(ax1, bx1)
        in_area_y1 = max(ay1, by1)
        in_area_x2 = min(ax2, bx2)
        in_area_y2 = min(ay2, by2)
        in_area_size = 0
        if in_area_x2 > in_area_x1 and in_area_y2 > in_area_y1:
            in_area_size = (in_area_y2 - in_area_y1) * (in_area_x2 - in_area_x1)

        area_a = (ax2-ax1)*(ay2-ay1)
        area_b = (bx2-bx1)*(by2-by1)
        return area_a + area_b - in_area_size