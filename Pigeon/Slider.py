class Slider:
    def __init__(self, name, loc, domain, isInt = True):
        self.name = name
        self.loc = loc
        self.low, self.high = domain.x, domain.y
        self.isInt = isInt
        self.blockLoc = PVector(loc.x, loc.y)
        self.blockSize = PVector(8, 12)
        self.lineLength = 130
        self.value = 0
    
    def setLocation(self, loc):
        self.loc = loc
    
    def setBlockLocation(self, x):
        self.blockLoc.x = x
    
    def Update(self):
        if self.blockLoc.x - self.blockSize.x/2 < self.loc.x:
            self.blockLoc.x = self.loc.x + self.blockSize.x/2
        if self.blockLoc.x > self.loc.x + self.lineLength - self.blockSize.x/2:
            self.blockLoc.x = self.loc.x + self.lineLength - self.blockSize.x/2
        remapBegin = self.loc.x + self.blockSize.x/2
        remapEnd = self.loc.x + self.lineLength - self.blockSize.x/2
        self.value = map(self.blockLoc.x, remapBegin, remapEnd, self.low, self.high)
        self.value = int(self.value) if self.isInt else round(self.value, 2)
        
    def setRange(self, low, high):
        self.low, self.high = low, high
    
    def getValue(self):
        return self.value
    
    def display(self):
        self.Update()
        pushStyle()
        pushMatrix()
        
        fill(255)
        name = self.name + str(self.value)
        text(name, self.loc.x, self.loc.y - 15)
        stroke(255); strokeWeight(1)
        line(self.loc.x, self.loc.y, self.loc.x + self.lineLength, self.loc.y) 
        stroke(100,100,255); strokeWeight(1);fill(255)
        rectMode(CENTER)
        rect(self.blockLoc.x, self.blockLoc.y, self.blockSize.x, self.blockSize.y)
        
        popMatrix()
        popStyle()
        
    
    def isHit(self, mouse):
        yLow, xLow = self.loc.y - self.blockSize.y/2 - 15, self.loc.x
        yHigh, xHigh = self.loc.y + self.blockSize.y/2 + 15, self.loc.x + self.lineLength
        isYInRange = True if mouse.y > yLow and mouse.y < yHigh else False
        isXInRange = True if mouse.x > xLow and mouse.x < xHigh else False
        result = isXInRange and isYInRange 
        # print("Received Click: ({}, {})\nRangeY : ({} - {})\nRangeX : ({} - {})\nClicked?{}\n\n".format(mouse.x, mouse.y, yLow, yHigh, xLow, xHigh, result))
        return  result
    
    
        
        
    
    
