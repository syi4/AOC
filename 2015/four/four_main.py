import hashlib

def find_min_number(input="iwrupvqb", target_zeros=6):
     number = 0
     prefix = '0' * target_zeros
    
     while True:
        hash_input = f"{input}{number}".encode('utf-8')
        hash_result = hashlib.md5(hash_input).hexdigest()
        
        if hash_result.startswith(prefix):
            return number  
        
        number += 1 

print(find_min_number())

