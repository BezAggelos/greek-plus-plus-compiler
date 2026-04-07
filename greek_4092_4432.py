#######################################
#       Μεταφραστές Project 2025      #
#######################################
#       Μπεζαΐτης Άγγελος : 4432      #
#     Γιάννης Κωνσταντινίδης : 4092   #
#######################################

import sys

if len(sys.argv) < 2:
    print("Usage: python mycompiler2.0.py <filename>")
    sys.exit(1)

file = open(sys.argv[1], 'r', encoding='utf-8')
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
            'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
            'Α','Β','Γ','Δ','Ε','Ζ','Η','Θ','Ι','Κ','Λ','Μ','Ν','Ξ','Ο','Π','Ρ','Σ','Τ','Υ','Φ','Χ','Ψ','Ω',
            'α','β','γ','δ','ε','ζ','η','θ','ι','κ','λ','μ','ν','ξ','ο','π','ρ','σ','τ','υ','φ','χ','ψ','ω','ς',
            'Ά','Έ','Ή','Ί','Ό','Ύ','Ώ','ά','έ','ή','ί','ό','ύ','ώ']
numbers = ['0','1','2','3','4','5','6','7','8','9']

#characters in finite-state automaton
empty_char = 0  # space, tab
letter = 1  # A-Z, a-z, Α-Ω, α-ω
number = 2  # 0-9
plus = 3    # +
minus = 4   # -
mult = 5    # *
div = 6    # /
smaller_than = 7    # <
greater_than = 8    # >
equal = 9   # =
modulo = 10 # %
lower = 11  # _
semicolon = 12  # ;
comma = 13  # ,
colon = 14  # :
left_parenthesis = 15  # (
right_parenthesis = 16  # )
left_bracket = 17  # [
right_bracket = 18  # ]
EOF = 19  # end of file
left_brace = 20 # {
right_brace = 21  # }
change_line = 22  # \n
not_accepted = 23  # not accepted character

#states of finite-state automaton
start_state = 0   # start
number_state = 1    # number
letter_state = 2    # letter
assign_state = 3  # assign
smaller_state = 4  # smaller
greater_state = 5  # greater
comment_state = 6  # comment

#token
plus_token = 24 # +
minus_token = 25 # -
mult_token = 26 # *
div_token = 27  # /
left_parenthesis_token = 28    # (
right_parenthesis_token = 29   # )
left_bracket_token = 30    # [
right_bracket_token = 31   # ]
comma_token = 32    # ,
semicolon_token = 33 # ;
modulo_token = 34    # %
equal_token = 35 # =
EOF_token = 36  # end of file
colon_token = 37 # :
number_token = 38  # number
ID_token = 39  # letter
smaller_than_token = 40    # <
greater_than_token = 41    # >
smaller_or_equal_token = 42    # <=
not_equal_token = 43    # <>
greater_or_equal_token = 44    # >=
assign_token = 45    # :=
left_brace_token = 46    # {
right_brace_token = 47    # }

#Reserved Words
program_token = 1001
declare_token = 1002
if_token = 1003
then_token = 1004
else_token = 1005
endif_token = 1006
do_token = 1007
until_token = 1008
while_token = 1009
endwhile_token = 1010
for_token = 1011
to_token = 1012
withstep_token = 1013
endfor_token = 1014
read_token = 1015
write_token = 1016
function_token = 1017
procedure_token = 1018
interface_token = 1019
input_token = 1020
output_token = 1021
functionStart_token = 1022
functionEnd_token = 1023
procedureStart_token = 1024
procedureEnd_token = 1025
programStart_token = 1026
programEnd_token = 1027
or_token = 1028
and_token = 1029
execute_token = 1030
not_token = 1031

#Errors
underscore_by_itself_error = 401
right_brace_error = 402
not_accepted_symbol_error = 403
letter_in_number_error = 404
comments_not_closed_error = 405
more_than_30_characters_error = 406

transition_to_state = [
    #start_state
    [start_state, letter_state, number_state, plus_token, minus_token, mult_token, div_token, smaller_state,
     greater_state, equal_token, modulo_token, underscore_by_itself_error, semicolon_token, comma_token, assign_state, left_parenthesis_token,
     right_parenthesis_token, left_bracket_token, right_bracket_token, EOF_token, comment_state, right_brace_error, start_state, not_accepted_symbol_error],

    #number_state
    [number_token, letter_in_number_error, number_state, number_token, number_token, number_token, number_token, number_token,
     number_token, number_token, number_token, number_token, number_token, number_token, number_token, number_token,
     number_token, number_token, number_token, number_token, number_token, number_token, number_token, not_accepted_symbol_error],

    #letter_state
    [ID_token, letter_state, letter_state, ID_token, ID_token, ID_token, ID_token, ID_token,
     ID_token, ID_token, ID_token, letter_state, ID_token, ID_token, ID_token, ID_token,
     ID_token, ID_token, ID_token, ID_token, ID_token, ID_token, ID_token, not_accepted_symbol_error],

    #assign_state
    [colon_token, colon_token, colon_token, colon_token, colon_token, colon_token, colon_token, colon_token,
     colon_token, assign_token, colon_token, colon_token, colon_token, colon_token, colon_token, colon_token,
     colon_token, colon_token, colon_token, colon_token, colon_token, colon_token, colon_token, not_accepted_symbol_error],

    #smaller_state
    [smaller_than_token, smaller_than_token, smaller_than_token, smaller_than_token, smaller_than_token, smaller_than_token, smaller_than_token, smaller_than_token,
     not_equal_token, smaller_or_equal_token, smaller_than_token, smaller_than_token, smaller_than_token, smaller_than_token, smaller_than_token, smaller_than_token,
     smaller_than_token, smaller_than_token, smaller_than_token, smaller_than_token, smaller_than_token, smaller_than_token, smaller_than_token, not_accepted_symbol_error],

    #greater_state
    [greater_than_token, greater_than_token, greater_than_token, greater_than_token, greater_than_token, greater_than_token, greater_than_token, greater_than_token,
     greater_than_token, greater_or_equal_token, greater_than_token, greater_than_token, greater_than_token, greater_than_token, greater_than_token, greater_than_token,
     greater_than_token, greater_than_token, greater_than_token, greater_than_token, greater_than_token, greater_than_token, greater_than_token, not_accepted_symbol_error],

    #comment_state
    [comment_state, comment_state, comment_state, comment_state, comment_state, comment_state, comment_state, comment_state,
     comment_state, comment_state, comment_state, comment_state, comment_state, comment_state, comment_state, comment_state,
     comment_state, comment_state, comment_state, comments_not_closed_error, comment_state, start_state, comment_state, comment_state]   
]

