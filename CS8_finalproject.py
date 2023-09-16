def make_rails(message, num_rails):
  indices = []
  period = (num_rails - 1) * 2

  for i in range(len(message)):
    rail_num = 0 if period == 0 else i % period
    if rail_num >= num_rails:
      rail_num = period - rail_num

    indices.append(rail_num)

  return indices
  
def encrypt_rail_fence(message, num_rails):
    indices = make_rails(message, num_rails)
    rails = [''] * num_rails 
    
    message = message.replace(' ','') 

    for i, char in enumerate(message):
        rails[indices[i]] += char 

    encrypted_message = ' '.join(rails) 
    return encrypted_message
    
def decrypt_rail_fence(message, num_rails): 
    indices = make_rails(message, num_rails)
    position = 0
    rails = [''] * num_rails
    
    for rail_num in range(num_rails):
        for track in range(len(message)):
            if indices[track] == rail_num:
                rails[rail_num] = rails[rail_num] + message[position]
                position = position + 1
                
    
    decrypted_message = ['']
        
    for i, rail_num in enumerate(indices):
        append_letter = rails[rail_num][0]
        decrypted_message.append(append_letter)
        rails[rail_num] = rails[rail_num][1:]
        
    message = message.replace(' ', '') 
    
    secret_message = ''.join(decrypted_message)

    return secret_message


if __name__ == '__main__':
  message = input() 
  num_rails = int(input()) 
  
  encrypted_message = encrypt_rail_fence(message, num_rails)
  print(encrypted_message) 
  
  decrypted_message = decrypt_rail_fence(message, num_rails) 
  print(decrypted_message) 
