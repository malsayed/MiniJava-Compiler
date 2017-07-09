import re


def is_eol(string):
    return re.fullmatch("[\r\n~]", string) is not None


def is_left_brace(string):
    return string == "{"


def is_right_brace(string):
    return string == "}"


def is_left_parenthesis(string):
    return string == "("


def is_right_parenthesis(string):
    return string == ")"


def is_left_bracket(string):
    return string == "["


def is_right_bracket(string):
    return string == "]"


def is_comma(string):
    return string == ","


def is_semicolon(string):
    return string == ";"


def is_period(string):
    return string == "."


def is_exclamation(string):
    return string == "!"


def is_equals(string):
    return string == "="


def is_and(string):
    return string == "&&"


def is_minus(string):
    return string == "-"


def is_asterisk(string):
    return string == "*"


def is_less_than(string):
    return string == "<"


def is_greater_than(string):
    return string == ">"


def is_if(string):
    return string == "if"


def is_int(string):
    return string == "int"


def is_else(string):
    return string == "else"


def is_main(string):
    return string == "main"


def is_this(string):
    return string == "this"


def is_id(string):

    if string == "public" or string == "static" \
            or string == "void" or string == "main" \
            or string == "int" or string == "float" \
            or string == "if" or string == "else" or string == "while" \
            or string == "String" or string == "char" or string == "boolean" \
            or string == "extends" or string == "return" or string == "new" \
            or string == "this" or string == "true" or string == "false" or string == "class":
                return False
    
    return re.fullmatch("[a-zA-Z$_](\\w|\$)*", string) is not None


def is_true(string):
    return string == "true"


def is_false(string):
    return string == "false"


def is_while(string):
    return string == "while"


def is_length(string):
    return string == "length"


def is_public(string):
    return string == "public"


def is_return(string):
    return string == "return"


def is_static(string):
    return string == "static"


def is_new(string):
    return string == "new"


def is_string(string):
    return string == "String"


def is_float(string):
    return string == "float"


def is_character(string):
    return string == "char"


def is_boolean(string):
    return string == "boolean"


def is_extends(string):
    return string == "extends"


def is_print(string):
    return string == "System`out`println"


def is_comment(string):
    return re.fullmatch("//.+", string) is not None


def is_comment_block(string):
    return re.fullmatch("/\*.+\*/", string) is not None


def is_float_literal(string):
    return re.fullmatch('\\d+\.\\d+', string) is not None


def is_string_literal(string):
    return re.fullmatch('".*"', string) is not None


def is_void(string):
    return string == "void"


def is_class(string):
    return string == "class"


def is_integer_literal(string):
    return re.fullmatch("\\d+", string) is not None


def is_a_char(string):
    return re.fullmatch("'.'", string) is not None


def is_plus(string):
    return string == "+"


def is_comment_block_opening(string):
    return string == "/*"


def is_comment_block_closing(string):
    return string == "*/"


def fix_no_spaces_and_split(string):

    list1 = re.findall('"[^"]*"|\'[^\']\'|/\\*[^*]*\\*+(?:[^/*][^*]*\\*+)*/|//[^\\n]*\\n|[^/]\*[^/]', string)

    string = string.replace("System.out.println", "System`out`println", )
    string = string.replace("+", " + ", )
    string = string.replace("-", " - ", )
    string = string.replace("=", " = ", )
    string = string.replace(";", " ; ", )
    string = string.replace("{", " { ", )
    string = string.replace("}", " } ", )
    string = string.replace("[", " [ ", )
    string = string.replace("]", " ] ", )
    string = string.replace("(", " ( ", )
    string = string.replace(")", " ) ", )
    string = string.replace(".", " . ", )

    for old in list1:
        if re.fullmatch("[^/]\*[^/]", old) is not None:
            new = re.sub("\*", " * ", old)
        else:
            new = re.sub("[ \n]", "@", old)
        old = re.sub("\*", "\\*", old)
        string = re.sub(old, new, string)

    string = string.replace("\n", " ~ ", )
    temp = string.split()
    final_split = []

    for words in temp:
        final_split.append(re.sub("@", " ", words))

    return final_split


