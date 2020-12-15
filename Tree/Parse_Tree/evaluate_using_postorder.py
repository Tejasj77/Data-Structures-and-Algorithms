import operator
from Parse_Tree import build_parse_tree

equation = '( ( 4 + 3 ) * 7 )'
expr_tree = build_parse_tree.buildparsetree(equation)

def postordertraversal(tree):
    operators = {'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.floordiv}
    res1 = None
    res2 = None

    if tree:
        res1 = postordertraversal(tree.getleftchild())
        res2 = postordertraversal(tree.getrightchild())

        if res1 and res2:
            return operators[tree.getroot()](res1,res2)
        else:
            return tree.getroot()

print(postordertraversal(expr_tree))