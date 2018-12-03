class Model:
    def __init__(self, dir):
        self.smoothedMap = {}
        self.dir = dir
        self.shape = loadShape(dir)
        self.vertexes, self.reducedVertexes = self.getVertexes(self.shape)
        self.tessShape = self.shape.getTessellation()
        self.triShape = self.getTriShape()
        self.distMap = self.getDistance(self.reducedVertexes)
        self.history = {}
        

    def __repr__(self):
        return """
        Model directory :   {}
        # of Shape Vertex :    {}
        # of tessShape Vertex :   {}
        # of triShape Vertex :   {}
        # of Vertexes :    {}""".format(self.dir, self.shape.getVertexCount(), self.tessShape.getVertexCount(), self.triShape.getVertexCount(), len(self.reducedVertexes))

    def getTriShape(self):
        result = createShape();
        result.beginShape(TRIANGLES)
        # result.noStroke()
        for i in range(len(self.vertexes)):
            if i%3 == 0:
                p1 = self.vertexes[i]
                p2 = self.vertexes[i+1]
                p3 = self.vertexes[i+2]
                for p in [p1,p2,p3]:
                    smoothed_p = self.smoothedMap[str(p)]
                    result.vertex(smoothed_p.x, smoothed_p.y, smoothed_p.z)
        result.endShape()
        return result
    
    def getVertexes(self, original):
        vertexes = []
        reducedVertexes = []
        for i in range(0, original.getChildCount()):
            if original.getChild(i).getVertexCount() == 3:
                for j in range(original.getChild(i).getVertexCount()):
                    p = original.getChild(i).getVertex(j)
                    vertexes.append(PVector(p.x,p.y,p.z))
                    if p not in reducedVertexes:
                         reducedVertexes.append(p)
                         self.smoothedMap[str(p)] = p
        return vertexes, reducedVertexes
                    
    def getDistance(self, vertexes):
        result = {}
        for i in range(len(vertexes)):
            result[i] = list()
        for i in range(len(vertexes) - 1):
            for j in range(i + 1, len(vertexes)):
                distance = round(PVector.dist(vertexes[i], vertexes[j]), 2)
                if distance > 0:
                    result[i].append([distance, vertexes[j]])
                    result[j].append([distance, vertexes[i]])
        for i in range(len(vertexes)):
            result[i].sort()
        return result

    def LaplaceSmoothing(self, k, phi):
        """
        Found a vertex's k nearest neighbors and update the vertex using laplace smoothing methods
        """
        if str([k, phi]) in self.history:
            self.triShape = self.history[str([k,phi])]
        
        else:
            weight = 1.0/k * phi if k != 0 else 0
            for i in range(len(self.reducedVertexes)):
                neighbors = [n[1] for n in self.distMap[i][0:k]]
                v = self.reducedVertexes[i]
                delta = PVector(0,0,0)
                for n in neighbors:
                    diff = PVector(n.x - v.x, n.y - v.y, n.z - v.z)
                    delta.add(diff.mult(weight))
                new_v = PVector(v.x + delta.x, v.y + delta.y, v.z + delta.z)
                self.smoothedMap[str(v)] = new_v
            self.triShape = self.getTriShape()
            self.history[str([k,phi])] = self.triShape

        
            
    
            
            
    
    
    
    
    
        