line = 1

def find_reserved_word(word):
    reserved_words = {
        'πρόγραμμα': program_token,
        'δήλωση': declare_token,
        'εάν': if_token,
        'τότε': then_token,
        'αλλιώς': else_token,
        'εάν_τέλος': endif_token,
        'επανάλαβε': do_token,
        'μέχρι': until_token,
        'όσο': while_token,
        'όσο_τέλος': endwhile_token,
        'για': for_token,
        'έως': to_token,
        'με_βήμα': withstep_token,
        'για_τέλος': endfor_token,
        'διάβασε': read_token,
        'γράψε': write_token,
        'συνάρτηση': function_token,
        'διαδικασία': procedure_token,
        'διαπροσωπεία': interface_token,
        'είσοδος': input_token,
        'έξοδος': output_token,
        'αρχή_συνάρτησης': functionStart_token,
        'τέλος_συνάρτησης': functionEnd_token,
        'αρχή_διαδικασίας': procedureStart_token,
        'τέλος_διαδικασίας': procedureEnd_token,
        'αρχή_προγράμματος': programStart_token,
        'τέλος_προγράμματος': programEnd_token,
        'ή': or_token,
        'και': and_token,
        'εκτέλεσε': execute_token,
        'όχι': not_token
    }
    return reserved_words.get(word, ID_token)

def check_errors(temp_token):
    if (temp_token == underscore_by_itself_error): 
        print(f'ERROR(401): Underscore cannot be by itself at line {line}')
        exit(0)
    elif (temp_token == right_brace_error):
        print(f'ERROR(402): Right brace cannot be without left brace at line {line}')
        exit(0)
    elif (temp_token == not_accepted_symbol_error): 
        print(f'ERROR(403): Not accepted symbol of the language at line {line}')
        exit(0)
    elif (temp_token == letter_in_number_error): 
        print(f'ERROR(404): Character in number at line {line}')
        exit(0)
    elif (temp_token == comments_not_closed_error): 
        print(f'ERROR(405): Comments are not closed at line {line}')
        exit(0)
    elif (temp_token == more_than_30_characters_error): 
        print(f'ERROR(406): More than 30 characters at line {line}')
        exit(0)

def lex():
    global line, file
    current_state = start_state
    line_counter = line 
    current_token = ""
    
    while (current_state >= 0 and current_state <= 6):
        char = file.read(1)

        if (char == ' ' or char == '\t'): char_token = empty_char
        elif (char in alphabet): char_token = letter
        elif (char in numbers): char_token = number
        elif (char == '+'): char_token = plus
        elif (char == '-'): char_token = minus
        elif (char == '*'): char_token = mult
        elif (char == '/'): char_token = div
        elif (char == '<'): char_token = smaller_than
        elif (char == '>'): char_token = greater_than
        elif (char == '='): char_token = equal
        elif (char == '%'): char_token = modulo
        elif (char == '_'): char_token = lower
        elif (char == ';'): char_token = semicolon
        elif (char == ','): char_token = comma
        elif (char == ':'): char_token = colon
        elif (char == '('): char_token = left_parenthesis
        elif (char == ')'): char_token = right_parenthesis
        elif (char == '['): char_token = left_bracket
        elif (char == ']'): char_token = right_bracket
        elif (char == '{'): char_token = left_brace
        elif (char == '}'): char_token = right_brace
        elif (char == '\n'):
            line_counter += 1
            char_token = change_line
        elif (char == ''): char_token = EOF
        else:
            char_token = not_accepted

        current_state = transition_to_state[current_state][char_token]
        if (len(current_token) < 30):
            if (current_state != comment_state and current_state != start_state):
                current_token += char
        else:
            current_state = more_than_30_characters_error
            break
    
    if (current_state >= 37 and current_state <= 41 and char != ''):
        file.seek(file.tell()-1,0)
        current_token = current_token[:-1]
        if (char == '\n'): line_counter -= 1
    
    check_errors(current_state)

    if (current_state == ID_token):
        current_state = find_reserved_word(current_token)

    line = line_counter
    return [current_state, ''.join(current_token), line_counter] 


#######################################
#          Intermediate Code          #
#######################################

global quadList
quadList = []
quadsCounter = 1

def nextQuad():         
    global quadsCounter
    return quadsCounter

def genQuad(op, x, y, z):
    global quadsCounter, quadList
    
    quadList.append([nextQuad(), op, x, y, z])
    quadsCounter += 1

