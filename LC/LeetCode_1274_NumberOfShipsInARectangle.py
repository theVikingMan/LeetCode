
class Solution(object):
  def countShips(self, sea, topRight, bottomLeft):
    def findShips(topRight, bottomLeft):
      if topRight.x < bottomLeft.x or topRight.y < bottomLeft.y:
        return 0

      if not sea.hasShips(topRight, bottomLeft):
        return 0
      elif topRight.x == bottomLeft.x and topRight.y == bottomLeft.y:
        return int(sea.hasShips(topRight, bottomLeft))

      midX = (bottomLeft.x + topRight.x) // 2
      midY = (bottomLeft.y + topRight.y) // 2
      mid = Point(midX, midY)

      topLeftQ = findShips(Point(mid.x, topRight.y), Point(bottomLeft.x, mid.y + 1))
      topRightQ = findShips(topRight, Point(mid.x + 1, mid.y + 1))
      bottomLeftQ = findShips(Point(mid.x, mid.y), bottomLeft)
      bottomRightR = findShips(Point(topRight.x, mid.y), Point(mid.x + 1, bottomLeft.y))

      return topLeftQ + topRightQ + bottomLeftQ + bottomRightR

    return findShips(topRight, bottomLeft)

# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea(object):
#    def hasShips(self, topRight, bottomLeft):
#        """
#        :type topRight: Point
#		 :type bottomLeft: Point
#        :rtype bool
#        """
#
#class Point(object):
#	def __init__(self, x, y):
#		self.x = x
#		self.y = y