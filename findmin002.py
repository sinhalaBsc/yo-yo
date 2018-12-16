
# define philosophers position
pil =[1,2,3,4,5]
    

# philosophers id
pid =[6,2,9,1,3]
    # 1 2 3 4 5

# philosophers connection in order
con =[[5,2],[1,3],[2,4],[3,5],[4,1]]
     # 1     2     3     4     5

# YO_CON 
YO_CON =[[0,0],[0,0],[0,0],[0,0],[0,0]]
        # 1     2     3     4     5
     
# YO
YO_VAL =[]   # yo value
YO_DIC =[]   # yo direction


def getIndex(arr,var):
    i=0
    for a in arr:
        if a==var:
            return i
        i+=1
    return -1



# each node communication with their neighbors
# and compare  each others id value to find minimum
for i in range(len(con)):
    YO_VAL.append([])             # new node communication add for value
    YO_DIC.append([])             # new node communication add for direction
    pil_Connections = con[i]
    pil_value =pid[i]

    for in_neighbour in pil_Connections:
        in_neighbour_value=pid[getIndex(pil,in_neighbour)]
        if pil_value > in_neighbour_value:
            YO_VAL[i].append([in_neighbour ,in_neighbour_value])
            YO_DIC[i].append([in_neighbour ,-1])
        else:
            YO_VAL[i].append([in_neighbour ,pil_value])
            YO_DIC[i].append([in_neighbour ,1])





print(YO_VAL)
print(YO_DIC)



def compare_arranger(arr):
    a=[]
    l=len(arr)
    for out1 in range(l):
        for out2 in range(out1+1,l):
            a.append([arr[out1],arr[out2]])
    return a
        
def get_neighbour_index(phil_position,neighbour_def):
    for i in range(len(YO_VAL[phil_position])):
        if YO_VAL[phil_position][i][0]==neighbour_def:
            return i
    print('error get_neighbour_id')    
    return -1,-1    

def get_neighbour_id(phil_position,neighbour_def):
    i=get_neighbour_index(phil_position,neighbour_def)
    return YO_VAL[phil_position][i][1]


def set_neighbour_s_value(phil_position,neighbour_def,neighbour_id):
    global YO_VAL    
    p=get_neighbour_index(phil_position,neighbour_def)
    YO_VAL[phil_position][p][1]=neighbour_id


def set_neighbour_s_direction(phil_position,neighbour_def,direction):
    global YO_DIC
    p=get_neighbour_index(phil_position,neighbour_def)
    YO_DIC[phil_position][p][1]=direction #YO_DIC[phil_position][p][1]*(-1)

def get_neighbours(phil_position):
    return con[phil_position]

def get_philosopher_position(phil_def): # n - philosopher def
    return getIndex(pil,phil_def)

def out_neighbours_compare(phil):
    # from philosopher's name get his position 
    phil_position=get_philosopher_position(phil)

    # get all philosopher's neighbours around him
    phil_neighbours=get_neighbours(phil_position)      # array 1d
    
    # make array two by n  to compare  philosophers at one time only two
    com_neighbours=compare_arranger(phil_neighbours)   # array 2d

    # compare neighbour's id between them
    for neighbour_def in com_neighbours:
        neighbour_id1=get_neighbour_id(phil_position,neighbour_def[0])
        neighbour_id2=get_neighbour_id(phil_position,neighbour_def[1])

        if neighbour_id1>neighbour_id2:

            # changes for  philosopher
            set_neighbour_s_value(phil_position,neighbour_def[0],neighbour_id2)
            set_neighbour_s_direction(phil_position,neighbour_def[0],1)
            
            # changes for  philosopher's neighbour
            neighbour_position=get_philosopher_position(neighbour_def[0])
            set_neighbour_s_value(neighbour_position,phil,neighbour_id2)
            set_neighbour_s_direction(neighbour_position,phil,-1)
        
        else:
            # changes for  philosopher
            set_neighbour_s_value(phil_position,neighbour_def[1],neighbour_id1)
            set_neighbour_s_direction(phil_position,neighbour_def[1],1)

            # changes for  philosopher's neighbour
            neighbour_position=get_philosopher_position(neighbour_def[1])
            set_neighbour_s_value(neighbour_position,phil,neighbour_id1)
            set_neighbour_s_direction(neighbour_position,phil,-1)
            
    print('updeated value and direction')
    print(YO_VAL)
    print(YO_DIC)

'''
out_neighbours_compare(1)
out_neighbours_compare(3)
out_neighbours_compare(5)
out_neighbours_compare(1)
'''

x=0
T=True
while T:
    block_round=0
    for neighbour in range(len(YO_DIC)):
        print('neighbour ',neighbour+1)
        block_neighbour=0
        for d in YO_DIC[neighbour]:
            if d[1]<0:
                block_neighbour+=1
        if block_neighbour>1:
            out_neighbours_compare(neighbour+1)
            block_round+=1
        else:
            pass
    if not block_round:
        T=False

def ask_leader(p):
    pil=get_philosopher_position(p)
    leader=YO_VAL[pil][0][1]
    name=getIndex(pid,leader)+1 # +1 for to escape to '0'in array
    return leader,name
    
    
   
# input the pil name to ask who is the leader at this time    
leader,name=ask_leader(1)
print('The leader id   is - ',leader)
print('The leader name is - ',name)