temp_var_counter = 1
def newTemp():
    global temp_var_counter
    
    tempVariable = f'T@{temp_var_counter}'
    temp_var_counter += 1
    
    entity = Entity()
    entity.type = 'TEMP'
    entity.name = tempVariable
    entity.tempVar.offset = compute_offset()
    new_entity(entity)
    
    return tempVariable

def makeList(x): return [x]
def merge(list1, list2): return list1 + list2

def backPatch(list, z):
    global quadList
    
    quad_dict = {quad[0]: idx for idx, quad in enumerate(quadList)}
    
    for quad_num in list:
        if quad_num in quad_dict and quadList[quad_dict[quad_num]][4] == '_':
            quadList[quad_dict[quad_num]][4] = z

def writeIntFile(inputFile):
    for quad in quadList:
        line = f"{quad[0]} : {quad[1]} , {quad[2]} , {quad[3]} , {quad[4]}\n"
        inputFile.write(line)

#######################################
#            Syntax Analysis          #
#######################################

def syntax_an():
    global line, token

    def program():
        global line, token

        if (token[0] == program_token):
            token = lex()
            line = token[2]

            if (token[0] == ID_token):
                IDreceived = token[1]
                token = lex()
                line = token[2]
                programblock(IDreceived)
            else:
                print(f"ERROR: Expected an identifier (ID) as the program name after 'πρόγραμμα' at line {line}")
                exit(0)
        else:
            print(f"ERROR: Expected reserved keyword 'πρόγραμμα' at the beginning of the program at line {line}")
            exit(0)

    def programblock(IDreceived):
        global token, line
        
        new_scope(IDreceived)
        declarations()
        subprograms()

        if (token[0] == programStart_token):
            token = lex()
            line = token[2]
            
            genQuad('begin_block', IDreceived, '_', '_')
            sequence()
            genQuad('halt', '_', '_', '_')
            genQuad('end_block', IDreceived, '_', '_')
            
            writeSymFile()
            final_code()
            delete_scope()

            if (token[0] == programEnd_token):
                token = lex()
                line = token[2]
            else:
                print(f"ERROR: Missing 'τέλος_προγράμματος' at the end of the script at line {line}. Found '{token[1]}' instead")
                exit(0)
        else:
            print(f"ERROR: Missing 'αρχή_προγράμματος' at the start of the script at line {line}. Found '{token[1]}' instead")
            exit(0)

    def declarations():
        global token, line
        
        while (token[0] == declare_token):
            token = lex()
            line = token[2]
            varlist('Entity')

    def varlist(flag):
        global token, line

        if (token[0] == ID_token):
            id_name = token[1]
            token = lex()
            line = token[2]
            
            if flag == 'Entity':
                entity = Entity()
                entity.type = 'VAR'
                entity.name = id_name
                entity.variable.offset = compute_offset()
                new_entity(entity)
            elif flag == 'Argument':
                argument = Argument()
                argument.name = id_name
                argument.parMode = ''
                new_argument(argument)
            elif flag == 'CV':
                for args in listOfScopes[-1].entities[-1].subprogram.argument:
                    if args.name == id_name:
                        args.parMode = 'CV'
            elif (flag == 'REF'):
                for args in listOfScopes[-1].entities[-1].subprogram.argument:
                    if args.name == id_name:
                        args.parMode = 'REF'

            while (token[0] == comma_token):
                token = lex()
                line = token[2]

                if (token[0] == ID_token):
                    id_name = token[1]
                    token = lex()
                    line = token[2]
                    
                    if flag == 'Entity':
                        entity = Entity()
                        entity.type = 'VAR'
                        entity.name = id_name
                        entity.variable.offset = compute_offset()
                        new_entity(entity)
                    elif flag == 'Argument':
                        argument = Argument()
                        argument.name = id_name
                        argument.parMode = ''
                        new_argument(argument)
                    elif flag == 'CV':
                        for args in listOfScopes[-1].entities[-1].subprogram.argument:
                            if args.name == id_name:
                                args.parMode = 'CV'
                    elif (flag == 'REF'):
                        for args in listOfScopes[-1].entities[-1].subprogram.argument:
                            if args.name == id_name:
                                args.parMode = 'REF'
                else:
                    print(f"ERROR: Expected an identifier (ID) after the comma at line {line}")
                    exit(0)
        else:
            print(f"ERROR: Expected an identifier in the declaration at line {line}")
            exit(0)

    def subprograms():
        global token

        while (token[0] == function_token or token[0] == procedure_token):
            if (token[0] == function_token): func()
            else: proc()

    def func():
        global token, line

        if (token[0] == function_token):
            token = lex()
            line = token[2]

            if (token[0] == ID_token):
                ID_received = token[1]
                token = lex()
                line = token[2]

                if (token[0] == left_parenthesis_token):
                    token = lex()
                    line = token[2]
                    
                    entity = Entity()
                    entity.type = 'SUBPR'
                    entity.name = ID_received
                    entity.subprogram.type = 'Function'
                    new_entity(entity)
                    
                    formalparlist()
                    if (token[0] == right_parenthesis_token):
                        token = lex()
                        line = token[2]
                        funcblock(ID_received)
                    else:
                        print(f"ERROR: Expected right parenthesis at line {line}")
                        exit(0)
                else:
                    print(f"ERROR: Expected left parenthesis at line {line}")
                    exit(0)
            else:
                print(f"ERROR: Expected ID after the function at line {line}")
                exit(0)

    def proc():
        global token, line

        if (token[0] == procedure_token):
            token = lex()
            line = token[2]

            if (token[0] == ID_token):
                IDreceived = token[1]
                token = lex()
                line = token[2]

                if (token[0] == left_parenthesis_token):
                    token = lex()
                    line = token[2]
                    
                    entity = Entity()
                    entity.type = 'SUBPR'
                    entity.name = IDreceived
                    entity.subprogram.type = 'Procedure'
                    new_entity(entity)
                    
                    formalparlist()
                    if (token[0] == right_parenthesis_token):
                        token = lex()
                        line = token[2]
                        procblock(IDreceived)
                    else:
                        print(f"ERROR: Expected right parenthesis ')' after parameter list at line {line}")
                        exit(0)
                else:
                    print(f"ERROR: Expected '(' before parameter list at line {line}")
                    exit(0)
            else:
                print(f"ERROR: Expected identifier after 'διαδικασία' at line {line}")
                exit(0)

    def formalparlist():
        global token

        if (token[0] == ID_token):
            varlist('Argument')

    def funcblock(ID_received):
        global token, line

        if (token[0] == interface_token):
            token = lex()
            line = token[2]
            funcinput()
            funcoutput()
            new_scope(ID_received)
            add_parameters()
            declarations()
            subprograms()

            if (token[0] == functionStart_token):
                token = lex()
                line = token[2]
                
                compute_startQuad()
                genQuad('begin_block', ID_received, '_', '_')
                sequence()
                compute_framelenght()
                genQuad('end_block', ID_received, '_', '_')
                
                writeSymFile()
                final_code()
                delete_scope()

                if (token[0] == functionEnd_token):
                    token = lex()
                    line = token[2]
                else:
                    print(f"ERROR: Reserved word 'τέλος_συνάρτησης' expected at the end of function at line {line}")
                    exit(0)
            else:
                print(f"ERROR: Reserved command 'αρχή_συνάρτησης' missing at the start of function at line {line}")
                exit(0)
        else:
            print(f"ERROR: Reserved word 'διαπροσωπεία' missing at start of function at line {line}")
            exit(0)

    def procblock(ID_received):
        global token, line

        if (token[0] == interface_token):
            token = lex()
            line = token[2]
            funcinput()
            funcoutput()
            new_scope(ID_received)
            add_parameters()
            declarations()
            subprograms()

            if (token[0] == procedureStart_token):
                token = lex()
                line = token[2]
                
                compute_startQuad()
                genQuad('begin_block', ID_received, '_', '_')
                sequence()
                compute_framelenght()
                genQuad('end_block', ID_received, '_', '_')
                
                writeSymFile()
                final_code()
                delete_scope()
                
                if (token[0] == procedureEnd_token):
                    token = lex()
                    line = token[2]
                else:
                    print(f"ERROR: Reserved word 'τέλος_διαδικασίας' expected at the end of procedure at line {line}")
                    exit(0)
            else:
                print(f"ERROR: Word 'αρχή_διαδικασίας' missing at the start of the procedure at line {line}")
                exit(0)
        else:
            print(f"ERROR: Reserved word 'διαπροσωπεία' not found at line {line}")
            exit(0)

    def funcinput():
        global token, line

        if (token[0] == input_token):
            token = lex()
            line = token[2]
            varlist('CV')

    def funcoutput():
        global token, line

        if (token[0] == output_token):
            token = lex()
            line = token[2]
            varlist('REF')

    def sequence():
        global token, line
        statement()
        
        while (token[0] == semicolon_token):
            token = lex()
            line = token[2]
            statement()

    def statement():
        global token, line

        if (token[0] == ID_token): assignment_stat()
        elif (token[0] == if_token): if_stat()
        elif (token[0] == while_token): while_stat()
        elif (token[0] == do_token): do_stat()
        elif (token[0] == for_token): for_stat()
        elif (token[0] == read_token): input_stat()
        elif (token[0] == write_token): print_stat()
        elif (token[0] == execute_token): call_stat()
        else:
            print(f"ERROR: Unknown Command '{token[1]}' at line {line}")
            exit(0)

    def assignment_stat():
        global token, line

        if (token[0] == ID_token):
            myid = token[1]
            token = lex()
            line = token[2]
            if (token[0] == assign_token):
                token = lex()
                line = token[2]
                Eplace = expression()
                genQuad(':=', Eplace, '_', myid)
            else:
                print(f"ERROR: Expected ':=' after the variable at line {line}")
                exit(0)

    def if_stat():
        global token, line

        if (token[0] == if_token):
            token = lex()
            line = token[2]
            cond = condition()
            backPatch(cond[0], nextQuad())

            if (token[0] == then_token):
                token = lex()
                line = token[2]
                sequence()
                if_list = makeList(nextQuad())
                genQuad('jump', '_', '_', '_')
                backPatch(cond[1], nextQuad())
                elsepart()
                backPatch(if_list, nextQuad())

                if (token[0] == endif_token):
                    token = lex()
                    line = token[2]
                else:
                    print(f"ERROR: Expected 'εάν_τέλος' at line {line}. Found '{token[1]}' instead")
                    exit(0)
            else:
                print(f"ERROR: Expected 'τότε' at line {line}. Found '{token[1]}' instead")
                exit(0)

    def elsepart():
        global token, line

        if (token[0] == else_token):
            token = lex()
            line = token[2]
            sequence()

    def while_stat():
        global token, line

        if (token[0] == while_token):
            token = lex()
            line = token[2]
            c_quad = nextQuad()
            cond = condition()
            backPatch(cond[0], nextQuad())

            if (token[0] == do_token):
                token = lex()
                line = token[2]
                sequence()
                genQuad('jump', '_', '_', c_quad)
                backPatch(cond[1], nextQuad())

                if (token[0] == endwhile_token):
                    token = lex()
                    line = token[2]
                else:
                    print(f"ERROR: Expected 'όσο_τέλος' at line {line}")
                    exit(0)

            else:
                print(f"ERROR: Expected 'επανάλαβε' at line {line}")
                exit(0)

    def do_stat():
        global token, line

        if (token[0] == do_token):
            token = lex()
            line = token[2]
            c_quad = nextQuad()
            sequence()

            if (token[0] == until_token):
                token = lex()
                line = token[2]
                cond = condition()
                backPatch(cond[1], c_quad)
                backPatch(cond[0], nextQuad())
            else:
                print(f"ERROR: Expected 'μέχρι' at line {line}")
                exit(0)

    def for_stat():
        global token, line

        if (token[0] == for_token):
            token = lex()
            line = token[2]

            if (token[0] == ID_token):
                for_id = token[1]
                token = lex()
                line = token[2]

                if (token[0] == assign_token):
                    token = lex()
                    line = token[2]
                    expPlace1 = expression()
                    genQuad(':=', expPlace1, '_', for_id)

                    if (token[0] == to_token):
                        token = lex()
                        line = token[2]
                        expPlace2 = expression()
                        Step = step()
                        contQuad = nextQuad()
                        
                        posExpList = makeList(nextQuad())
                        genQuad('>', Step, '0', '_')
                        negExpList = makeList(nextQuad())
                        genQuad('<', Step, '0', '_')
                        zeroExpList = makeList(nextQuad())
                        genQuad('=', Step, '0', '_')
                        
                        backPatch(posExpList, nextQuad())
                        pos_step_out = makeList(nextQuad())
                        genQuad('>=', for_id, expPlace2, '_')
                        pos_step_in = makeList(nextQuad())
                        genQuad('jump', '_', '_', '_')
                        
                        backPatch(negExpList, nextQuad())
                        neg_step_out = makeList(nextQuad())
                        genQuad('<=', for_id, expPlace2, '_')
                        neg_step_in = makeList(nextQuad())
                        genQuad('jump', '_', '_', '_')
                        
                        backPatch(zeroExpList, nextQuad())

                        if (token[0] == do_token):
                            token = lex()
                            line = token[2]
                            backPatch(pos_step_in, nextQuad())
                            backPatch(neg_step_in, nextQuad())
                            sequence()
                            
                            genQuad('+', for_id, Step, for_id)
                            genQuad('jump', '_', '_', contQuad)
                            
                            backPatch(pos_step_out, nextQuad())
                            backPatch(neg_step_out, nextQuad())

                            if (token[0] == endfor_token):
                                token = lex()
                                line = token[2]
                            else:
                                print(f"ERROR: Expected 'για_τέλος' at line {line}")
                                exit(0)
                        else:
                            print(f"ERROR: Expected 'επανάλαβε' after the condition at line {line}")
                            exit(0)
                    else:
                        print(f"ERROR: Expected 'έως' after the expression at line {line}")
                        exit(0)
                else:
                    print(f"ERROR: Expected ':=' after the variable assignment at line {line}")
                    exit(0)
            else:
                print(f"ERROR: Expected identifier (ID) after 'για' at line {line}")
                exit(0)

    def step():
        global token, line

        if (token[0] == withstep_token):
            token = lex()
            line = token[2]
            expPlace3 = expression()
            return expPlace3
        else:
            return '1'

    def print_stat():
        global token, line

        if (token[0] == write_token):
            token = lex()
            line = token[2]
            Eplace = expression()
            genQuad('out', Eplace, '_', '_')

    def input_stat():
        global token, line

        if (token[0] == read_token):
            token = lex()
            line = token[2]

            if (token[0] == ID_token):
                myid = token[1]
                token = lex()
                line = token[2]
                genQuad('inp', myid, '_', '_')
            else:
                print(f"ERROR: Expected identifier at line {line}")
                exit(0)

    def call_stat():
        global token, line

        if (token[0] == execute_token):
            token = lex()
            line = token[2]

            if (token[0] == ID_token):
                IDname = token[1]
                token = lex()
                line = token[2]
                idtail(IDname, 0)
                genQuad('call', IDname, '_', '_')
            else:
                print(f"ERROR: Expected identifier (ID) at line {line}")
                exit(0)

    def idtail(name, caller):
        global token, line

        if (token[0] == left_parenthesis_token):
            actualpars()
            
            if (caller == 1):
                w = newTemp()
                genQuad('par', w, 'RET', '_')
                genQuad('call', name, '_', '_')
                return w
        else:
            return name

    def actualpars():
        global token, line

        if (token[0] == left_parenthesis_token):
            token = lex()
            line = token[2]
            actualparlist()

            if (token[0] == right_parenthesis_token):
                token = lex()
                line = token[2]
            else:
                print(f"ERROR: Expected right parenthesis ) at line {line}")
                exit(0)

    def actualparlist():
        global token, line
        actualparitem()

        while (token[0] == comma_token):
            token = lex()
            line = token[2]
            actualparitem()

    def actualparitem():
        global token, line

        if (token[0] == modulo_token):
            token = lex()
            line = token[2]

            if (token[0] == ID_token):
                name = token[1]
                token = lex()
                line = token[2]
                genQuad('par', name, 'REF', '_')
            else:
                print(f"ERROR: Missing variable name after % at line {line}")
                exit(0)
        else:
            this_expr = expression()
            genQuad('par', this_expr, 'CV', '_')

    def condition():
        global token, line
        boolTerm1 = boolterm()
        c_true = boolTerm1[0]
        c_false = boolTerm1[1]

        while (token[0] == or_token):
            token = lex()
            line = token[2]
            backPatch(c_false, nextQuad())
            boolTerm2 = boolterm()
            c_true = merge(c_true, boolTerm2[0])
            c_false = boolTerm2[1]
        
        return c_true, c_false

    def boolterm():
        global token, line
        
        bool_factor1 = boolfactor()
        BT_true = bool_factor1[0]
        BT_false = bool_factor1[1]

        while (token[0] == and_token):
            token = lex()
            line = token[2]
            backPatch(BT_true, nextQuad())
            bool_factor2 = boolfactor()
            BT_false = merge(BT_false, bool_factor2[1])
            BT_true = bool_factor2[0]
        
        return BT_true, BT_false
            

    def boolfactor():
        global token, line

        if (token[0] == not_token):
            token = lex()
            line = token[2]

            if (token[0] == left_bracket_token):
                token = lex()
                line = token[2]
                cond = condition()
                BF_true = cond[1]
                BF_false = cond[0]

                if (token[0] == right_bracket_token):
                    token = lex()
                    line = token[2]
                else:
                    print(f"ERROR: Missing right bracket ] at line {line}")
                    exit(0)
            else:
                print(f"ERROR: Missing left bracket [ at line {line}")
                exit(0)

        elif (token[0] == left_bracket_token):
            token = lex()
            line = token[2]
            cond = condition()
            BF_true = cond[0]
            BF_false = cond[1]

            if (token[0] == right_bracket_token):
                token = lex()
                line = token[2]
            else:
                print(f"ERROR: Missing right bracket ] at line {line}")
                exit(0)
        else:
            E_place1 = expression()
            rel_op = relational_oper()
            E_place2 = expression()
            BF_true = makeList(nextQuad())
            genQuad(rel_op, E_place1, E_place2, '_')
            BF_false = makeList(nextQuad())
            genQuad('jump', '_', '_', '_')
        
        return BF_true, BF_false

    def expression():
        global token, line
        opt_sign = optional_sign()
        t1_place = term()
        
        if (opt_sign == '-'):
            w = newTemp()
            genQuad('-', '0', t1_place, w)
            t1_place = w

        while (token[0] == plus_token or token[0] == minus_token):
            plusOrMinus = add_oper()
            t2_place = term()
            w = newTemp()
            genQuad(plusOrMinus, t1_place, t2_place, w)
            t1_place = w
        
        Eplace = t1_place
        return Eplace

    def term():
        global token, line
        f1_place = factor()

        while (token[0] == mult_token or token[0] == div_token):
            mulOrDiv = mul_oper()
            f2_place = factor()
            w = newTemp()
            genQuad(mulOrDiv, f1_place, f2_place, w)
            f1_place = w
        
        Tplace = f1_place
        return Tplace

    def factor():
        global token, line

        if (token[0] == number_token):
            fact = token[1]
            token = lex()
            line = token[2]
        elif (token[0] == left_parenthesis_token):
            token = lex()
            line = token[2]
            Eplace = expression()
            fact = Eplace

            if (token[0] == right_parenthesis_token):
                token = lex()
                line = token[2]
            else:
                print(f"ERROR: Expected right parenthesis ) at line {line}")
                exit(0)

        elif (token[0] == ID_token):
            fact_temp = token[1]
            token = lex()
            line = token[2]
            fact = idtail(fact_temp, 1)
        else:
            print(f"ERROR: Expeced constant/expression/variable at line {line}")
            exit(0)
        return fact

    def relational_oper():
        global token, line

        if (token[0] == equal_token):
            rel_op = token[1]
            token = lex()
            line = token[2]
        elif (token[0] == smaller_than_token):
            rel_op = token[1]
            token = lex()
            line = token[2]
        elif (token[0] == smaller_or_equal_token):
            rel_op = token[1]
            token = lex()
            line = token[2]
        elif (token[0] == not_equal_token):
            rel_op = token[1]
            token = lex()
            line = token[2]
        elif (token[0] == greater_than_token):
            rel_op = token[1]
            token = lex()
            line = token[2]
        elif (token[0] == greater_or_equal_token):
            rel_op = token[1]
            token = lex()
            line = token[2]
        else:
            print(f"ERROR: Expected relational operator (< , > , <= , >=) at line {line}")
            exit(0)
        return rel_op

    def add_oper():
        global token, line

        if (token[0] == plus_token):
            addOp = token[1]
            token = lex()
            line = token[2]
        elif (token[0] == minus_token):
            addOp = token[1]
            token = lex()
            line = token[2]
        
        return addOp

    def mul_oper():
        global token, line

        if (token[0] == mult_token):
            oper = token[1]
            token = lex()
            line = token[2]
        elif (token[0] == div_token):
            oper = token[1]
            token = lex()
            line = token[2]
        return oper

    def optional_sign():
        global token, line

        if (token[0] == plus_token or token[0] == minus_token):
            operator = add_oper()
            return operator
        else:
            return '+'

    token = lex()
    line = token[2]
    program()

