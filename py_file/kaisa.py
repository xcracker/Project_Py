for x in range(0,len(C)):
    #ÊäÈë´óĞ´×ÖÄ¸
     if ord(C[x])<=ord("Z") and ord(C[x])-3>=ord("A"):
         print chr(ord(C[x])-3),
        
     elif ord(C[x])-3<ord("A") and ord(C[x])<=ord("Z"):
         print chr(ord("Z")+ord(C[x])-3-ord("A")+1),