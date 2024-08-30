import ast

from mutpy.operators.base import MutationResign, MutationOperator, AbstractUnaryOperatorDeletion


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
    
    def mutate_Eq_to_Lt(self, node):
        return ast.Lt()


class SecurityOperatorReplacement(AbstractSecurityOperatorReplacement):
    def should_mutate(self, node):
        return not isinstance(node.parent, ast.AugAssign)

