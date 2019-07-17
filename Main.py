Descr = ["entrance","A room"]
RoutDescr = ["N","E","S","W"]
tilenumber = 0

class Tile(object):
	name =""
	descri = ""
	
	exit = [None,None,None,None]
	exitnum = 1
	path= 0
	_id = ""
	
	
	def __init__(self, roomType, connections, Path,num):
		global tilenumber
		self.exits = connections
		self.path = Path
		self_id = num
		if roomType == 0:
			self.descri = Descr[roomType]
			self.name = "E" + self.name + str(self._id)
			#expansion required for this part
		elif roomType == 1:
			self.descri = Descr[roomType]
			self.name = C + self.name + str(self._id)
		
		print ("New Tile created")
		
	def ConnectTile(self, Prevtile, location):
	    self.exit[location] = Prevtile
	    return True
		
class Dungeon(object):	
	
    entrance = object

    def Traversal(self, currTile):
        names=""
        i= 0
        if type(currTile) is Tile:
            while i < 4:
                if type(currTile.exit) is Tile:
                    names = names + " "+ currTile.exit[i].name + " "
                else:
                    names = names + " NA "
                i = i+1 
            print("Room "+ currTile.name + ":Connections= "  + names )    
            i =0
            while i < 4:
                if type(currTile.exit[i]) is Tile and type(currTile.exit[i]) is not None:
                    print("digging in to " + currTile.exit[i].name)
                    self.Traversal(currTile.exit[i])
                else:
                    print("")
                i = i+1
                if i > 5:
                    break
                
    def GenerateDungeon(self,currTile,prevTile):
        global tilenumber
        print("Potato 0: test location reached")
        connection = [None,None,None, None]

        #####
        #start the Recursive algorithim from the entrance tile object and move 
        #through creating a tile attach at the correct locations, first as a stack then as a binary tree.
        #####
        if type(self.entrance) is Tile and tilenumber < 10:#Recursive loop
            print("Potato 0.1.9 type check: " + str(type(currTile)) + "|" + str(type(prevTile)))
            if prevTile is Tile  and currTile is Tile:  #for binary tree algorithim 
                print ("Potato 0.3 : new tile to generate New tile number" + str(tilenumber) + " || " + prevTile.name +" | "+ currTile.name)
                
            if type(currTile) is Tile:    #first line
                print ("potato0.2: adding a new tile to game. New tile number" + str(tilenumber))
                newTile = self.CreateNewTile(currTile,1)
                self.GenerateDungeon(newTile, currTile)
                
        if tilenumber > 10:
            print("Finished First Generation")
        
        
        #intial Creation
        if type(self.entrance) is not Tile and currTile == None:	
            print ("Potato 0.1: start Generation")
            self.entrance = Tile(0, [None,None,None,None],0,0 )
            tilenumber = tilenumber + 1
            self.GenerateDungeon(self.entrance,None)
            print(type(self.entrance))
            
    def __init__(self):
        self.GenerateDungeon(None, None)
        
    # generate a new tile to connect to the tile that came before it
    def CreateNewTile(self, connectedTile, location):
        global tilenumber
        NewTile = Tile(0,[None,None,None,None], connectedTile.path,tilenumber)
        tilenumber= tilenumber +1
        
        if NewTile.ConnectTile(connectedTile, location):
            print("Connected")
        else:
            print("Failed")
        return NewTile
    
    
    
    
class GameLoop(object):
    dungeon = object()
    def __init__(self):
        print ("Start")
        dungeon = Dungeon()
        dungeon.Traversal(dungeon.entrance)
        
gameLoop = GameLoop()
