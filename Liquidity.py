#This algorithm calculates CPMMs price impact based on influx of liquidity


ETH_PRICE = 3200
INITIAL_PAIR_LIQUIDITY_ETH = X0 = 40  # This represents the initial liquidity in ETH added to the pool
INITIAL_PAIR_LIQUIDITY_TOKENS = Y0 = 17680000000  # This represents the initial liquidity of native token added to the pool
BUY_PRESSURE_ETH = B = 1 #This indicates the new buy pressure in ETH
PRICE_TARGET = PT = 0.000022
MARKET_CAP_TARGET = MCT = 750000
CIRCULATING_SUPPLY = CS = 100000000000


import math

#PHASE 1: Calculate the initial constant product of the liquidity pool and derive the initial price of the token
#To find pool related information, enter your CA here: https://etherscan.io/token/ADD_TOKEN_CONTRACT_HERE#balances and look for the biggest pool

K = X0 * Y0 #From this we derive the constant, where K0 is the ETH amount, and Y0 is the token amount
INITIAL_PRICE = Z0 = (X0/Y0)*ETH_PRICE #From this we derive the initil price of the pair at X0 and Y0

print('The constant of the pool is', K)
print ('The starting price is {:.9f}'.format(Z0)) #this formats the value of Z0 as a floating-point number with 9 decimal places.


#PHASE 2: Given a buy pressure B, calculate a final price target Z1 and a price delta PD

FINAL_PRICE = Z1 = (((INITIAL_PAIR_LIQUIDITY_ETH+BUY_PRESSURE_ETH)**2)/K)*ETH_PRICE
PRICE_DELTA_IN_PERCENTAGE = PDP = ((FINAL_PRICE-INITIAL_PRICE)/INITIAL_PRICE)*100
PRICE_DELTA_IN_X = PDX = (FINAL_PRICE/INITIAL_PRICE)

print('With a', B,'ETH buy pressure the final price will be {:.9f}.'.format(Z1), 
      'This represents a price change of', PDX, 'x or', round(PDP),'%') #this formats the value of Z0 as a floating-point number with 9 decimal places.



#PHASE 2.1: Find a buy pressure B, to reach a final price target PT

TOT_POOL_LIQUIDITY_ETH = math.sqrt(PT*K/ETH_PRICE)
B = (TOT_POOL_LIQUIDITY_ETH-INITIAL_PAIR_LIQUIDITY_ETH)
MARKET_CAP = MC = PT*CS

print('The liquidity needed to reach a price of {:.9f}'.format(PT),'$ is', B,"ETH. This would mean a market cap of", int(MC),'$')


#PHASE 4: Find the buy pressure B needed to reach a market cap MCT

TOT_POOL_LIQUIDITY_ETH = math.sqrt((MCT/CS)*K/ETH_PRICE)
B = (TOT_POOL_LIQUIDITY_ETH-INITIAL_PAIR_LIQUIDITY_ETH)

print('The liquidity needed to reach a market cap of', MCT,'$ is', B, 'ETH.')