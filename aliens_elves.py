ones_accumulator=[]
ceros_accumulator=[]
long_list=[]
maximum = 0
while True:
    alien_message=input("Enter the alien message (binary message) received:")
    alien_message=alien_message.strip()
    arr=list(alien_message)
    n=len(alien_message)
    #validation condition:
    if all([ x=="1" or x=="0" for x in alien_message]):
        if all([ h=="1" for h in alien_message]) or all([ l=="0" for l in alien_message]):
            print("There is no string with the same number of zeros and ones")
            break
        else:
            #define the function that sorts the 0s and 1s, and transforms them into integers
            def transfor(element=0):
                if element=="0":
                    ceros_accumulator.append(0)
                else:
                    ones_accumulator.append(int(element))
                return int(element)
            arr= list( map(transfor, arr) )
            ceros=len(ceros_accumulator)
            ones=len(ones_accumulator)
            #showing how many zeros and ones there are in the message:
            print("This is the message written as a list of integers: ", arr)
            print("number of ZEROS in the message: ",ceros)
            print("number of ONES in the message: ",ones)
            
            for k in range(0,n-1):
                if arr[k]==0 and arr[k+1]==1:
                    first=[0,1]
                    break
                elif arr[k]==1 and arr[k+1]==0:
                    first=[1,0]
                    break    
            for i in range(0,n-1):  
                if arr[i]==0:
                    sum=-1 
                else:
                    sum=1
                # Leaving "i" fixed and moving "j", to obtain all possible combinations
                for j in range(i+1,n):
                    if arr[j]==0:
                        sum+=-1 
                    else: 
                        sum+=1
                    #Taking the largest list that has zero sum
                    if sum==0 and maximum<j-i+1:
                        maximum=j-i+1
                        initial_index=i                                 
            for k in range(initial_index, initial_index + maximum):
                long_list.append(arr[k])
            print("The first string found from left to right is: ", first)                                          
            print("THE LONGEST SEGMENT IS: ",long_list)
            print("the longest segment is found from the position:", initial_index, "to", initial_index + maximum-1)
            print("The LENGTH of the longest segment is: ", len(long_list))
            break            
    else:   
        print("The message is not binary, please try again")
