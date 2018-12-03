global pigeon, pigeonTess, triShape, quadShape, scale_factor
scale_factor = 2
def setup():
    size(800,600,P3D)
    global pigeon, pigeonTess, triShape, quadShape
    pigeon = loadShape("../pigeon.obj")
    print(pigeon)
    pigeon.setFill(255)
    pigeonTess = pigeon.getTessellation()
    triShape = getTriShape(pigeon)
    # Make a PShape with the all the faces with three verticcreateShapeTri(pigeon)geon.GetTriShape()
    print("pigeon vertex count: {}\ntriShape vertex count: {}\npigeonTess vertex count: {}".format(pigeon.getVertexCount(), triShape.getVertexCount(), pigeonTess.getVertexCount()))
    # Make a PShape with the all the faces with four vertices
    # quadShape = createShapeQuad(objShape);
    
def draw():
    background(0)
    lights()
    translate(width/2, height/2, 0)
    scale(scale_factor)
    rotateX(PI)
    # pigeon.rotateY(.01)
    # shape(pigeon)
    triShape.rotateY(.01)
    shape(triShape)
    # pigeonTess.rotateY(.01)
    # shape(pigeonTess)
    
def getTriShape(r):
    s = createShape();
    s.beginShape(TRIANGLES)
    # s.noStroke()
    for i in range(0, r.getChildCount()):
        if r.getChild(i).getVertexCount() >= 3 :
            for j in range(r.getChild(i).getVertexCount()):
                p = r.getChild(i).getVertex(j)
                n = r.getChild(i).getNormal(j)
                u = r.getChild(i).getTextureU(j)
                v = r.getChild(i).getTextureV(j)
                s.normal(n.x, n.y, n.z)
                s.vertex(p.x, p.y, p.z, u, v)
    s.endShape()
    return s

def mouseWheel(event):
    e = event.getCount()
    global scale_factor
    scale_factor += e * 0.8
    
    
    
    
    
