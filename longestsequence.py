def compute(str1 ,str2):
        n1 = len(str1)
        n2 = len(str2)
        i = 0
        j = 0
        result = "";
        while i<= n1 -1 and j <= n2 -1:
            if(str1[i] != str2[j]):
                break
            result += str1
            i += 1
            j += 1
        return (result)
def commonPrefix(arr, n):
        prefix = arr[0]
        for i in range(1, n):
            
             prefix = compute(prefix,arr[i])
        return prefix
if __name__ =="__main__":
 
    arr = ["geeksforgeeks", "geeks",
                    "geek", "geezer"]
    n = len(arr)
 
    ans = commonPrefix(arr, n)
 
    if (len(ans)):
        print ("The longest common prefix is -",
                ans);
    else:
        print("There is no common prefix")
    