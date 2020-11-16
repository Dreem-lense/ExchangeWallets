from etherscan.etherscan import Etherscan
##import schedule
##import time

##Run this once daily at 1pm central time using "pip install schedule" python schedule.  see docs : https://schedule.readthedocs.io/en/stable/
#def job():


eth = Etherscan('M3K3M2PGEK77K4MEYM8AKGQ88Q6WUFR753') # key in quotation marks


Binance_Addresses = {
    "wallet1" : "0x3f5ce5fbfe3e9af3971dd833d26ba9b5c936f0be",
    "wallet2" : "T0xd551234ae421e3bcba99a0da6d736074f22192ff",
    "wallet3" : "0x564286362092d8e7936f0549571a803b203aaced",
    "wallet4" : "0x0681d8db095565fe8a346fa0277bffde9c0edbbf",
    "wallet5" : "0xfe9e8709d3215310075d67e3ed32a380ccf451c8",
    "wallet6" : "0x4e9ce36e442e55ecd9025b9a6e0d88485d628a67",
    "wallet7" : "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",
    "wallet8" : "0xf977814e90da44bfa03b6295a0616a897441acec",
    "wallet9" : "0x001866ae5b3de6caa5a51543fd9fb64f524f5478",
  }
Bittrex_Addresses = {
    "wallet1" : "0xfbb1b73c4f0bda4f67dca266ce6ef42f520fbb98",
    "wallet2" : "T0xe94b04a0fed112f3664e45adb2b8915693dd5ff3",
    "wallet3" : "0x66f820a414680b5bcda5eeca5dea238543f42054",
    "wallet3" : "0xa3c1e324ca1ce40db73ed6026c4a177f099b5770",
  }
Coinbase_Addresses = {
    "wallet1" : "0xfbb1b73c4f0bda4f67dca266ce6ef42f520fbb98",
    "wallet2" : "T0xe94b04a0fed112f3664e45adb2b8915693dd5ff3",
    "wallet3" : "0x66f820a414680b5bcda5eeca5dea238543f42054",
    "wallet3" : "0xa3c1e324ca1ce40db73ed6026c4a177f099b5770",
  }
Kraken_Addresses = {
    "wallet1" : "0x2910543af39aba0cd09dbb2d50200b3e800a63d2",
    "wallet2" : "0x0a869d79a7052c7f1b55a8ebabbea3420f0d1e13",
    "wallet3" : "0xe853c56864a2ebe4576a807d26fdc4a0ada51919",
    "wallet4" : "0x267be1c1d684f78cb4f6a176c4911b741e4ffdc0",
    "wallet5" : "0x53d284357ec70ce289d6d64134dfac8e511c8a3d",
  }
OKEx_Addresses = {
    "wallet1" : "0x6cc5f688a315f3dc28a7781717a9a798a59fda7b",
    "wallet2" : "0x236f9f97e0e62388479bf9e5ba4889e46b0273c3",
    "wallet3" : "0xa7efae728d2936e78bda97dc267687568dd593f3",
  }  
FTX_Addresses = {
    "wallet1" : "0x2faf487a4414fe77e2327f0bf4ae2a264a776ad2",
    "wallet2" : "0xc098b2a3aa256d2140208c3de6543aaef5cd3a94",
  }

Token_Contract_Addresses = {
	"Chainlink" : "0x514910771af9ca656af840dff83e8264ecf986ca",
	"YearnFinance" : "0x0bc529c00C6401aEF6D220BE8C6Ea1667F6Ad93e",
	"BandToken" : "0xba11d00c5f74255f56a5e366f4f77f5a186d7f55",
	"ReserveRights" : "0x8762db106b2c2a0bccb3a80d1ed41273552616e8",
	"OceanToken" : "0x967da4048cD07aB37855c090aAF366e4ce1b9F48",
	"BNB" : "0xB8c77482e45F1F44dE1745F52C74426C631bDD52",
	"Uniswap" : "0x1f9840a85d5af5bf1d1762f925bdaddc4201f984",
	"SynthetixNetworkToken" : "0xc011a73ee8576fb46f5e1c5751ca3b9fe0af2a6f",
	"Decentraland" : "0x0f5d2fb29fb7d3cfee444a200298f468908cc942",
	"KyberNetwork" : "0xdd974d5c2e2928dea5f71b9825b8b646686bd200",
	"ZRX" : "0xe41d2489571d322189246dafa5ebde1f4699f498",
	"BAT" : "0x0d8775f648430679a709e98d2b0cb6250d2887ef",
	"AaveToken" : "0x7fc66500c84a76ad7e9c93437bfc5ac33e2ddae9",
	"Republic" : "0x408e41876cccdc0f92210600ef50372656052a38",
}

token_list = ('Chainlink', 'YearnFinance', 'BandToken', 'ReserveRights', 'OceanToken', 'BNB', 'Uniswap', 'SynthetixNetworkToken', 'Decentraland', 'KyberNetwork', 'ZRX', 'BAT', 'AaveToken', 'Republic')

#Addresses for ERC-20 Tokens
Token_Address = Token_Contract_Addresses.get(token_list[Chainlink])

print(Token_Address)


##Retrieve Account Balance of each listed token from their corresponding contract_address and all Exchange Wallets
##eth.get_acc_balance_by_token_and_contract_address(contract_address = "", address="")

##Collect Total Supply of asset/token 
##eth.get_total_supply_by_contract_address()

##Store Data pulled from above in SQL database


##Total Asset Balance & Total Asset Circulating Supply. Calculate % change in account balances on 1/5/14/30 day