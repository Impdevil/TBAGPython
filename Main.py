
tilenumber = 0
MaxTileDepth = 40

class Tile(object):
	name =""
	descri = ""
	
	exits = [None,None,None,None]
	exitnum = 1
	path= 0
	_id = ""
	Descr = ["entrance","A room"]
	RoutDescr = ["N","E","S","W"]
	
	def __init__(self, roomType, connections, Path,num):
		global tilenumber
		self.exits = connections
		self.path = Path
		self._id = num
		if roomType == 0:
			self.descri = self.Descr[roomType]
			self.name = "E" + self.name + str(self._id)
			#expansion required for this part
		elif roomType == 1:
			self.descri = self.Descr[roomType]
			self.name = "C" + self.name + str(self._id)
		
		print ("New Tile created")
		
	def ConnectTile(self, Prevtile, location, establised):
	    print("potato 4 connections: "+Prevtile.name + " ==> " + self.name + " @ " + str(location))
	    self.exits[location] = Prevtile
	    if establised != True:
	        if location >= 2:
	            Prevtile.ConnectTile(self,max(0,min(location-2, 4)),True)
	        elif location < 2:
	            Prevtile.ConnectTile(self,max(0,min(location+2, 4)),True)
	    return True
		
class Dungeon(object):	
	
    entrance = object

    def Traversal(self,currTile,j, prevTile):
        
        names=""
        i= 0
        if j < 40:
            if type(currTile) is Tile:
                while i < 4:
                    if type(currTile.exits[i]) is Tile:
                        names = names + " "+ currTile.exits[i].name + " "
                    else:
                        names = names + " NA "
                    i = i+1 
                print("Room "+ currTile.name + ":Connections= "  + names )    
                i =0
                while i < 4:
                    if currTile.exits[i] != None and currTile.exits[i].name != None:
                        #print("potato 4: Traversal data currtile" + str(type(currTile)) +", "+ currTile.name+ "| next tile " + str(type(currTile.exits[i])) +", "+ currTile.exits[i].name)
                        if type(currTile.exits[i]) is Tile and type(currTile.exits[i]) is not None:
                            if prevTile is None: 
                                print("digging in to " + currTile.exits[i].name + " from " + currTile.name)
                                j=j+1
                                self.Traversal(currTile.exits[i], j , currTile)
                            elif currTile.exits[i] != prevTile:
                                print("digging in to " + currTile.exits[i].name + " from " + currTile.name)
                                j=j+1
                                self.Traversal(currTile.exits[i], j , currTile)
                            else:
                                print( currTile.name + " empty @ " + str(i))
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
            if type(prevTile) is Tile  and type(currTile) is Tile:  #for binary tree algorithim 
                print ("Potato 0.3 : new tile to generate New tile number" + str(tilenumber) + " || " + prevTile.name +" | "+ currTile.name)
                if tilenumber == 3:
                    newTile = self.CreateNewTile(currTile,0)
                    print("offshoot of main line at " + str(tilenumber))
                else:
                        newTile = self.CreateNewTile(currTile,3)
                self.GenerateDungeon(newTile,currTile)
                
            elif type(currTile) is Tile:    #first line
                newTile = self.CreateNewTile(currTile,3)
                print ("potato0.2: adding a new tile to game. New tile number" + str(tilenumber) +" named: " + newTile.name)
                self.GenerateDungeon(newTile, currTile)
                
        if tilenumber > 10:
            print("Finished First Generation")
        
        #intial Creation
        if type(self.entrance) is not Tile and currTile == None:	
            print ("Potato 0.1: start Generation")
            self.entrance = Tile(0, [None,None,None,None],0,0 )
            tilenumber = tilenumber + 1
            print ("potato0.2: adding a new tile to game. New tile number" + str(tilenumber) +" named: " + self.entrance.name)
            self.GenerateDungeon(self.entrance,None)
            print(type(self.entrance))
            
    def __init__(self):
        self.GenerateDungeon(None, None)
        
    # generate a new tile to connect to the tile that came before it
    def CreateNewTile(self, connectedTile, location):
        global tilenumber
        NewTile = Tile(1,[None,None,None,None], connectedTile.path,tilenumber)
        
        tilenumber= tilenumber +1
        
        if NewTile.ConnectTile(connectedTile, location, False):
            print("Connected")
        else:
            print("Failed")
        return NewTile
    
    
    
    
class GameLoop(object):
    dungeon = object()
    def __init__(self):
        print ("Start")
        dungeon = Dungeon()
        dungeon.Traversal(dungeon.entrance,0, None)
        
gameLoop = GameLoop()
