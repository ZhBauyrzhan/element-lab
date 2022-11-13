a = int(input())
ans = 9*60 + a * 45 + ( (a-1)//2 + (a-1)%2  )*5  + (a-1)//2 * 15;
print(ans//60, ans%60)