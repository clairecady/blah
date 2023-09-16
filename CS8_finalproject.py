def make_rails(message, num_rails): 
  #defines function make_rails(message, num_rails)
  indices = [] 
  #creates an empty list literal under the variable indices
  period = (num_rails - 1) * 2 
  #computes the period or cycle of the wave of the cipher
  #done so by taking the number of rails, subracting one, and dividing by two

  for i in range(len(message)): 
    #length of the message counts the number of characters
    #range of that starts the sequnce at zero
    #the for loop iterates the following for each number
    rail_num = 0 if period == 0 else i % period 
    #finds the rail number by finding
    #the remainder of the specific number when divided by the period
    #unless the period is zero (thus the number of rails is one)
    #because then the characters would be on the same row
    if rail_num >= num_rails: 
      #accounts for the case of the rail number being bigger
      #or equal to the number of rails
      #which creates too many rails and the characters only go down
        rail_num = period - rail_num 
      #so the rail number is subtracted from the period

    indices.append(rail_num) 
    #puts together every rail number inside the list literal
 
  return indices 
  #returns the indices under the definition
 
def encrypt_rail_fence(message, num_rails): 
  #defines function
     indices = make_rails(message, num_rails) 
  #indices is defined by 
  # the reult of make_rails(message, num_rails)
     rails = [''] * num_rails 
  #creates an empty set of list literals under the variable rails
  #done by multiplying empty list literals by the number of rails 
  #so characters can be placed within then to create the message
     
     message = message.replace(' ','') 
  #removes all the spaces from the message  
     
     for i, char in enumerate(message): 
      #enumerating message iterates over it and
      #creates an iteration counter
      #introduces a for loop for every character in the message  
       rails[indices[i]] += char 
      #adds each character to the correct rail based on the rail number assigned
      #by indices
 
     encrypted_message = ' '.join(rails) 
  #joins together the rails with spaces in between
     return encrypted_message
  #returns the encrypted message under the function
def decrypt_rail_fence(message, num_rails): #We created our function!
    indices = make_rails(message, num_rails) #We called our previous function make_rails to get the rail pattern
    position = 0 #message starts at index 0
    rails = [''] * num_rails #We created an empty list of strings and multiplied it by num_rails to get one for each rail
    
    #This for loop was used to reconstruct the rails
    for rail_num in range(num_rails): 
        for track in range(len(message)):
            if indices[track] == rail_num:
                rails[rail_num] = rails[rail_num] + message[position]
                position = position + 1
                
    
    decrypted_message = [''] #Start with an empty list     
    for i, rail_num in enumerate(indices): #used to tell us what rail should pick up the next character
        append_letter = rails[rail_num][0] #gets the first character which is why it starts at zero
        decrypted_message.append(append_letter)
        rails[rail_num] = rails[rail_num][1:] #removes the character that we had just utilized from the rail
        
    message = message.replace(' ', '') #we moved the spaces since the decrypt output is supposed to displat without any spaces
    
    secret_message = ''.join(decrypted_message) #it combines all the characters into a single string

    return secret_message #return our function


if __name__ == '__main__':
  message = input() #create variable to allow a user_input string
  num_rails = int(input()) #creates variable to allow a user_input integer
  
  encrypted_message = encrypt_rail_fence(message, num_rails) #calls the encrypt function
  print(encrypted_message) #outputs the encrypt function
  
  decrypted_message = decrypt_rail_fence(message, num_rails) #calls the decrypt function
  print(decrypted_message) #ouputs the decrypt function