listOfScopes = []

class Argument():
    def __init__(self):
        self.name: str = ''
        self.type: str = 'Int'
        self.parMode: str = ''
    
class Variable():
    def __init__(self, var_type='Int', offset=0):
        self.type = var_type
        self.offset = offset

class SubProgram():
    def __init__(self):
        self.type = ''
        self.startQuad = 0
        self.framelenght = 0
        self.argument = []

class Parameter():
    def __init__(self):
        self.mode = ''
        self.offset = 0

class TempVar():
    def __init__(self, var_type='Int', offset=0):
        self.type = var_type
        self.offset = offset

class Entity():
    def __init__(self):
        self.name = ''
        self.type = ''
        self.variable = Variable()
        self.subprogram = SubProgram()
        self.parameter = Parameter()
        self.tempVar = TempVar()
        
class Scope():
    def __init__(self):
        self.scope_name = ''
        self.entities = []
        self.nesting_level = 0



def writeSymFile():
    global symFile, listOfScopes
    
    symFile.write("______________________________________________________________________________________________________\n\n")
    for scope in listOfScopes:
        symFile.write(f"Scope: {scope.scope_name} (Nesting Level: {scope.nesting_level})\n")
        for entity in scope.entities:
            if entity.type == 'VAR': symFile.write(f"\tEntity: {entity.name} (Type: {entity.type}\t Variable Type: {entity.variable.type}\t Offset: {entity.variable.offset})\n")
            elif entity.type == 'PARAM': symFile.write(f"\tEntity: {entity.name} (Type: {entity.type}\t Parameter Mode: {entity.parameter.mode}\t Offset: {entity.parameter.offset})\n")
            elif entity.type == 'TEMP': symFile.write(f"\tEntity: {entity.name} (Type: {entity.type}\t Temporary Variable Type: {entity.tempVar.type}\t Offset: {entity.tempVar.offset})\n")
            elif entity.type == 'SUBPR':
                symFile.write(f"\tEntity: {entity.name} (Type: {entity.type}\t Subprogram Type: {entity.subprogram.type}\t Start Quad: {entity.subprogram.startQuad})\t Frame Length: {entity.subprogram.framelenght}\n")
                for argument in entity.subprogram.argument:
                    symFile.write(f"\t\tArgument: {argument.name} (Type: {argument.type}\t Parameter Mode: {argument.parMode})\n")  
        symFile.write("\n")   
    symFile.write("______________________________________________________________________________________________________\n\n") 
    
