def knapSack(W, wt, val, n): 
  
    # Base Case 
    if n == 0 or W == 0 : 
        return 0
        
    if (wt[n-1] > W): 
        return knapSack(W, wt, val, n-1) 
        
    else: 
        return max(val[n-1] + knapSack(W-wt[n-1], wt, val, n-1), 
                   knapSack(W, wt, val, n-1)) 
  
val = [20, 130, 150] 
wt = [13, 30, 45] 
W = 50
n = len(val) 
print knapSack(W, wt, val, n)
