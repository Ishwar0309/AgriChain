pragma solidity ^0.4.21;
contract microFinance{
    struct Farmer{
        string farmerId;
        string farmerName;
    }
    struct ExpectedYields{
        string landLocation;
        string crop;
        uint256 quantity;
        uint256 expectedPrice;
        string expDate;
    }
    struct deal{
        address farmer;
        address customer;
        string terms;
        uint256 amount;
        uint256 holdingPercent;
    }
    mapping(address => Farmer) farmerMap;
    mapping(address => uint256) customerAddressToIdMap;
    mapping(address => deal) dealMapping;
    mapping(address => ExpectedYields) farmerYields;
    mapping(address => string) farmerAddressToYieldMapping;
    mapping(string => ExpectedYields) yieldIdToExpectedYieldMapping;
    
    mapping(string => string) dealIdToYieldId;

    mapping(string => deal) stringToDealMapping;
    mapping(string => address) farmerIdToAddressMapping;
    event farmerAdded(address farmer,string farmerId);
    event produceAdded(string farmerId,string crop,uint256 expectedPrice,string expDate);
    event rechargeWallet(address customer,uint256 amount);
    
    function addFarmer(address farmer,string memory farmerId) public {
        farmerIdToAddressMapping[farmerId] = farmer;
        emit farmerAdded(farmer,farmerId);
    }
    
    
    function addProduce(string memory farmerId,string memory yieldId,
    string memory landLocation,
    string memory crop,
    uint256 quantity,
    string memory expDate,
    uint256 expectedPrice
    ) public {
        ExpectedYields memory farmYield;
        farmYield.landLocation = landLocation;
        farmYield.crop = crop;
        farmYield.quantity = quantity;
        farmYield.expectedPrice = expectedPrice;
        farmYield.expDate = expDate;
        farmerYields[farmerIdToAddressMapping[farmerId]] = farmYield;
        yieldIdToExpectedYieldMapping[yieldId] = farmYield;

        farmerAddressToYieldMapping[farmerIdToAddressMapping[farmerId]] = yieldId;
        
        // farmerYields[farmerIdToAddressMapping[farmerId]].push(farmYield);
        emit produceAdded(farmerId,crop,expectedPrice,expDate); 
    }
    
    function getProduce(string memory farmerId) public view returns(
        string memory expDate,
        uint256 quantity,
        uint256 expectedPrice
        ){
            expDate = farmerYields[farmerIdToAddressMapping[farmerId]].expDate;
            quantity = farmerYields[farmerIdToAddressMapping[farmerId]].quantity;
            expectedPrice = farmerYields[farmerIdToAddressMapping[farmerId]].expectedPrice;
        }
       
    function addDeal(address customer,address farmer,string memory terms,
    uint256 amount, uint256 holdingPercent,string memory yieldId,string memory dealId) public {
        deal memory tempDeal;
        tempDeal.customer = customer;
        tempDeal.farmer = farmer;
        tempDeal.terms = terms;
        tempDeal.holdingPercent = holdingPercent;
        tempDeal.amount = amount;
        dealMapping[customer] = tempDeal;
        dealIdToYieldId[dealId] = yieldId;
        stringToDealMapping[dealId] = tempDeal;
    }
    function getDeal(string dealId) public view returns(string memory terms,
    uint256 amount, uint256 holdingPercent , address farmer
    ){
        terms = stringToDealMapping[dealId].terms;
        amount = stringToDealMapping[dealId].amount;
        holdingPercent = stringToDealMapping[dealId].holdingPercent;
        farmer = stringToDealMapping[dealId].farmer;
    }   
    
    
}