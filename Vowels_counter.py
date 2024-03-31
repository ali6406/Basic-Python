with open('Writing of Charles Dickens.txt', encoding='utf-8') as file:
    text = file.read()
vowels = ['a', 'e', 'i', 'o', 'u']
counts = [text.lower().count(vowel) for vowel in vowels] #capital letters are converted to lower letters
dictionary = dict(zip(vowels, counts))
print("Total vowels:", sum(counts),"\nCount of each vowel:",dictionary,"\n","-"*25)

scaling_factor = 0.1 #scaling count of each vowel to fit histogram in screen
scaled_counts = [int(count * scaling_factor) for count in counts]
print("a/A:","#"*scaled_counts[0],"\ne/E:","#"*scaled_counts[1],"\ni/I:","#"*scaled_counts[2],
      "\no/O:","#"*scaled_counts[3],"\nu/U:","#"*scaled_counts[4],"\n","-"*25)
# Transpose and print the vertical histogram
for level in range(max(scaled_counts), 0, -1):
    print("     ".join("#" if each_value >= level else " " for each_value in scaled_counts))
print("a/A  e/E   i/I   o/O   u/U")
    



