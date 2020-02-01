pragma solidity ^0.5.0;
contract SupplyChain{

    struct qualityReport{
        address inspector;
        int256 quantity;
        int256 sampleSize;
        int256 defective;
        string remarks;
    }
    struct processorReport{
        string remarks;
        string receivedShipment;
        qualityReport qualityreport;
    }
    struct retailerReport{
        string productName;
        string rawMaterial;
        string remarks;
        string manufacturedDate;
        int256 quantityProduced;
        processorReport processedReport;
    }
   
    // Maps address of respective Stakeholders to true
    mapping(address=>bool) isFarmer;
    mapping(address=>bool) isProcessor;
    mapping(address=>bool) isRetailer;
    // mapping(address=>bool) isDistributor;
    mapping(address=>bool) isInspector;
   
    // Map Stakeholders address to Key
    mapping(address=>string) farmerMapping;
    mapping(address=>string) processorMapping;
    mapping(address=>string) retailerMapping;
    // mapping(address=>string) distributorMapping;
    mapping(address=>string) inspectorMapping;
   
    //Events
   
    event farmerAddition(address farmerAddress,string farmerKey);
    event processorAddition(address processorAddress,string processorKey);
    // event distributorAddition(address distributorAddress,string farmerKey);
    event retailerAddition(address retailerAddress,string retailerKey);
    event inspectorAddition(address inspectoAddress,string inspectoKey);
    //Modifiers
    modifier onlyFarmer(address farmer){
        require(isFarmer[farmer]);
        _;
    }
    modifier onlyInspector(address inspector){
        require(isFarmer[inspector]);
        _;
    }
    modifier onlyRetailer(address retailer){
        require(isRetailer[retailer]);
        _;
    }
    modifier onlyProcessor(address processor){
        require(isProcessor[processor]);
        _;
    }
    // modifier onlyDistributor(address distributor){
    //     require(isDistributor[distributor]);
    //     _;
    // }
    mapping(address=>mapping(string=>qualityReport)) qualityReports; // mapping of farmers address to lotNumber and report
    mapping(address=>mapping(address => mapping(string=>processorReport))) processorReports;
    mapping(string => string) lotToBatch;
    mapping(address=>mapping(string=>retailerReport)) retailerReports;
   
    function addFarmer(address _farmer,string memory _farmerKey) public {
        isFarmer[_farmer] = true;
        farmerMapping[_farmer] = _farmerKey;
        emit farmerAddition(_farmer,_farmerKey);
    }
    function addProcessor(address _processor,string memory _processorKey) public {
        isProcessor[_processor] = true;
        processorMapping[_processor] = _processorKey;
        emit processorAddition(_processor,_processorKey);
    }
    function addInspector(address _inspector,string memory _inspectorKey) public {
        isInspector[_inspector] = true;
        inspectorMapping[_inspector] = _inspectorKey;
        emit inspectorAddition(_inspector,_inspectorKey);
    }
    function addRetailer(address _retailer,string memory _retailerKey) public {
        isRetailer[_retailer] = true;
        retailerMapping[_retailer] = _retailerKey;
        emit retailerAddition(_retailer,_retailerKey);
    }
    function addQualityReport(address _farmer,address _inspector,string memory _lotNumber,string memory _remarks,int256 _sampleSize,int256 _quantity, int256 _defective) public {
        qualityReports[_farmer][_lotNumber].inspector = _inspector;
        qualityReports[_farmer][_lotNumber].remarks = _remarks;
        qualityReports[_farmer][_lotNumber].sampleSize = _sampleSize;
        qualityReports[_farmer][_lotNumber].defective = _defective;
        qualityReports[_farmer][_lotNumber].quantity = _quantity;
    }
    function getQualityReport(address _farmer,string memory _lotNumber) public view returns(
        string memory _remarks,
        address _inspector,
        int256 _sampleSize,
        int256 _defective,
        int256 _quantity
        ){
        _remarks = qualityReports[_farmer][_lotNumber].remarks;
        _inspector = qualityReports[_farmer][_lotNumber].inspector;
        _sampleSize = qualityReports[_farmer][_lotNumber].sampleSize;
        _defective = qualityReports[_farmer][_lotNumber].defective;
        _quantity = qualityReports[_farmer][_lotNumber].quantity;
    }
    function addProcessorReport(address _processor,address _farmer,
                                string memory _lotNumber,string memory _remarks,
                                string memory _receivedShipment) public{
        // qualityReport = qualityReports[_farmer][_lotNumber];
        processorReports[_processor][_farmer][_lotNumber].remarks = _remarks;
        processorReports[_processor][_farmer][_lotNumber].receivedShipment = _receivedShipment;
        processorReports[_processor][_farmer][_lotNumber].qualityreport = qualityReports[_farmer][_lotNumber];
    }
    function getProcessorReport(address _processor,address _farmer,string memory _lotNumber) public view returns(
        string memory _remarks,
        string memory _receivedShipment
        ){
        _remarks = processorReports[_processor][_farmer][_lotNumber].remarks;
        _receivedShipment = processorReports[_processor][_farmer][_lotNumber].receivedShipment;
    }
    function BatchtoLot(string memory _batchNumber,string memory _lotNumber) public{
        lotToBatch[_batchNumber] = _lotNumber;
    }
    function addRetailerReport(address _retailer, address _processor, address _farmer,
        string memory _remarks,
        string memory _rawMaterial,
        string memory _productName,
        string memory _manufacturedDate,
        int256 _quantity,
        string memory _batchNumber
    ) public {
        retailerReports[_retailer][_batchNumber].productName = _productName;
        retailerReports[_retailer][_batchNumber].remarks = _remarks;
        retailerReports[_retailer][_batchNumber].rawMaterial = _rawMaterial;
        retailerReports[_retailer][_batchNumber].manufacturedDate = _manufacturedDate;
        retailerReports[_retailer][_batchNumber].quantityProduced = _quantity;
        retailerReports[_retailer][_batchNumber].processedReport = processorReports[_processor][_farmer][lotToBatch[_batchNumber]];
    }
    function getRetailerReport(address _retailer,string memory _batchNumber) public view returns(
        string memory _productName,
        string memory _remarks,
        string memory _rawMaterial,
        string memory _manufacturedDate,
        int256 _quantity
        ){
            _productName = retailerReports[_retailer][_batchNumber].productName;
            _remarks = retailerReports[_retailer][_batchNumber].remarks;
            _rawMaterial = retailerReports[_retailer][_batchNumber].rawMaterial;
            _manufacturedDate = retailerReports[_retailer][_batchNumber].manufacturedDate;
            _quantity = retailerReports[_retailer][_batchNumber].quantityProduced;
        }
   
}