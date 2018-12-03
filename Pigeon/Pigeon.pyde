from Model import Model
from Slider import Slider

global pigeon # Pigeon model
global scale_factor, theta # Coordinate variables
global switchMode # Switch between original model and smoothed model
global vexNum # Number of vertexes to display in vertex mode
global neighborNum, phi # Sliders indicating the maximum neighbors around a certain vertex and the strength of the smooth method

switchMode = True 
vexNum = 2000
theta = 0 # The Y rotation amount
scale_factor = 4

def setup():
    size(800,600,P3D)
    global pigeon, neighborNum, phi
    pigeon = Model("../pigeon.obj")
    neighborNum = Slider("Neighbors to detect : ", PVector(10, 30), PVector(5, 200))
    phi = Slider("Smoothing  strength : ", PVector(10, 70), PVector(0, 2), isInt = False)

def draw():
    background(0)
    showVariables()
    neighborNum.display()
    phi.display()
    
    global theta
    theta += 0.01
    
    # phi.setBlockLocation(phi.blockLoc.x + sin(theta*1.65))
    neighbor = neighborNum.getValue()
    strength = phi.getValue()
    pigeon.LaplaceSmoothing(neighbor, strength)
    
    showModel(pigeon.triShape) if switchMode else showModel(pigeon.shape)

"""
Processing Event Hendlers
"""
def mouseWheel(event):
    e = event.getCount()
    global scale_factor
    scale_factor += e * 0.8

def mouseDragged():
    if neighborNum.isHit(PVector(mouseX, mouseY)):
        neighborNum.setBlockLocation(mouseX)
    if phi.isHit(PVector(mouseX, mouseY)):
        phi.setBlockLocation(mouseX)
    
def keyPressed():
    global vexNum
    if keyCode == UP:
        vexNum += 3
    elif keyCode == DOWN:
        vexNum -= 3
    elif key == ' ':
        global switchMode
        switchMode = False if switchMode else True

"""
Functions 
"""
def showVertexes(vertexes):
    pushStyle(); pushMatrix()
    translate(width/2, height/2, 0)
    scale(scale_factor)
    stroke(255); strokeWeight(1)
    rotateX(PI)
    rotateY(theta)
    for v in vertexes[:vexNum]:
        point(v.x, v.y, v.z)
    popStyle(); popMatrix()    
        
def showModel(model):
    lights()
    translate(width/2, height/2, 0)
    scale(scale_factor)
    rotateX(PI)
    rotateY(theta)
    shape(model)
    
def showVariables():
    pushStyle()
    fill(255)
    data = str(pigeon)
    text(data, -23, 80)
    popStyle()
    
    
