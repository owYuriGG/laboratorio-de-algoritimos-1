valorCombustivel = float(input("Digite o valor do combustível: "))

distri = valorCombustivel * 0.17
etanol = valorCombustivel * 0.12
icms = valorCombustivel * 0.28
cidecofins = valorCombustivel * 0.07

valorRef = valorCombustivel - distri - etanol - icms - cidecofins
print("O valor de refinaria é de: ", valorRef)
print("Os impostos/custos inclusos no valor são: ")
print("Custo de Distribuição: ", distri)
print("Custo do etanol: ", etanol)
print("Valor do ICMS: ", icms)
print("Valor CIDE, PIS/PASEP e COFINS: ", cidecofins)
