$(document).ready(function(){
    $("#bajra").click(function(){
            $.ajax({
                type: "GET",
                url: "/analysis/data",
                data: {
                    'post_id': 'bajra',
                },
                success: function (data) {
                    console.log(data);
                      var ctx_bajra = null;
                      ctx_bajra = document.getElementById('myChartArea');
    //                  if (ctx_bajra) {
    //                        ctx_bajra.destroy();
    //                    }
                       chart_bajra = new Chart(ctx_bajra, {
                            type: 'line',
                            data: data.datasets,
                            options: data.options,
                       });
                       }
          });
    });

    $("#barley").click(function(){
        $.ajax({
                type: "GET",
                url: "/analysis/data",
                data: {
                    'post_id': 'barley',
                },
                success: function (data) {
                    console.log(data);
                      var ctx_bajra = null;
                      ctx_bajra = document.getElementById('myChartArea');
    //                  if (ctx_bajra) {
    //                        ctx_bajra.destroy();
    //                    }
                       chart_bajra = new Chart(ctx_bajra, {
                            type: 'line',
                            data: data.datasets,
                            options: data.options,
                       });
                       }
          });
    });

    $("#jowar").click(function(){
          $.ajax({
                type: "GET",
                url: "/analysis/data",
                data: {
                    'post_id': 'jowar',
                },
                success: function (data) {
                    console.log(data);
                      var ctx_bajra = null;
                      ctx_bajra = document.getElementById('myChartArea');
    //                  if (ctx_bajra) {
    //                        ctx_bajra.destroy();
    //                    }
                       chart_bajra = new Chart(ctx_bajra, {
                            type: 'line',
                            data: data.datasets,
                            options: data.options,
                       });
                       }
          });
    });

    $("#maize").click(function(){
        $.ajax({
                type: "GET",
                url: "/analysis/data",
                data: {
                    'post_id': 'maize',
                },
                success: function (data) {
                    console.log(data);
                      var ctx_bajra = null;
                      ctx_bajra = document.getElementById('myChartArea');
    //                  if (ctx_bajra) {
    //                        ctx_bajra.destroy();
    //                    }
                       chart_bajra = new Chart(ctx_bajra, {
                            type: 'line',
                            data: data.datasets,
                            options: data.options,
                       });
                       }
          });
    });

    $("#wheat").click(function(){
        $.ajax({
                type: "GET",
                url: "/analysis/data",
                data: {
                    'post_id': 'wheat',
                },
                success: function (data) {
                    console.log(data);
                      var ctx_bajra = null;
                      ctx_bajra = document.getElementById('myChartArea');
    //                  if (ctx_bajra) {
    //                        ctx_bajra.destroy();
    //                    }
                       chart_bajra = new Chart(ctx_bajra, {
                            type: 'line',
                            data: data.datasets,
                            options: data.options,
                       });
                       }
          });
    });


});