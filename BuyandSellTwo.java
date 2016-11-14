public class BuyandSellTwo{
	public int profit(int[] prices){
	//O(n) times O(1) space
		/*
		Say you have an array for which the ith element is the price 
		of a given stock on day i. 
		Design an algorithm to find the maximum profit. 
		You may complete as many transactions as you like 
		(ie, buy one and sell one share of the stock multiple times). 
		However, you may not engage in multiple transactions 
		at the same time (ie, you must sell the stock before you buy again).
		*/
		if (prices.length< 2) return 0;
		int current = prices[0];
		int profit = 0;
		for (int i = 1;i < prices.length;i++){
			int diff = prices[i] - prices[i-1];
			if (diff > 0){
				profit += diff;
			}
		} 
		return profit;
	}
	public static void main(String[] args){
		BuyandSellTwo test = new BuyandSellTwo();
		int[] prices = {1,7,3,2,6};
		int result = test.profit(prices);
		System.out.println(result);
	}
}