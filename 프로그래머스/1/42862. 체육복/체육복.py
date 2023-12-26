def solution(n, lost, reserve): 
    answer = 0 
    
    set_r = set(reserve)-set(lost) 
    set_l = set(lost)-set(reserve) 
    
    for size in set_r: 
        if size-1 in set_l: 
            set_l.remove(size-1) 
            
        elif size+1 in set_l: 
            set_l.remove(size+1) 
            
    answer = n - len(set_l)
    
    return answer