def new_argument(object):
    global listOfScopes

    current_scope = listOfScopes[-1]
    last_entity = current_scope.entities[-1]
    subprogram = last_entity.subprogram
    subprogram.argument.append(object)

def new_entity(object):
    global listOfScopes
    
    current_scope = listOfScopes[-1]
    current_scope.entities.append(object)
    
def new_scope(name):
    global listOfScopes
    newScope = Scope()
    newScope.scope_name = name
    
    if not listOfScopes:
        newScope.nesting_level = 0
    else:
        newScope.nesting_level = listOfScopes[-1].nesting_level + 1
    listOfScopes.append(newScope)

def delete_scope():
    global listOfScopes
    deleteScope = listOfScopes.pop()
    del deleteScope

def compute_offset():
    global listOfScopes
    count = 0
    
    if listOfScopes[-1].entities:
        for entity in listOfScopes[-1].entities:
            if (entity.type == 'PARAM'  or entity.type == 'TEMP' or entity.type == 'VAR'):
                count += 1
    
    current_offset = 12 + (4 * count)
    return current_offset

def compute_startQuad():
    global listOfScopes
    
    listOfScopes[-2].entities[-1].subprogram.startQuad = nextQuad()

def compute_framelenght():
    global listOfScopes
    
    listOfScopes[-2].entities[-1].subprogram.framelenght = compute_offset()

