$(document).ready(function(){
	// alert('jeyyy');
	// alert(data);
	mapboxgl.accessToken = 'pk.eyJ1IjoiZGVlcGlrYXBvbWVuZGthciIsImEiOiJjazFsMWd4d3QwMHdpM21uc3U3OGxrbndlIn0.6Cj2VYFMQq8V6TCYLIySzg';

	var map = new mapboxgl.Map({
	  container: 'map',
	  style: 'mapbox://styles/mapbox/light-v10',
	  center: [-96, 37.8],
	  zoom: 3
	});
	var geojson_new = {};
	$.ajax({
		type : 'GET',
		url : '/marker/map',
		data : {
			post_id : 'my_map',
		},
		success:function(data) {
			// alert('entered');
			var count = 0;

			// console.log(data);
			$.each(data, function(farmer_key, values){
				// console.log(farmer_key);
				// console.log(values[0]);
				// for(let i = 0; i < values.length; i++){
					console.log(typeof(values[0]));
					$.each(values[0], function(broadcast_key, value1){
						// console.log(broadcast_key);
						// console.log(value1.cropName);
						// console.log(value1.expectedPrice);
						// console.log(value1.availableQuantity);
						// console.log(value1.coordinates[0]);

					// });
						// console.log('hello');
						geojson = {
						  type: 'FeatureCollection',
						  features: [{
						    type: 'Feature',
						    geometry: {
						      type: 'Point',
						      coordinates: value1.coordinates,
						    },
						    properties: {
						      title: farmer_key,
						      description: [{
						      	'cropName':value1.cropName,
						      	'availableQuantity':value1.availableQuantity,
						      	'expectedPrice':value1.expectedPrice}]
						    }
						    }]
						}
						count = count+1;
						geojson_new[count] = geojson;
						console.log(geojson);
				});
			});
			var marker_count = 0;
			$.each(geojson_new, function(length, marker) {
				// console.log('EMTER');

			  var el = document.createElement('div');
			  el.className = 'marker';
			  // console.log('HELOOOOO');
			  // console.log(marker.features[0].properties.description[0].cropName);
			  // console.log('DONEEE');

			  // make a marker for each feature and add to the map
			  new mapboxgl.Marker(el)
			  .setLngLat(marker.features[0].geometry.coordinates)
			  .setPopup(new mapboxgl.Popup({ offset: 25 }) // add popups
			  .setHTML('<h3>' + marker.features[0].properties.title + '</h3><p>' + 'cropName:' + marker.features[0].properties.description[0].cropName + '</p><p>' + 'availableQuantity:' + marker.features[0].properties.description[0].availableQuantity +'</p><p>' + 'expectedPrice:' + marker.features[0].properties.description[0].expectedPrice +'</p>'))
			  .addTo(map);
				});	
				marker_count = marker_count+1;
				console.log(marker_count);
		}
	});
});

