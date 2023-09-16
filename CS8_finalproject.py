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
def decrypt_rail_fence(message, num_rails): 
  #defines the function
    indices = make_rails(message, num_rails) 
  #calls the make_rails function
    rail_len = [0] * num_rails 
  #empty set of list has been created
     
    start_message = 0 
  #set message_start index to 0, will be used in 
    decrypted_message = [' '] * len(message) 
  #Creating a variable/assigning it to the 
  #product of an empty list and the length of the message to determine the amount of 
  #times the code will reproduce
     
    for letter in range(len(message)): 
    #create a for loop
    #the variable (letter) takes characters from 0 to the length of 
    #message to go through each character
         rail_len[indices[letter]] = rail_len[indices[letter]] + 1
        #rail_len[indices[letter]] allows the user to obtain rail_len at any index 
        #that which is determined by indices[letter]
         #We increment the value by 1 to keep track of the different rails
 
    for rail_num in range(num_rails): 
    #creates a for loop
    #iterates over the values from the index 0 to num_rails
        rail_length = rail_len[rail_num] 
        #created a variable/rail_len list is created based on the value of rail_num
        for _track in range(rail_length): 
        #creates for loop
        #track keeps track of the amount of loops from 0 to rail_len
          decrypted_message[start_message] = message[start_message] 
          #it replicates a character from message
          start_message = start_message + 1 
          #increments value by 1 to make sure it moves on to the following character
             
 
    decrypted_message = ''.join(decrypted_message) 
    #uses join() to combine all characters from the decrypted_message
    decrypt = decrypted_message.replace(' ', '') 
    #since our output requires no spaces, replace() helps us get rid of the spaces
 
    return decrypt 
    #return the decrypt variable
 
if __name__ == '__main__':
  message = input() 
  #create variable to allow a user_input string
  num_rails = int(input()) 
  #creates variable to allow a user_input integer   
   
  encrypted_message = encrypt_rail_fence(message, num_rails) 
  #calls the encrypt function
  print(encrypted_message) 
  #outputs the encrypt function
   
  decrypted_message = decrypt_rail_fence(message, num_rails) 
  #calls the decrypt function
  print(decrypted_message) 
  #ouputs the decrypt function
