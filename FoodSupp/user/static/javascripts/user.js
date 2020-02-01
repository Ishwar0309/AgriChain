$(document).ready(function(){
    var myOptions1 = [];
    $.ajax({
            type: "GET",
            url: "getData/",
            data: {
				'post_id':'yieldIds'
            },
            success: function (data) {
//                alert(data);
                $.each( data, function( key, value ) {
                    myOptions1[key] = value;
                });
                console.log(myOptions1)
                var mySelect1 = $('#idSelect');
                 $.each(myOptions1, function(key,value) {
//                    console.log(value.yieldIds)
                    mySelect1.append( $('<option></option>').val(value.yieldIds).html(value.yieldIds));
                });
            }
     });
     $('#idSelect').on('change',function () {
            var selectedItem = $(this).val();
//	        alert('hey');
            var myOptions = []
            $.ajax({
                type: "GET",
                url: "getData/",
                data: {
                    'post_id':'lotIds',
                    'selectedItem': selectedItem,
                },
                success: function (data) {
    //                alert(data);
                    $.each( data, function( key, value ) {
                        myOptions[key] = value;
                    });
                    console.log(myOptions);
                    var mySelect = $('#lotIdSelect');
                     $.each(myOptions, function(key,value) {
//                        console.log(value)
                        mySelect.append( $('<option></option>').val(value.lotNumbers).html(value.lotNumbers));
                    });
                }
            });
     });
    var elementClicked;
    $("#statusButton").click(function(){
       elementClicked = true;
       console.log("aya")
    });
//    if( elementClicked != true ) {
//        alert("element not clicked");
//    }else{
//        alert("element clicked");
//    }
});

//
//function getStatus(){
//    alert('heyyy');
//    selectedValue = document.getElementById('idSelect').value;
//    lotIdSelected = document.getElementById('lotIdSelect').value;
//    $.ajax({
//                type: "GET",
//                url: "getData/",
//                data: {
//                    'post_id':'statusCheck',
//                    'selectedValue': selectedValue,
//                    'lotIdSelected': lotIdSelected
//                },
//                success: function (data) {
//                   alert('done');
//                }
//    });
//}

$(document).ready(function () {
  // Listen to click event on the submit button
  $('#statusButton').click(function (e) {

    e.preventDefault();

    var selectedValue = $('#idSelect').val();
    var lotIdSelected = $('#lotIdSelect').val();



    $.ajax({
                type: "GET",
                url: "getData/",

                data: {
                    'post_id':'statusCheck',
                    'selectedValue': selectedValue,
                    'lotIdSelected': lotIdSelected
                },
                success: function (data) {
                   reportStatus = data.insuredStatus;
                   paymentStatus = data.paymentStatus;
                   processorReportStatus = data.processorReportStatus;
//                   alert(processorReportStatus);
                   console.log(reportStatus);
                   console.log(paymentStatus);
                   console.log(processorReportStatus);

                   if(reportStatus == 1){
                        $('#reportAdded').attr('class','progtrckr-done');
                        if(paymentStatus == 1){
                            $('#paymentStatus').attr('class','progtrckr-done');
                        }
                        if(processorReportStatus == 1){
                            $('#processorReportStatus').attr('class','progtrckr-done');
                        }
                   }
//                   $('#statusButton').click(function() {
//                    $(".ptracker").toggle();
//                  });
                }
    });
  });
});
