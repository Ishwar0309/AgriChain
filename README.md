# FoodSupp 

# Implementation
Food Supply Chain can be used to track a particular product right from its raw material( eg: Tomato ) from farm to the processed product (eg : Tomato sauce) in the retailer store up for sale.

The supply chain starts with the production of raw material in the farmers. Hence we have created a full end to end solution for farmers which will help them to produce and sell their yields at a good rate.

The functionalities provided by us are as follows:
1. A machine learning model(which uses KNN algorithm)  predicts the most suitable crops that can be cultivated by the farmer depending on the different conditions like temperature and nitrogen value , pH value of soil,etc.Also, it predicts the suitable Bio-fertilizers for the crop.
2. The next step is the cost that goes into the agriculture process. We are providing a blockchain based Micro Finance solution where the investors can invest their money and provide funds to the farmers which they can get back in terms of profit percent.dfty Hence, the farmer does not have to wait for bank loan or other lending mechanisms to raise the initial investment.
3. Another machine learning model using Decision Tree Regressor predicts the optimal crop price at which the crop should be sold. This model helps to educate the farmers about the current market price of product.
4. The farmers can sell their produce to the processor at the marketplace. The quality of the crops is verified by the quality checker and the report of the quality is stored in the blockchain network. The processor can use this as a tool for ensuring that the raw material is of good quality.
5. The processor can then sell their product to the retailer. At each step a report is added to the blockchain. When finally the product reaches the customer the entire report from the retailer to the farmer can be made available. 
6. By implementing this, the network is totally transparent and forgery anywhere in between the supply chain can be known easily as timestamp of each transaction is recorded. This provides full traceability of the product to the customer.  


Ppt link : https://docs.google.com/presentation/d/15PZT7NSlSMeFujkZKU1RieKTWBCMYGEKVQHFiGKzUqc/edit?usp=sharing


# Dependencies 
1. Ganache(install from "https://www.trufflesuite.com/ganache")
2. Remix Console (https://remix.ethereum.org/)
3. Django Framework (pip3 install django)

# Steps to implement :
For testing:

1. Deploy Contracts on Ganache
-  Connect Ganache to Remix IDE.
-  Deploy both the contracts in Contracts folder after compiling.
-  Copy the contract addressess and assign them to contract and contract1 variables in user/views.py. (Line 31 and 40).
  
2. Change Path of SVG files (Present in "user/views.py" at line number --) to Systems directory(Ex: "C://Your path/FoodSupp/user/static/Images/QRfiles/").

3. Run server 
  a. Run the "python manage.py runserver" command after changing the root directory as "FoodSupp".

# Demo Link : 
