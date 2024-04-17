val = [1,5,10,20,50]


# versión iterativa...
def g_desglosar(importe, val):

    res = []
    i = len(val)-1
    while i >= 0:
        dem = val[i]
        if importe >= dem:
            res.append(dem)
            importe -= dem
        else:
            i -= 1
    return res

print (f"Solución greedy para desglosar 99 es {g_desglosar(99,val)}")   

# versión DI

def DI_desglosar(importe, val,memo=None):
    
    if memo is None:
        memo = {}
    
    if importe <= 0:
        return []
    
    if importe in memo:
        return memo[importe]
        
    o_len = 2*importe
    o_sol = []
    
    # scan all options....
    for dem in val:
        # only consider those which fit...
        if importe >= dem:
            sol = [dem] + DI_desglosar(importe-dem,val,memo)
            
            # if better solution take it...
            if len(sol) < o_len:
                o_sol = sol
    
    # store in memo and return
    memo[importe] = o_sol
    return o_sol



print (f"Solución Prog Dinámica para desglosar 99 es {DI_desglosar(99,val)}")   
    

