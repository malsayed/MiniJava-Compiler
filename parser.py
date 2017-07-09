from cfg.single_or_array import *
from cfg.expression import *
from cfg.exp import *
from cfg.exp_only_one import *
from cfg.statement import *
from cfg.st import *
from cfg.type import *
from cfg.md import *
from cfg.method_declaration import *
from cfg.vd import *
from cfg.var_declaration import *
from cfg.cd import *
from cfg.class_declaration import *
from cfg.dot import *
from cfg.main_class import *
from cfg.goal import *
from cfg.parameters import *
from cfg.parameters_list import *
from cfg.epsilon import *
from cfg.Else import *
from cfg.operations import *
from cfg.new_object import *
from cfg.extends import *
from cfg.expression_recursion_fix import *
import LexicalAnalyzer


def parse_goal(queue):

    m = parse_main_class(queue)
    c = parse_cd(queue)
    g = Goal(m, c)

    return g


def parse_main_class(queue):

    validate(queue, "class")

    i = parse_identifier(queue)

    validate(queue, "{")
    validate(queue, "public")
    validate(queue, "static")
    validate(queue, "void")
    validate(queue, "main")
    validate(queue, "(")
    validate(queue, "String")
    validate(queue, "[")
    validate(queue, "]")

    i2 = parse_identifier(queue)

    validate(queue, ")")
    validate(queue, "{")

    s = parse_statement(queue)

    # if type(s) == Epsilon:
    #     raise Exception("ERROR: Code Not Complete: Expected a Statement")

    validate(queue, "}")
    validate(queue, "}")

    m = MainClass(i, i2, s)

    return m


def parse_cd(queue):

    c = parse_class_declaration(queue)

    if type(c) == Epsilon:
        cd = Epsilon()
        return cd

    else:
        cd = parse_cd(queue)
        final_cd = CD(c, cd)
        return final_cd


def parse_class_declaration(queue):

    if len(queue) == 0:
        e = Epsilon()
        return e

    else:

        validate(queue, "class")
        i = parse_identifier(queue)
        ex = parse_extends(queue)

        validate(queue, "{")

        vd = parse_vd(queue)
        md = parse_md(queue)

        validate(queue, "}")

        c = ClassDeclaration(i, ex, vd, md)

        return c


def parse_extends(queue):
    if len(queue) == 0:
        print("ERROR: Code not complete")
        raise SystemExit

    if queue[0][1] == "{":
        e = Epsilon()
        return e

    else:
        validate(queue, "extends")
        i = parse_identifier(queue)
        e = Extends(i)

        return e


def parse_vd(queue):

    v = parse_variable_declaration(queue)

    if type(v) == Epsilon:
        e = Epsilon()
        return e
    else:
        vd = parse_vd(queue)
        final_vd = VD(v, vd)
        return final_vd


def parse_variable_declaration(queue):

    ty = parse_type(queue)

    if type(ty) == Epsilon:
        e = Epsilon()
        return e
    else:

        i = parse_identifier(queue)

        validate(queue, ";")

        v = VarDeclaration(ty, i)

        return v


def parse_type(queue):
    # TYPE Check

    if len(queue) == 0:
        print("ERROR: Code not complete: Expected a data type")
        raise SystemExit
    else:
        value = queue[0][1]
        if value == DataType.INT:
            d = DataType.INT
            queue.pop(0)

        elif value == DataType.BOOL:
            d = DataType.BOOL
            queue.pop(0)

        elif value == DataType.CHAR:
            d = DataType.CHAR
            queue.pop(0)

        elif value == DataType.FLOAT:
            d = DataType.FLOAT
            queue.pop(0)

        elif value == DataType.STRING:
            d = DataType.STRING
            queue.pop(0)

        else:
            e = Epsilon()
            return e

        # End of TYPE check
        # BRACKET Check

        if len(queue) == 0:
            print("ERROR: Code not complete")
            raise SystemExit

        else:

            if len(queue) < 2:
                print("ERROR: Code not complete at line", queue[0][0])
                raise SystemExit

            else:
                value = queue[0][1] + queue[1][1]

                if value == Bracket.BRACKET:
                    b = Bracket.BRACKET
                    queue.pop(0)
                    queue.pop(0)

                else:
                    b = Bracket.EPSILON

        ty = Type(d, b)
        return ty


