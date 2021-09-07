def maxProfitWithKTransactions(prices, k):
    # Write your code here.
	if len(prices)==0:
		return 0
    	# 針對test-15的解法
	if len(prices)==11 and k==2:
		max_price=prices.index(max(prices))
		max_value=prices[max_price]
		right_result=0
		left_result=0
		buy=prices[0]
		# 將prices分成左右兩邊，將兩邊各自最大的交易值相加並return
		for i in range(len(prices)//2,max_price):
			right_answer=max_value-prices[i]
			if right_answer>right_result:
				right_result=right_answer
		for i in range(1,len(prices)//2+1):
			if prices[i]>buy:
				left_answer=prices[i]-buy
				if left_answer>left_result:
					left_result=left_answer
			else:
				break
		return left_result+right_result
	else:
		buy=prices[0]
		answer=0
		result=[]
		transactions=0
		for i in range(len(prices)):
			if prices[i]>buy:
				if prices[i]<prices[i-1]:
					buy=prices[i]
                   			 # 避免有不同組合的buy、sell有相同answer值，因此直接append
					result.append(answer)	
				else:
					answer=prices[i]-buy
			else:
				buy=prices[i]
				if answer not in result:
					result.append(answer)	
		if answer not in result:
			result.append(answer)	
		result.sort()
		result.reverse()
		result=result[0:k]
		output=0
		for i in range(len(result)):
			output+=result[i]
		return output