def add_parameters():
    global listOfScopes
    
    for scope in listOfScopes[-2].entities[-1].subprogram.argument:
        entity = Entity()
        entity.name = scope.name
        entity.type = 'PARAM'
        entity.parameter.mode = scope.parMode
        entity.parameter.offset = compute_offset()
        new_entity(entity)

#######################################
#              Final Code             #
#######################################

asciiFile = open('asciiFile.asm', 'w')
asciiFile.write("          \n")

turn = 0

def search_entity(var_name):
    global listOfScopes
    
    for scope in reversed(listOfScopes):
        for entity in scope.entities:
            if entity.name == var_name:
                return (scope, entity)
    print(f"ERROR: Variable '{var_name}' not found in any scope")
    exit(0)

def gnlvcode(name):
    global listOfScopes, asciiFile
    
    asciiFile.write(f"lw t0,-4(sp)\n")
    scope, entity = search_entity(name)
    
    for i in range(scope.nesting_level, listOfScopes[-1].nesting_level):
        asciiFile.write(f"lw t0,-4(t0)\n")
    asciiFile.write(f"addi t0,t0,-{entity.variable.offset}\n")
    

def loadvr(v,r):
    global listOfScopes, asciiFile
    
    if v.isdigit():
        asciiFile.write(f"li t{r},{v}\n")
    else:
        scope, entity = search_entity(v)
        
        if scope.nesting_level == 0 and entity.type == 'VAR':
            asciiFile.write(f"lw t{r},-{entity.variable.offset}(gp)\n")
        elif scope.nesting_level == listOfScopes[-1].nesting_level and entity.type == 'VAR':
            asciiFile.write(f"lw t{r},-{entity.variable.offset}(sp)\n")
        elif scope.nesting_level == listOfScopes[-1].nesting_level and entity.type == 'PARAM' and entity.parameter.mode == 'CV':
            asciiFile.write(f"lw t{r},-{entity.parameter.offset}(sp)\n")
        elif scope.nesting_level == listOfScopes[-1].nesting_level and entity.type == 'TEMP':
            asciiFile.write(f"lw t{r},-{entity.tempVar.offset}(sp)\n")
        elif scope.nesting_level == listOfScopes[-1].nesting_level and entity.type == 'PARAM' and entity.parameter.mode == 'REF':
            asciiFile.write(f"lw t0,-{entity.parameter.offset}(sp)\n")
            asciiFile.write(f"lw t{r},(t0)\n")
        elif scope.nesting_level < listOfScopes[-1].nesting_level and entity.type == 'VAR':
            gnlvcode(v)
            asciiFile.write(f"lw t{r},(t0)\n")
        elif scope.nesting_level < listOfScopes[-1].nesting_level and entity.type == 'PARAM' and entity.parameter.mode == 'CV':
            gnlvcode(v)
            asciiFile.write(f"lw t{r},(t0)\n")
        elif scope.nesting_level < listOfScopes[-1].nesting_level and entity.type == 'PARAM' and entity.parameter.mode == 'REF':
            gnlvcode(v)
            asciiFile.write("lw t0,(t0)\n")
            asciiFile.write(f"lw t{r},(t0)\n")
        
            
