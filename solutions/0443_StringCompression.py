from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        while i < len(chars):
            if i == 0:
                current = chars[i]
                count = 1
                i += 1
            else:
                if chars[i] == current:
                    del chars[i]
                    count += 1
                else:
                    current = chars[i]
                    if count > 1:
                        str_num = str(count)
                        for digit in str_num:
                            chars.insert(i, digit)
                            i += 1
                        count = 1
                        i += 1
                    else:
                        count = 1
                        i += 1
        if count > 1:
            str_num = str(count)
            for digit in str_num:
                chars.append(digit)
        
        return(len(chars))
    


    def compress2(self, chars: List[str]) -> int:
        # Setup
        current = chars[0]
        count = 1
        i = 1

        # Sliding window through array
        while i < len(chars):
            print("\n")
            print(chars)
            print(f"current character {chars[i]} at index {i}")
            if chars[i] == current:
                count += 1
                del chars[i]
                print(f"Deleted {current}, count is now {count}")
            else:
                if count > 1:
                    str_count = str(count)
                    for digit in str_count:
                        chars.insert(i, digit)
                        i += 1
                    i += 1
                else:
                    i += 1
                current = chars[i] 
                print(f"New chain of {current}")
                count = 1
        
        # Add final group
        print(f"count is {count}")
        if count > 1:
            str_count = str(count)
            for digit in str_count:
                chars.insert(i, digit)
                i += 1
        print(chars)
        return len(chars)
        