def tokenize(input_file, output_file):

    data = input_file.read()

    tokens = fix_no_spaces_and_split(data)

    #print(tokens, "\n")

    lexicon = []
    line_num = 1
    lexicon_numbered = []

    for token in tokens:
        if is_int(token):
            lexicon.append(("<INT>", token))

        elif is_equals(token):
            lexicon.append(("<EQUALS>", token))

        elif is_float_literal(token):
            lexicon.append(("<FLOAT_LITERAL>", token))

        elif is_integer_literal(token):
            lexicon.append(("<INTEGER_LITERAL>", token))

        elif is_semicolon(token):
            lexicon.append(("<SEMICOLON>", token))

        elif is_float(token):
            lexicon.append(("<FLOAT>", token))

        elif is_comma(token):
            lexicon.append(("<COMMA>", token))

        elif is_and(token):
            lexicon.append(("<AND>", token))

        elif is_asterisk(token):
            lexicon.append(("<ASTERISK>", token))

        elif is_boolean(token):
            lexicon.append(("<BOOLEAN>", token))

        elif is_character(token):
            lexicon.append(("<CHARACTER>", token))

        elif is_class(token):
            lexicon.append(("<CLASS>", token))

        elif is_comment(token):
            lexicon.append(("<COMMENT>", token))

        elif is_comment_block(token):
            lexicon.append(("<COMMENT_BLOCK>", token))

        elif is_else(token):
            lexicon.append(("<ELSE>", token))

        elif is_eol(token):
            #lexicon.append(("<EOL>", "\\n"))
            line_num += 1

        elif is_exclamation(token):
            lexicon.append(("<EXCLAMATION>", token))

        elif is_extends(token):
            lexicon.append(("<EXTENDS>", token))

        elif is_false(token):
            lexicon.append(("<FALSE>", token))

        elif is_greater_than(token):
            lexicon.append(("<GREATER_THAN>", token))

        elif is_if(token):
            lexicon.append(("<IF>", token))

        elif is_left_bracket(token):
            lexicon.append(("<LEFT_BRACKET>", token))

        elif is_left_brace(token):
            lexicon.append(("<LEFT_BRACE>", token))

        elif is_left_parenthesis(token):
            lexicon.append(("<LEFT_PARENTHESIS>", token))

        elif is_length(token):
            lexicon.append(("<LENGTH>", token))

        elif is_less_than(token):
            lexicon.append(("<LESS_THAN>", token))

        elif is_main(token):
            lexicon.append(("<MAIN>", token))

        elif is_minus(token):
            lexicon.append(("<MINUS>", token))

        elif is_new(token):
            lexicon.append(("<NEW>", token))

        elif is_period(token):
            lexicon.append(("<PERIOD>", token))

        elif is_plus(token):
            lexicon.append(("<PLUS>", token))

        elif is_print(token):
            lexicon.append(("<PRINT>", "System.out.println"))

        elif is_public(token):
            lexicon.append(("<PUBLIC>", token))

        elif is_return(token):
            lexicon.append(("<RETURN>", token))

        elif is_right_brace(token):
            lexicon.append(("<RIGHT_BRACE>", token))

        elif is_right_bracket(token):
            lexicon.append(("<RIGHT_BRACKET>", token))

        elif is_right_parenthesis(token):
            lexicon.append(("<RIGHT_PARENTHESIS>", token))

        elif is_static(token):
            lexicon.append(("<STATIC>", token))

        elif is_string(token):
            lexicon.append(("<STRING>", token))

        elif is_this(token):
            lexicon.append(("<THIS>", token))

        elif is_true(token):
            lexicon.append(("<TRUE>", token))

        elif is_void(token):
            lexicon.append(("<VOID>", token))

        elif is_while(token):
            lexicon.append(("<WHILE>", token))

        elif is_a_char(token):
            lexicon.append(("<A_CHAR>", token))

        elif is_string_literal(token):
            lexicon.append(("<STRING_LITERAL>", token))

        elif is_id(token):
            lexicon.append(("<ID>", token))

        elif is_comment_block_opening(token):
            lexicon.append(("<COMMENT_L>", token))

        elif is_comment_block_closing(token):
            lexicon.append(("<COMMENT_R>", token))

        else:
            lexicon.append(("<INVALID>", token))

        if not is_eol(token):
            if token == "System`out`println":
                token = "System.out.println"

            lexicon_numbered.append((line_num, token))

    output_string = ""

    for lexeme in lexicon:
        output_string = output_string + " : ".join(lexeme) + "\n"

    #print(output_string)

    output_file.write(output_string)

    return lexicon_numbered


def open_file(file_name_in="input.txt", file_name_out="output.txt"):
    input_f = open(file_name_in, "r")

    output_f = open(file_name_out, "w")
    files = (input_f, output_f)

    return files

f = open_file()
l = tokenize(f[0], f[1])
