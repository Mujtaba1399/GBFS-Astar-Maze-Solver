"""
positions:

    0		2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19
    20	21	22	23	24	25	26	27	28	29	30	31	32	33	34	35	36	37	38	39
    40	41	42	43	44	45	46	47	48	49	50	51	52	53	54	55	56	57	58	59
    60	61	62	63	64	65	66	67	68	69	70	71	72	73	74	75	76	77	78	79
    80	81	82	83	84	85	86	87	88	89	90	91	92	93	94	95	96	97	98	99
    100	101	102	103	104	105	106	107	108	109	110	111	112	113	114	115	116	117	118	119
    120	121	122	123	124	125	126	127	128	129	130	131	132	133	134	135	136	137	138	139
    140	141	142	143	144	145	146	147	148	149	150	151	152	153	154	155	156	157	158	159
    160	161	162	163	164	165	166	167	168	169	170	171	172	173	174	175	176	177	178	179
    180	181	182	183	184	185	186	187	188	189	190	191	192	193	194	195	196	197	198	199
    200	201	202	203	204	205	206	207	208	209	210	211	212	213	214	215	216	217	218	219
    220	221	222	223	224	225	226	227	228	229	230	231	232	233	234	235	236	237	238	239
    240	241	242	243	244	245	246	247	248	249	250	251	252	253	254	255	256	257	258	259
    260	261	262	263	264	265	266	267	268	269	270	271	272	273	274	275	276	277	278	279
    280	281	282	283	284	285	286	287	288	289	290	291	292	293	294	295	296	297	298	299
    300	301	302	303	304	305	306	307	308	309	310	311	312	313	314	315	316	317	318	319
    320	321	322	323	324	325	326	327	328	329	330	331	332	333	334	335	336	337	338	339
    340	341	342	343	344	345	346	347	348	349	350	351	352	353	354	355	356	357	358	359
    360	361	362	363	364	365	366	367	368	369	370	371	372	373	374	375	376	377	378	379
    380	381	382	383	384	385	386	387	388	389	390	391	392	393	394	395	396	397	398	399

    initial state  : root_node
    sucessor state : new_node
    goal test : node.position==goal
    path steps : cost
    searching steps : moves 

"""
size = 20
goal = 259
start = 280
maze = [
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,
            0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,1,0,0,
            0,0,1,0,0,0,0,0,0,0,1,1,1,1,0,0,0,1,1,1,
            0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,1,0,1,
            0,0,1,1,1,1,0,0,0,0,1,0,0,1,1,1,1,1,0,1,
            0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1,
            0,0,0,1,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,1,
            0,0,0,1,0,1,1,1,1,0,1,0,0,0,0,0,1,1,1,1,
            0,0,1,1,0,1,0,0,1,0,1,1,1,1,1,0,1,0,0,0,
            0,0,1,0,1,1,0,0,1,0,0,0,0,0,1,0,1,1,1,1,
            0,0,1,0,1,1,1,0,1,0,0,0,0,0,1,0,1,0,0,0,
            1,1,1,1,0,0,1,0,1,0,0,0,0,0,1,0,0,0,1,1,
            0,0,1,0,0,0,1,0,1,0,0,0,0,0,1,1,1,1,1,0,
            0,0,1,1,1,1,1,0,1,0,0,0,0,0,1,0,0,1,0,0,
            0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        ]

def getRow(temp):
    return int(temp/20)

def getColumn(temp):
    return temp%20

def heuristics(temp):
    count = 0
    tempRow = getRow(temp)
    tempCol = getColumn(temp)
    while(tempRow > getRow(goal)):
        count = count +1
        tempRow = tempRow -1
    while(tempRow < getRow(goal)):
        count = count +1
        tempRow = tempRow +1
    while(tempCol < getColumn(goal)):
        count = count +1
        tempCol = tempCol +1
    return count

def move_up(pos):
    if (maze[pos-20]==0):
        return False
    return pos-20

def move_down(pos):
    if (maze[pos+20]==0):
        return False
    return pos+20

def move_right(pos):
    if ( getColumn(pos) >19):
        return False
    elif(maze[pos+1]==0):
        return False
    return pos+1

def move_left(pos):
    if( getColumn(pos) < 0):
        return False
    if(maze[pos-1]==0):
        return False
    return pos-1













#--------------------------------------------------------------------------------------------------------------
# A Star algorithm

class NodeAstar:
    def __init__(self , position , cost , g , h ,f):
        self.position = position
        self.cost = cost
        self.g = g
        self.h = h
        self.f = f
    def __lt__(self, other):
        return self.f < other.f
    def __eq__(self, other):
        return self.position == other.position