def parse_md(queue):

    m = parse_method_declaration(queue)

    if type(m) == Epsilon:
        e = Epsilon()
        return e
    else:
        md = parse_md(queue)
        final_md = MD(m, md)
        return final_md


def parse_method_declaration(queue):

    if len(queue) == 0:
        print("ERROR: Code not complete")
        raise SystemExit
    
    else:
        value = queue[0][1]

        if value == Modifier.PRIVATE:
            mod = Modifier.PRIVATE
            queue.pop(0)

        elif value == Modifier.PUBLIC:
            mod = Modifier.PUBLIC
            queue.pop(0)

        else:
            e = Epsilon()
            return e

        ty = parse_type(queue)

        if type(ty) == Epsilon:
            print("ERROR: Expected a data type found: \"" + queue[0][1] + "\" at line", queue[0][0])
            raise SystemExit
        
        i = parse_identifier(queue)

        validate(queue, "(")

        p = parse_parameters(queue)

        validate(queue, ")")
        validate(queue, "{")

        vd = parse_vd(queue)

        st = parse_st(queue)

        validate(queue, "return")

        exp = parse_expression(queue)
        throw_exception_expression(exp)

        validate(queue, ";")
        validate(queue, "}")

        m = MethodDeclaration(mod, ty, i, p, vd, st, exp)
        return m


def parse_parameters(queue):

    ty = parse_type(queue)

    if type(ty) == Epsilon:
        e = Epsilon()
        return e

    i = parse_identifier(queue)
    pl = parse_parameters_list(queue)

    p = Parameters(ty, i, pl)
    return p


def parse_parameters_list(queue):

    if len(queue) == 0:
        print("ERROR: Code not complete. Expected: )")
        raise SystemExit
    
    value = queue[0][1]

    if value != ",":
        e = Epsilon()
        return e

    queue.pop(0)

    ty = parse_type(queue)
    if type(ty) == Epsilon:
        print("ERROR: Expected a data type")
        raise SystemExit

    i = parse_identifier(queue)
    pl = parse_parameters_list(queue)

    final_pl = ParametersList(ty, i, pl)
    return final_pl


def parse_st(queue):

    s = parse_statement(queue)

    if type(s) == Epsilon:
        e = Epsilon()
        return e
    else:
        st = parse_st(queue)
        final_st = ST(s, st)
        return final_st


def parse_statement(queue):

    if len(queue) == 0:
        print("ERROR: Code Not Complete: Expected a Statement")
        raise SystemExit
    else:
        value = queue[0][1]

        if value == "{":
            queue.pop(0)

            st = parse_st(queue)
            validate(queue, "}")
            s = Statement1(st)
            return s

        elif value == "if":
            queue.pop(0)
            validate(queue, "(")

            exp = parse_expression(queue)
            throw_exception_expression(exp)

            validate(queue, ")")

            s = parse_statement(queue)

            el = parse_else(queue)

            s2 = Statement2(exp, s, el)
            return s2

        elif value == "while":
            queue.pop(0)
            validate(queue, "(")

            exp = parse_expression(queue)
            throw_exception_expression(exp)

            validate(queue, ")")

            s = parse_statement(queue)

            s3 = Statement3(exp, s)
            return s3

        elif value == "System.out.println":
            queue.pop(0)

            validate(queue, "(")

            exp = parse_expression(queue)
            throw_exception_expression(exp)

            validate(queue, ")")
            validate(queue, ";")

            s4 = Statement4(exp)
            throw_exception_expression(exp)

            return s4

        elif LexicalAnalyzer.is_id(value):
            i = parse_identifier(queue)
            si = parse_single_or_array(queue)

            s5 = Statement5(i, si)
            return s5

        else:
            e = Epsilon()
            return e


