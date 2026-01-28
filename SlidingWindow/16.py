for i in range(len(nums)):
            for j in range(i,len(nums)):
                win=nums[i:j+1]
                if len(set(win))==k:
                    c+=1
        return c