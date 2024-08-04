from priority_queue_one import Priority_Queue
from time import *
from copy import deepcopy
def bestFirstSearch(initial_state, goal_state):
    obj =Priority_Queue()
    obj.enqueue(calculateHeuristic(initial_state, goal_state), initial_state,1)
    visited =[]
    mydic ={}
    mydic[tuple(map(tuple, initial_state))] =0
    x =0
    while obj.is_empty()!=True:
        x +=1
        
        new_obj =(obj.dequeue())
        d =new_obj.depth +1
        new_obj =new_obj.obj
        visited.append(new_obj)

        ind=index_of(new_obj, 0)
        i =ind[0]
        j =ind[1]
        if new_obj==goal_state:
            print("Solution Found")
            
            path =[]
            c =mydic[tuple(map(tuple, goal_state))]
        
            path.append(goal_state)
            while c!=0:
               
                path.append(c)
                c =mydic[tuple(map(tuple, c))]
            path.reverse()
            
            
            display_path(path)
            print(len(path))
            break
        
        for pos in [(0,1),(0,-1),(1,0),(-1,0)]:
            li =deepcopy(new_obj)
            
           
            
        
        
        
            new_pos =(i+pos[0], j + pos[1])
        
            if 0<=new_pos[0]<=2 and 0<=new_pos[1]<=2:
                li[i][j] =li[new_pos[0]][new_pos[1]]
                li[new_pos[0]][new_pos[1]] =0
         
                if li not in visited:
                
                    new_prio =calculateHeuristic(li, goal_state)+d
                   
                    v =obj.search(li)
                    if v!=False:
                        if new_prio<v:
                            obj.update(new_prio, li, d)
                              
                    else:
                        
                        obj.enqueue(new_prio, li, d) 
                              

                    mydic[tuple(map(tuple, li))] =new_obj

  

    



def display_path(li):
    for i in li:
        print(i)
       
def index_of(li, x):
    for i in range(len(li)):
        for j in range(3):
            if li[i][j]==x:
               
                return (i, j)
def calculateHeuristic(current_state, goal_state):
    #implementing using manhattan heuridtic
    heuristic =0
    for i in range(3):
        for j in range(3):
            if goal_state[i][j]!=0:
                v =index_of(current_state, goal_state[i][j])
                
                a =v[0]
                b =v[1]
                heuristic +=(abs(a-i) + abs(b-j))
        
    return heuristic

    

def main():
    initial_state =[[2,3,6],
                    [1,5,0],
                    [4, 7,8]]
    goal_state =[[1,2,3],
                 [4,5,6],
                 [7,8,0]]
    bestFirstSearch(initial_state, goal_state)

main()