def createNodeAstar(position , cost , g , h , f):
        return NodeAstar(position , cost , g , h , f) 

def get_NeighborsAstar(node ):
    neigbors_list = []
    if(move_up(node.position)):
        new_Node = createNodeAstar(move_up(node.position) , node.cost+1 , node.g , node.h , node.f)
        neigbors_list.append(new_Node)
    if(move_left(node.position)):
        new_Node = createNodeAstar(move_left(node.position) , node.cost+1 , node.g , node.h , node.f)
        neigbors_list.append(new_Node)
    if(move_right(node.position)):
        new_Node = createNodeAstar(move_right(node.position) , node.cost+1 , node.g , node.h , node.f)
        neigbors_list.append(new_Node)
    if(move_down(node.position)):
        new_Node = createNodeAstar(move_down(node.position) , node.cost+1 , node.g , node.h , node.f)
        neigbors_list.append(new_Node)
    return neigbors_list 
    
def check_currentAstar( open , current_neigbor):
    for node in open:
        if (node==current_neigbor and current_neigbor.f >= node.f):
            return False
    return True

def A_Star(node , moves):
    open = []
    closed = []

    open.append(node)
    open_lenght = len(open)

    while( open_lenght > 0 ):
        open.sort()
        current_Node = open.pop(0)
        closed.append(current_Node)
        
        if(current_Node.position == goal):
            print("A_star Algorithm\n\tPath cost :" + str(current_Node.cost) + "\n\tMoves :" + str(moves) )
            return True
        
        neigbors = get_NeighborsAstar(current_Node )

        for current_neigbor in neigbors:
            if current_neigbor in closed:
                continue

            current_neigbor.g = current_Node.g + 1
            current_neigbor.h = heuristics(current_neigbor.position)
            current_neigbor.f = current_neigbor.g + current_neigbor.h
            moves+=1

            if( check_currentAstar( open , current_neigbor)==True ):
                open.append(current_neigbor)
       
















#--------------------------------------------------------------------------------------------------------------
# GREEDY Best First Search algorithm
class NodeGBFS:
    def __init__(self , position , cost , h ):
        self.position = position
        self.cost = cost
        self.h = h
    def __lt__(self, other):
        return self.h < other.h
    def __eq__(self, other):
        return self.position == other.position

def createNodeGBFS(position , cost , h ):
        return NodeGBFS(position , cost , h ) 

def get_NeighborsGBFS(node ):
    neigbors_list = []
    if(move_up(node.position)):
        new_Node = createNodeGBFS(move_up(node.position) , node.cost+1 , node.h )
        neigbors_list.append(new_Node)
    if(move_left(node.position)):
        new_Node = createNodeGBFS(move_left(node.position) , node.cost+1 , node.h )
        neigbors_list.append(new_Node)
    if(move_right(node.position)):
        new_Node = createNodeGBFS(move_right(node.position) , node.cost+1 , node.h )
        neigbors_list.append(new_Node)
    if(move_down(node.position)):
        new_Node = createNodeGBFS(move_down(node.position) , node.cost+1 , node.h )
        neigbors_list.append(new_Node)
    return neigbors_list 
    
def check_currentGBFS( open , current_neigbor):
    for node in open:
        if (node==current_neigbor and current_neigbor.h >= node.h):
            return False
    return True
def GBFS(node , moves):
    open = []
    closed = []

    open.append(node)
    open_lenght = len(open)

    while( open_lenght > 0 ):
        open.sort()
        current_Node = open.pop(0)
        closed.append(current_Node)
        
        if(current_Node.position == goal):
            print("GBFS Algorithm\n\tPath cost :" + str(current_Node.cost) + "\n\tMoves :" + str(moves) +"\n" )
            return True
        
        neigbors  = get_NeighborsGBFS(current_Node )

        for current_neigbor in neigbors:
            if current_neigbor in closed:
                continue

            current_neigbor.h = heuristics(current_neigbor.position)
            moves+=1

            if( check_currentGBFS( open , current_neigbor)==True ):
                open.append(current_neigbor)
                
















#--------------------------------------------------------------------------------------------------------------
# Main
if __name__ == "__main__":

    root_nodeAstar = createNodeAstar(start , 0 , 0 , heuristics(start) , 0)
    movesAstar = 0

    print("")
    A_Star(root_nodeAstar , movesAstar)

    print("")

    root_nodeGBFS = createNodeGBFS(start , 0 , heuristics(start))
    movesGBFS = 0

    GBFS(root_nodeGBFS , movesGBFS)