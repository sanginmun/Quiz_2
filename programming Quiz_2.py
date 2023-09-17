# 환율표 (1달러 = 1320원, 1엔 = 950원, 1위안 = 182원)
exchange_rates = {
    'USD': 1320,
    'JPY': 950,
    'CNY': 182
}

# 가지고 있는 돈 (13달러, 200엔, 13위안)
money = {
    'USD': 13,
    'JPY': 200,
    'CNY': 13
}

# 환율을 이용하여 한화로 변환
total_krw = sum(money[currency] * rate for currency, rate in exchange_rates.items())

# 결과 출력
print(f"철수가 가지고 있는 돈의 원화 가치는  {total_krw} 원 입니다.")