def parse_else(queue):
    if len(queue) == 0:
        print("ERROR: Code Not Complete")
        raise SystemExit
    else:
        value = queue[0][1]

        if value == "else":
            queue.pop(0)
            s = parse_statement(queue)

            el = Else(s)
            return el

        else:
            e = Epsilon()
            return e


def parse_single_or_array(queue):

    if len(queue) == 0:
        print("ERROR: Code Not Complete: Expected an operator")
        raise SystemExit
    
    else:

        value = queue[0][1]

        if value == "=":
            queue.pop(0)
            exp = parse_expression(queue)
            throw_exception_expression(exp)

            validate(queue, ";")

            si = SingleOrArray1(exp)
            return si

        elif value == "[":
            queue.pop(0)
            exp = parse_expression(queue)
            throw_exception_expression(exp)

            validate(queue, "]")
            validate(queue, "=")

            exp2 = parse_expression(queue)

            validate(queue, ";")

            si = SingleOrArray2(exp, exp2)
            return si

        else:
            print("ERROR: Code Not Complete: Expected an operator at line", queue[0][0])
            raise SystemExit


def parse_expression(queue):
    if len(queue) == 0:
        print("ERROR: Code Not Complete: Expected an expression")
        raise SystemExit
    
    else:
        value = queue[0][1]

        if LexicalAnalyzer.is_integer_literal(value):
            queue.pop(0)
            e_rec = parse_expression_recursion_fix(queue)

            e1 = Expression1(value, e_rec)
            return e1

        elif value == "true":
            queue.pop(0)
            e_rec = parse_expression_recursion_fix(queue)

            e2 = Expression2(e_rec)
            return e2

        elif value == "false":
            queue.pop(0)
            e_rec = parse_expression_recursion_fix(queue)

            e3 = Expression3(e_rec)
            return e3

        elif value == "this":
            queue.pop(0)
            e_rec = parse_expression_recursion_fix(queue)

            e5 = Expression5(e_rec)
            return e5

        elif value == "new":
            queue.pop(0)
            n = parse_new_object(queue)
            e_rec = parse_expression_recursion_fix(queue)

            e6 = Expression6(n, e_rec)
            return e6

        elif value == "!":
            queue.pop(0)
            exp = parse_expression(queue)
            throw_exception_expression(exp)

            e_rec = parse_expression_recursion_fix(queue)

            e7 = Expression7(exp, e_rec)
            return e7

        elif value == "(":
            queue.pop(0)

            exp = parse_expression(queue)
            throw_exception_expression(exp)

            validate(queue, ")")

            e_rec = parse_expression_recursion_fix(queue)

            e8 = Expression8(exp, e_rec)
            return e8

        elif LexicalAnalyzer.is_id(value):
            i = parse_identifier(queue)
            e_rec = parse_expression_recursion_fix(queue)

            e4 = Expression4(i, e_rec)
            return e4

        else:
            e = Epsilon()
            return e


def parse_expression_recursion_fix(queue):

    o = parse_operations(queue)

    if type(o) == Epsilon:
        e = Epsilon()
        return e

    else:
        e_rec = parse_expression_recursion_fix(queue)
        final_e_rec = ExpressionRecursionFix(o, e_rec)
        return final_e_rec


def parse_new_object(queue):

    if len(queue) == 0:
        print("ERROR: Code Not Complete: Expected an Object")
        raise SystemExit
    
    else:
        value = queue[0][1]

        if value == "int":
            queue.pop(0)
            validate(queue, "[")

            exp = parse_expression(queue)
            throw_exception_expression(exp)

            validate(queue, "]")

            n = NewObject1(exp)
            return n

        elif LexicalAnalyzer.is_id(value):
            i = parse_identifier(queue)

            validate(queue, "(")
            validate(queue, ")")

            n = NewObject2(i)
            return n

        else:
            print("ERROR: Code Not Complete: Expected an Object at line", queue[0][0])
            raise SystemExit
        

