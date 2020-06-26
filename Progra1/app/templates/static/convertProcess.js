    /*
    $(document).ready(function(){
        var milliseconds = 5000;
        var processInterval = setInterval("convertProcess()",milliseconds);
    });
    */
    function convertProcess() {
        var processImageDiv = $(".convertProgressImage");
        $.ajax({
            url:"/convertProcess", //the page containing python script
            type: "get", //request type,
            success:function(plot_model){
                if(plot_model === "False"){
                    stopConvertProcess();
                    $(".startConvertProcess").show();
                }
                else{
                    processImageDiv.empty();
                    processImageDiv.append(plot_model);
                    convertProgressBar();
                }

            }
        });
    }

    function convertProgressBar(){
        var progressSpan = $(".convertProgress");
        $.ajax({
            url:"/convertProgress", //the page containing python script
            type: "get", //request type,
            success:function(progress){
                progressSpan.text("voraz: " + progress + "%");
            }
        });
    }

    function stopConvertProcess(){
        clearInterval(window.processInterval);
        console.log("Ciclo detenido");
    }

    function startConvertProcess(){
        var milliseconds = 5000;
        window.processInterval = setInterval("convertProcess()",milliseconds);
        console.log("Ciclo iniciado");
    }

    $(".convertProcess").on("click", ".startConvertProcess",
        function () {
            url = $(this).attr("methodUrl");
            var processImageDiv = $(".convertProgressImage");
            $(this).hide();
            startConvertProcess();
            $.ajax({
                url: url, //the page containing python script
                type: "get", //request type,
                success: function (t) {
                    console.log(t);
                }
            });
        });

