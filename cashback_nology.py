class Cliente():
    @staticmethod
    def calc_cashback(valor_compra, desconto):
        if valor_compra > 500:
            return ((valor_compra - desconto) * 0.05) * 2
        else:
            return (valor_compra - desconto) * 0.05
    
class ClienteVIP(Cliente):
    @classmethod
    def calc_cashback(classe, valor_compra, desconto):
        return super().calc_cashback(valor_compra, desconto) * 1.10

valor_compra = float(input("Digite o valor da compra: "))
desconto = float(input("Digite o valor do desconto(em %): ")) * valor_compra / 100
valor_final = Cliente.calc_cashback(valor_compra, desconto)
print(f"O valor de cashback é R$ {valor_final:.2f}")
valor_final_vip = ClienteVIP.calc_cashback(valor_compra, desconto)
print(f"O valor de cashback vip é R$ {valor_final_vip:.2f}")