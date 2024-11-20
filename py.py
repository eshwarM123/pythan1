import math
p=3
q=7
n=p*q
print("n=",n)
phi=(p-1)*(q-1)
print("phi=",phi)
e=2
while(e<phi):
    if(math.gcd(e,phi)==1):
        break
    else:
        e+=1
print("e=",e)
k=2
d=((k*ph)+1)/e
print("d=",d)
print("public key",{e,n})
print("private key",{d,n})
msg=11
print("original message",msg)
C=pow(ms,e)
C=math.fmod(C,n)
print("encrypted message",C)
M=po(C,d)
M=math.fmod(M,n)
print("decrypted msg",M)
