# CIS 122 Fall 2020 Lab 7 Part 2
# Author: Jacob Burke
# Partner: 
# Description: Created a function that loops through each line of a text,
# where each line has a word. The function calculates and displays the results
# of this loop at the end, with data given such as how many words started with
# a certain letter, or how many palindromes were there.

# Assign variables:
text_file = "words_alpha.txt"

# Create Function
def parse_file(text_file):
    '''
    Opens the file inputed as a parameter of the function, loops through each
    line of the file. As it scans each line, it checks it line's word and
    adjusts counters based on the word. Once all lines have been checked in the
    file the loop ends, and the results are printed out for the user with the
    function call then ending.

    Extended Summary:
    A file is used as a parameter for the function and is opened. Local variables
    are then established in the function to be used as counters for starting
    letters of words, variables for length of words, and variables of the
    longest and shortest words. The function then loops through each line,
    adjusting counters and variables based on the lowercase word in each line.
    Once all lines have been checked in the file the loop ends and the file is
    closed. The results are then printed out for the user with the function
    thus ending.

    Args:
    text_file (str): file input

    Returns:
    None
    '''
    fin = open(text_file)
    line_count = 0
    longest_word = ''
    longest_word_length = 0
    shortest_word = ''
    shortest_word_length = 0
    palindrome_count = 0
    A_counter = 0
    B_counter = 0
    C_counter = 0
    D_counter = 0
    E_counter = 0
    F_counter = 0
    G_counter = 0
    H_counter = 0
    I_counter = 0
    J_counter = 0
    K_counter = 0
    L_counter = 0
    M_counter = 0
    N_counter = 0
    O_counter = 0
    P_counter = 0
    Q_counter = 0
    R_counter = 0
    S_counter = 0
    T_counter = 0
    U_counter = 0
    V_counter = 0
    W_counter = 0
    X_counter = 0
    Y_counter = 0
    Z_counter = 0
    Misc_counter = 0
    line_length = 0
    for line in fin:
        current_line = str(line.strip().lower())
        line_count = line_count + 1
        line_length = len(current_line.strip())
        if line_length > longest_word_length:
            longest_word = current_line
            longest_word_length = len(current_line)
        if shortest_word == '':
            shortest_word = current_line
            shortest_word_length = len(current_line)
        if line_length < shortest_word_length:
            shortest_word = current_line
            shortest_word_length = len(current_line)
        if current_line == current_line[::-1]:
            palindrome_count = palindrome_count + 1
        if line.strip()[0] == 'a':
           A_counter = A_counter +1
        elif line.strip()[0] == 'b':
           B_counter = B_counter +1
        elif line.strip()[0] == 'c':
           C_counter = C_counter +1
        elif line.strip()[0] == 'd':
           D_counter = D_counter +1
        elif line.strip()[0] == 'e':
           E_counter = E_counter +1
        elif line.strip()[0] == 'f':
           F_counter = F_counter +1
        elif line.strip()[0] == 'g':
           G_counter = G_counter +1
        elif line.strip()[0] == 'h':
           H_counter = H_counter +1
        elif line.strip()[0] == 'i':
           I_counter = I_counter +1
        elif line.strip()[0] == 'j':
           J_counter = J_counter +1
        elif line.strip()[0] == 'k':
           K_counter = K_counter +1
        elif line.strip()[0] == 'l':
           L_counter = L_counter +1
        elif line.strip()[0] == 'm':
           M_counter = M_counter +1
        elif line.strip()[0] == 'n':
           N_counter = N_counter +1
        elif line.strip()[0] == 'o':
           O_counter = O_counter +1
        elif line.strip()[0] == 'p':
           P_counter = P_counter +1
        elif line.strip()[0] == 'q':
           Q_counter = Q_counter +1
        elif line.strip()[0] == 'r':
           R_counter = R_counter +1
        elif line.strip()[0] == 's':
           S_counter = S_counter +1
        elif line.strip()[0] == 't':
           T_counter = T_counter +1
        elif line.strip()[0] == 'u':
           U_counter = U_counter +1
        elif line.strip()[0] == 'v':
           V_counter = V_counter +1
        elif line.strip()[0] == 'w':
           W_counter = W_counter +1
        elif line.strip()[0] == 'x':
           X_counter = X_counter +1
        elif line.strip()[0] == 'y':
           Y_counter = Y_counter +1
        elif line.strip()[0] == 'z':
           Z_counter = Z_counter +1
        else:
            Misc_counter = Misc_counter + 1
           
    # Close file
    fin.close()
    # Print results
    print("Count: " + str(line_count))
    print("Longest word is " + longest_word + " (" + str(longest_word_length) + ")")
    print("Shortest word is " + shortest_word + " (" + str(shortest_word_length) + ")")
    print("Palindromes: " + str(palindrome_count) + " (" + str(round((palindrome_count / line_count) * 100, 2)) + "%)")
    print("First letter counts")
    print("A: " + str(A_counter) + " (" + str(round((A_counter / line_count) * 100, 2)) + "%)")
    print("B: " + str(B_counter) + " (" + str(round((B_counter / line_count) * 100, 2)) + "%)")
    print("C: " + str(C_counter) + " (" + str(round((C_counter / line_count) * 100, 2)) + "%)")
    print("D: " + str(D_counter) + " (" + str(round((D_counter / line_count) * 100, 2)) + "%)")
    print("E: " + str(E_counter) + " (" + str(round((E_counter / line_count) * 100, 2)) + "%)")
    print("F: " + str(F_counter) + " (" + str(round((F_counter / line_count) * 100, 2)) + "%)")
    print("G: " + str(G_counter) + " (" + str(round((G_counter / line_count) * 100, 2)) + "%)")
    print("H: " + str(H_counter) + " (" + str(round((H_counter / line_count) * 100, 2)) + "%)")
    print("I: " + str(I_counter) + " (" + str(round((I_counter / line_count) * 100, 2)) + "%)")
    print("J: " + str(J_counter) + " (" + str(round((J_counter / line_count) * 100, 2)) + "%)")
    print("K: " + str(K_counter) + " (" + str(round((K_counter / line_count) * 100, 2)) + "%)")
    print("L: " + str(L_counter) + " (" + str(round((L_counter / line_count) * 100, 2)) + "%)")
    print("M: " + str(M_counter) + " (" + str(round((M_counter / line_count) * 100, 2)) + "%)")
    print("N: " + str(N_counter) + " (" + str(round((N_counter / line_count) * 100, 2)) + "%)")
    print("O: " + str(O_counter) + " (" + str(round((O_counter / line_count) * 100, 2)) + "%)")
    print("P: " + str(P_counter) + " (" + str(round((P_counter / line_count) * 100, 2)) + "%)")
    print("Q: " + str(Q_counter) + " (" + str(round((Q_counter / line_count) * 100, 2)) + "%)")
    print("R: " + str(R_counter) + " (" + str(round((R_counter / line_count) * 100, 2)) + "%)")
    print("S: " + str(S_counter) + " (" + str(round((S_counter / line_count) * 100, 2)) + "%)")
    print("T: " + str(T_counter) + " (" + str(round((T_counter / line_count) * 100, 2)) + "%)")
    print("U: " + str(U_counter) + " (" + str(round((U_counter / line_count) * 100, 2)) + "%)")
    print("V: " + str(V_counter) + " (" + str(round((V_counter / line_count) * 100, 2)) + "%)")
    print("W: " + str(W_counter) + " (" + str(round((W_counter / line_count) * 100, 2)) + "%)")
    print("X: " + str(X_counter) + " (" + str(round((X_counter / line_count) * 100, 2)) + "%)")
    print("Y: " + str(Y_counter) + " (" + str(round((Y_counter / line_count) * 100, 2)) + "%)")
    print("Z: " + str(Z_counter) + " (" + str(round((Z_counter / line_count) * 100, 2)) + "%)")
    print("Other: " + str(Misc_counter) + " (" + str(round((Misc_counter / line_count) * 100, 2)) + "%)")
    return


# Parse File and display results:
parse_file(text_file)


    
