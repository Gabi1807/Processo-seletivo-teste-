# Vetor com o faturamento diário
faturamento_diario = [31490.7866, 37277.94, 37708.4303, 0.0, 0.0, 17934.2269, 0.0, 6965.1262, 24390.9374, 14279.6481, 0.0, 0.0, 39807.6622, 27261.6304, 39775.6434, 29797.6232, 17216.5017, 0.0, 0.0, 12974.2, 28490.9861, 8748.0937, 8889.0023, 17767.5583, 0.0, 0.0, 3071.3283, 48275.2994, 10299.6761, 39874.1073]

# Menor valor de faturamento
menor_faturamento = min(faturamento_diario)
print("Menor faturamento diário: R$ {:.2f}".format(menor_faturamento))

# Maior valor de faturamento
maior_faturamento = max(faturamento_diario)
print("Maior faturamento diário: R$ {:.2f}".format(maior_faturamento))

# Média mensal de faturamento
media_mensal = sum(faturamento_diario) / len(faturamento_diario)

# Número de dias com faturamento acima da média mensal
dias_acima_media = sum(1 for f in faturamento_diario if f > media_mensal)
print("Número de dias com faturamento acima da média mensal: {}".format(dias_acima_media))