def storerv(r,v):
    global listOfScopes, asciiFile
    
    scope, entity = search_entity(v)
    
    if scope.nesting_level == 0 and entity.type == 'VAR':
        asciiFile.write(f"sw t{r},-{entity.variable.offset}(gp)\n")
    elif scope.nesting_level == listOfScopes[-1].nesting_level and (entity.type == 'VAR' or entity.type == 'TEMP' or (entity.type == 'PARAM' and entity.parameter.mode == 'CV')):
        asciiFile.write(f"sw t{r},-{entity.variable.offset}(sp)\n")
    elif scope.nesting_level == listOfScopes[-1].nesting_level and entity.type == 'PARAM' and entity.parameter.mode == 'REF':
        asciiFile.write(f"lw t0,-{entity.parameter.offset}(sp)\n")
        asciiFile.write(f"sw t{r},(t0)\n")
    elif scope.nesting_level < listOfScopes[-1].nesting_level and entity.type == 'VAR' or (entity.type == 'PARAM' and entity.parameter.mode == 'CV'):
        gnlvcode(v)
        asciiFile.write(f"sw t{r},(t0)\n")
    elif scope.nesting_level < listOfScopes[-1].nesting_level and entity.type == 'PARAM' and entity.parameter.mode == 'REF':
        gnlvcode(v)
        asciiFile.write("lw t0,(t0)\n")
        asciiFile.write(f"sw t{r},(t0)\n")
    elif scope.nesting_level < listOfScopes[-1].nesting_level and entity.type == 'SUBPR' and entity.subprogram.type == 'Function':
            asciiFile.write(f"lw t0,-8(sp)\n")
            asciiFile.write(f"sw t{r},(t0)\n")