def parse_operations(queue):

    if len(queue) == 0:
        print("ERROR: Code Not Complete: Expected an operator")
        raise SystemExit
    
    else:
        value = queue[0][1]

        # U can switch to the class use
        if value == BinaryOperations.AND or value == BinaryOperations.LESS_THAN\
                or value == BinaryOperations.PLUS or value == BinaryOperations.MINUS\
                or value == BinaryOperations.MULTIPLY:

            queue.pop(0)

            exp = parse_expression(queue)
            throw_exception_expression(exp)

            o = Operations1(value, exp)
            return o

        elif value == "[":

            queue.pop(0)
            exp = parse_expression(queue)
            validate(queue, "]")

            o = Operations2(exp)
            return o

        elif value == ".":

            queue.pop(0)
            dot = parse_dot(queue)

            o = Operations3(dot)
            return o

        else:
            e = Epsilon()
            return e


def parse_dot(queue):
    if len(queue) == 0:
        print("ERROR: Code Not Complete: Expected a method call")
        raise SystemExit

    else:
        value = queue[0][1]

        if value == "length":
            queue.pop(0)
            d = Dot1()
            return d

        elif LexicalAnalyzer.is_id(value):
            i = parse_identifier(queue)
            validate(queue, "(")

            exp_one = parse_exp_only_one(queue)
            exp = parse_exp(queue)

            validate(queue, ")")

            d = Dot2(i, exp_one, exp)
            return d

        else:
            print("ERROR: Code Not Complete: Expected a method call at line", queue[0][0])
            raise SystemExit
        

def parse_exp_only_one(queue):

    exp = parse_expression(queue)

    if type(exp) == Epsilon:
        e = Epsilon()
        return e
    else:
        e_one = ExpOnlyOne(exp)
        return e_one


def parse_exp(queue):

    ex = parse_expression(queue)

    if type(ex) == Epsilon:
        e = Epsilon()
        return e
    else:
        exp = parse_exp(queue)
        final_exp = Exp(ex, exp)
        return final_exp


def parse_identifier(queue):

    if len(queue) == 0:
        print("ERROR: Expected an identifier")
        raise SystemExit
    
    token = queue.pop(0)

    if not LexicalAnalyzer.is_id(token[1]):
        print("Not a correct identifier at line", token[0])
        raise SystemExit
    
    if token[1] == "public" or token[1] == "static" \
            or token[1] == "void" or token[1] == "main" \
            or token[1] == "int" or token[1] == "float" \
            or token[1] == "if" or token[1] == "else" or token[1] == "while" \
            or token[1] == "String" or token[1] == "char" or token[1] == "boolean" \
            or token[1] == "extends" or token[1] == "return" or token[1] == "new" \
            or token[1] == "this" or token[1] == "true" or token[1] == "false" or token[1] == "class":
                print("Using keyword as an identifier at line", token[0])
                raise SystemExit
    
    return token[1]


def parse_integer_literal(queue):

    if len(queue) == 0:
        print("ERROR: Expected an integer")
        raise SystemExit
    
    token = queue.pop(0)

    if not LexicalAnalyzer.is_integer_literal(token[1]):
        print("ERROR: Not an integer at line", token[0])
        raise SystemExit
    
    return token[1]


def validate(queue, expected_value):

    if len(queue) == 0:
        print("ERROR: Code Not Complete: expected \"" + expected_value + "\"")
        raise SystemExit
    
    else:
        value = queue.pop(0)

        if value[1] != expected_value:
            print("ERROR: Expected \"" + expected_value + "\" found: \"" + value[1] + "\" at line", value[0])
            raise SystemExit


def check_if_epsilon(queue, expected_value):

    if len(queue) == 0 or queue[0][1] != expected_value:
        return True
    else:
        return False


def throw_exception_expression(expression):

    if type(expression) == Epsilon:
        print("ERROR: Expected an expression")
        raise SystemExit
    
files = LexicalAnalyzer.open_file()
lex = LexicalAnalyzer.tokenize(files[0], files[1])
goal = parse_goal(lex)

print(goal.get_value(), "\nCode Executed Successfully")
