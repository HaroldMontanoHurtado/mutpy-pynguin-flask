import ast

from mutpy.operators.base import MutationOperator, AbstractUnaryOperatorDeletion, copy_node


class ConditionalOperatorDeletion(AbstractUnaryOperatorDeletion):
    def get_operator_type(self):
        return ast.Not

    def mutate_NotIn(self, node):
        return ast.In()


class ConditionalOperatorInsertion(MutationOperator):
    def negate_test(self, node):
        not_node = ast.UnaryOp(op=ast.Not(), operand=node.test)
        node.test = not_node
        return node

    @copy_node
    def mutate_While(self, node):
        return self.negate_test(node)

    @copy_node
    def mutate_If(self, node):
        return self.negate_test(node)

    def mutate_In(self, node):
        return ast.NotIn()


class LogicalConnectorReplacement(MutationOperator):
    def mutate_And(self, node):
        return ast.Or()

    def mutate_Or(self, node):
        return ast.And()


class LogicalOperatorDeletion(AbstractUnaryOperatorDeletion):
    def get_operator_type(self):
        return ast.Invert


class LogicalOperatorReplacement(MutationOperator):
    def mutate_BitAnd(self, node):
        return ast.BitOr()

    def mutate_BitOr(self, node):
        return ast.BitAnd()

    def mutate_BitXor(self, node):
        return ast.BitAnd()

    def mutate_LShift(self, node):
        return ast.RShift()

    def mutate_RShift(self, node):
        return ast.LShift()


class RelationalOperatorReplacement(MutationOperator):
    def mutate_Lt(self, node): # less that -> great that
        return ast.Gt()

    def mutate_Lt_to_LtE(self, node): # less that -> less or equal
        return ast.LtE()

    def mutate_Gt(self, node): # great that
        return ast.Lt()

    def mutate_Gt_to_GtE(self, node): # great that -> great or equal
        return ast.GtE()

    def mutate_LtE(self, node): # less or equal -> great or equal
        return ast.GtE()

    def mutate_LtE_to_Lt(self, node): # less or equal -> less that
        return ast.Lt()

    def mutate_GtE(self, node): # great or equal -> less or equal
        return ast.LtE()

    def mutate_GtE_to_Gt(self, node): # great or equal -> great that
        return ast.Gt()

    def mutate_Eq(self, node): # equal -> not equal
        return ast.NotEq()

    def mutate_NotEq(self, node): # not equal -> equal
        return ast.Eq()
