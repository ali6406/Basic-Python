message = input("Enter string to be encrypted or decrypted:")
option = input("You want to encrypt or decrypt?")
even_no = [0,2,4,6,8,10,12,14,16]
odd_no = [1,3,5,7,9,11,13,15,17,19]

if option == "encrypt":
    encrypted = [message[i] for i in even_no + odd_no if i < len(message)] 
    print(encrypted)
elif option == "decrypt":     
    decrypted = [message[i] for i in odd_no + even_no if i < len(message)]
    print(decrypted)