relational_operators = ['<', '>', '<=', '>=', '=', '<>']
operators = ['+', '-', '*', '/']

def final_code():
    global listOfScopes, asciiFile, quadList, turn, relational_operators, operators
    
    for i in range(len(quadList)):
        asciiFile.write(f"L{quadList[i][0]}: \n")
        
        if quadList[i][1] == 'jump':
            asciiFile.write(f"b L{quadList[i][4]}\n")
        elif quadList[i][1] == 'out':
            loadvr(quadList[i][2], 1)
            asciiFile.write("li a0,44\n")
            asciiFile.write("li a7,1\n")
            asciiFile.write("ecall\n")
        elif quadList[i][1] == 'inp':
            asciiFile.write("li a7,5\n")
            asciiFile.write("ecall\n")
            storerv(1, quadList[i][2])
        elif quadList[i][1] in relational_operators:
            loadvr(quadList[i][2], 1)
            loadvr(quadList[i][3], 2)
            if quadList[i][1] == '<': asciiFile.write(f"blt t1,t2,L{quadList[i][4]}\n")
            if quadList[i][1] == '>': asciiFile.write(f"bgt t1,t2,L{quadList[i][4]}\n")
            if quadList[i][1] == '<=': asciiFile.write(f"ble t1,t2,L{quadList[i][4]}\n")
            if quadList[i][1] == '>=': asciiFile.write(f"bge t1,t2,L{quadList[i][4]}\n")
            if quadList[i][1] == '=': asciiFile.write(f"beq t1,t2,L{quadList[i][4]}\n")
            if quadList[i][1] == '<>': asciiFile.write(f"bne t1,t2,L{quadList[i][4]}\n")
        elif quadList[i][1] in operators:
            loadvr(quadList[i][2], 1)
            loadvr(quadList[i][3], 2)
            if quadList[i][1] == '+': asciiFile.write(f"add t1,t1,t2\n")
            if quadList[i][1] == '-': asciiFile.write(f"sub t1,t1,t2\n")
            if quadList[i][1] == '*': asciiFile.write(f"mul t1,t1,t2\n")
            if quadList[i][1] == '/': asciiFile.write(f"div t1,t1,t2\n")
            storerv(1, quadList[i][4])
        elif quadList[i][1] == 'begin_block' and listOfScopes[-1].nesting_level == 0:
            asciiFile.seek(0, 0)
            asciiFile.write(f"j L{quadList[i][4]}\n")
            asciiFile.seek(0, 2)
            asciiFile.write(f"addi sp,sp,-{listOfScopes[-1].entities[-1].subprogram.framelenght}\n")
            asciiFile.write("move gp,sp\n")
        elif quadList[i][1] == 'begin_block' and listOfScopes[-1].nesting_level != 0:
            asciiFile.write("sw ra,(sp)\n")
        elif quadList[i][1] == 'end_block' and listOfScopes[-1].nesting_level != 0:
            asciiFile.write("lw ra,(sp)\n")
            asciiFile.write("jr ra\n")
        elif quadList[i][1] == 'halt':
            asciiFile.write("li a7,0\n")
            asciiFile.write("li a7,93\n")
            asciiFile.write("ecall\n")
            
            
        
    writeIntFile(intFile)           
    quadList.clear()
            
        
    
    

intFile = open('intermediateFile.int', 'w') 
symFile = open('symbolTable.sym', 'w')

syntax_an()
print("Syntax analysis completed successfully")


intFile.close()