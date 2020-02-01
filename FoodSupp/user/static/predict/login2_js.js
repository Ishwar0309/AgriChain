
$(function() {

    $('#login-form-link').click(function(e) {
		$("#login-form").delay(100).fadeIn(100);
 		$("#register-form").fadeOut(100);
		$('#register-form-link').removeClass('active');
		$(this).addClass('active');
		e.preventDefault();
		window.location.href = "/users/login";
	});
	$('#register-form-link').click(function(e) {
		$("#register-form").delay(100).fadeIn(100);
 		$("#login-form").fadeOut(100);
		$('#login-form-link').removeClass('active');
		$(this).addClass('active');
		e.preventDefault();
		window.location.href = "/users/register";
	});


  $("#manual_btn").click(function(){
    $('#input_value1').removeAttr("disabled");
    $('#input_value2').removeAttr("disabled");
    $('#input_value3').removeAttr("disabled");
    $('#input_value4').removeAttr("disabled");
    $('#input_value5').removeAttr("disabled");
    $('#auto_btn').removeClass("active");
    $('#manual_btn').addClass("active");
  });

  $("#auto_btn").click(function(){
    $('#input_value1').attr("disabled" , "true");
    $('#input_value2').attr("disabled" , "true");
    $('#input_value3').attr("disabled" , "true");
    $('#input_value4').attr("disabled" , "true");
    $('#input_value5').attr("disabled" , "true"); 
    $('#auto_btn').addClass("active");
    $('#manual_btn').removeClass("active");
  });
});


function myMap() {
  var cordinateslt = [];
  var cordinateslg = [];
  var loclat , loclng ; 
    var cordinates = [];
  var num = cordinates.length;
  var map,location,mapCanvas,mapOptions;
  
 if (navigator.geolocation) {
          navigator.geolocation.getCurrentPosition(function(position) { 
              loclat =  position.coords.latitude;
              loclng = position.coords.longitude;
                location = new google.maps.LatLng(loclat , loclng);
          mapCanvas = document.getElementById("map");
            mapOptions = {center: location, zoom: 16};
                map = new google.maps.Map(mapCanvas,mapOptions);
                map.setMapTypeId(google.maps.MapTypeId.SATELLITE); 
             
         
                function setpoly(){

           for(var i=0;i<num;i++)
            {
            cordinates.push(new google.maps.LatLng(cordinateslt[i] , cordinateslg[i]));
          }
            cordinates.pop();
            map.setCenter(cordinates[num-1]);

            flightPath = new google.maps.Polygon({  
             path:cordinates,
            strokeColor: "#0000FF",
            strokeOpacity: 0.8,
            strokeWeight: 2,
            fillColor: "#0000FF",
            fillOpacity: 0.4
           });
            flightPath.setMap(map);
            google.maps.event.clearListeners(map, "rightclick");
            google.maps.event.clearListeners(map, "click");
          }

      google.maps.event.addListener(map, "rightclick", function(event) {
          var lat = event.latLng.lat();
          var lng = event.latLng.lng();
          cordinateslt.push(lat);
          cordinateslg.push(lng);
           num = num + 1;
          setpoly();
      });

      google.maps.event.addListener(map, "click", function(event) {
          var lat = event.latLng.lat();
          var lng = event.latLng.lng();
          cordinateslt.push(lat);
          cordinateslg.push(lng);
          num = num + 1;
      });


          });
        }
  }
