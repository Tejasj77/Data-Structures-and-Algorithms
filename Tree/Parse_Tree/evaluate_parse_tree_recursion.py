import operator
from Parse_Tree import build_parse_tree

equation = '( ( 4 + 3 ) * 7 )'
expr_tree = build_parse_tree.buildparsetree(equation)

def evaluate(tree):
    operators = {'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.floordiv}
    left_C = tree.getleftchild()
    right_C = tree.getrightchild()

    if left_C and right_C:
        func = operators[tree.getroot()]
        return func(evaluate(left_C),evaluate(right_C))                 #move to the leftest tree
    else:
        return tree.getroot()

print(evaluate(expr_tree))
#operator.mul(operator.add(3,4),7) = 49
