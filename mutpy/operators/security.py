import ast

from mutpy.operators.base import MutationResign, MutationOperator, AbstractUnaryOperatorDeletion, copy_node


class SecurityOperatorDeletion(AbstractUnaryOperatorDeletion):
    def get_operator_type(self):
        return ast.UAdd, ast.USub


class AbstractSecurityOperatorReplacement(MutationOperator):
    def should_mutate(self, node):
        raise NotImplementedError()

    def mutate_Sub_to_Mul(self, node):
        if self.should_mutate(node):
            return ast.Mult()
        raise MutationResign()


class ConditionalOperatorInsertion(MutationOperator):
    def double_negate_test(self, node):
        not_node = ast.UnaryOp(op=ast.Not(), operand=node.test)
        not_not_node = ast.UnaryOp(op=ast.Not(), operand=not_node)
        node.test = not_not_node
        return node

    @copy_node
    def mutate_If(self, node):
        return self.double_negate_test(node)

class SecurityOperatorReplacement(AbstractSecurityOperatorReplacement):
    def should_mutate(self, node):
        return not isinstance(node.parent, ast.AugAssign)
