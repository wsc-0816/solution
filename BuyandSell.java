public class BuyandSell{
	//Take O(n) time,and O(1) space
	/*
	Say you have an array for which the ith element 
	is the price of a given stock on day i. 
	If you were only permitted to complete at most one transaction 
	(ie, buy one and sell one share of the stock), 
	design an algorithm to find the maximum profit.
	*/
	public int maxProfit(int[] prices){
		if (prices.length< 2) return 0;
		int profit = 0;
		int current = prices[0];
		for (int i = 1; i < prices.length;i ++){
			current= Math.min(current,prices[i]);
			profit = Math.max(profit,prices[i] - current);

		}
	return profit;
	}
	public static void main(String[] args){
		BuyandSell test = new BuyandSell();
		int[] prices= {8,2,7,1,5,6,4,3};
		//int[] prices= {7,1};
		int result = test.maxProfit(prices);
		System.out.println(result);
	}

}