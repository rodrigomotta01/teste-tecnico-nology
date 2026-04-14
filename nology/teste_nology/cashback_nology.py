from decimal import Decimal

class Cliente():
    @staticmethod
    def calc_cashback(valor_compra, desconto):
        valor_compra = Decimal(valor_compra)
        desconto = Decimal(desconto)

        if valor_compra > Decimal('500'):
            return ((valor_compra - desconto) * Decimal('0.05')) * Decimal('2')
        else:
            return (valor_compra - desconto) * Decimal('0.05')
    
class ClienteVIP(Cliente):
    @classmethod
    def calc_cashback(cls, valor_compra, desconto):
        return super().calc_cashback(valor_compra, desconto) * Decimal('1.10')

