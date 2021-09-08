def maxProfitWithKTransactions(prices, k):
	if len(prices)==0:
		return 0
	result=[]
	for i in range(len(prices)):
		lis=[]
		for j in range(k+1):
			lis.append(0)
		result.append(lis)
	#計算每個sell、buy組合，找出最大交易值，並利用list的index判斷經過多少次交易。 
	for sell in range(1,len(prices)):
		for transaction in range(1,k+1):
			max_profit=0
			for buy in range(sell):
				max_profit=max(max_profit,prices[sell]-prices[buy]+result[buy][transaction-1])
			result[sell][transaction]=max(max_profit,result[sell-1][transaction])
	return result[len(prices)-1][k]
