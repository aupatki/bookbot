from stats import word_count, char_count, get_book_text, dict_list

def main():
    import sys
    book_path = ""
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]


    with open(book_path) as file:
        book_text = get_book_text(file)

        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")

        print(f"Found {len(word_count(book_text))} total words")

        print("--------- Character Count -------")
        chars = char_count(book_text)

    d_list = dict_list(chars) 

    sorted_list = []
    for i in range (0, len(d_list)):   

        c = d_list[i]['char'] 
        if c.isalpha():

            num = d_list[i]['count'] 

            # DEBUG print(f"{num} instances of {c}")
            # DEBUG print (i)

            if(i):
                for j in range (0,i):
                    # DEBUG print (f"J: {j}, I: {i}")
                    lower_bound = float("-inf")
                    upper_bound = sorted_list[j][1]
                    if len(sorted_list) == 1:
                        # DEBUG print (f"Sorted list has 1 element: {sorted_list}")
                        if num > upper_bound:
                            sorted_list = [(c,num)] + sorted_list
                            # DEBUG print(sorted_list)
                        else: 
                            sorted_list = sorted_list + [(c,num)]
                            # DEBUG print (sorted_list)
                    elif len(sorted_list) > 1: 
                        # DEBUG print(f"Sorted list has multiple elements: {len(sorted_list)}")
                        # DEBUG print(f"before: {sorted_list}")
                        lower_bound = sorted_list[j+1][1]
                        # DEBUG print(f"Upper: {upper_bound}, Lower: {lower_bound}, Num: {num}")
                        if num >= lower_bound and num < upper_bound:
                            sorted_list = sorted_list[0:j+1] + [(c,num)] + sorted_list[j+1:]
                            # DEBUG print(f"after: {sorted_list}")
                            break
                        elif num > upper_bound and j==0:
                            sorted_list = [(c,num)] + sorted_list
                            # DEBUG print(f"after: {sorted_list}")
                            break
                        elif num <= lower_bound and j==len(sorted_list)-2: 
                            sorted_list = sorted_list + [(c,num)]
                            # DEBUG print(f"after: {sorted_list}")
                            break
                    # DEBUG print (upper_bound)
                    # DEBUG print(lower_bound) 

            else:
                sorted_list.append((c,num))
                # DEBUG print ("GOT HERE")
    
    for i in range(0, len(sorted_list)):
        print(f"{sorted_list[i][0]}: {sorted_list[i][1]}")
    
    # DEBUG print(sorted_list)




            

    

main()