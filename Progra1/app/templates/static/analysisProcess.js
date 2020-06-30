    function stopAnalysisProcess(){
        clearInterval(window.analysisProcessInterval);
        console.log("Ciclo analisis detenido");
    }

    function startAnalysisProcess(){
        var millisecondsAnalyse = 1000;
        window.analysisProcessInterval = setInterval("", millisecondsAnalyse);

        $(".startConvertProcess").show();
        console.log("Ciclo analisis iniciado");
    }


    $(".analysisProcess").on("click", ".startAnalysisProcess",
        function () {
            url = $(this).attr("methodUrl");
            startConvertProcess();

            $.ajax({
                url: url, //the page containing python script
                type: "get", //request type,
                success: function (t) {
                    if(t === "False"){
                        //stopConvertProcess();
                        $(".convertProgress").text("voraz: no!");
                    }
                    else{
                        stopConvertProcess();
                        $(".convertProgress").text("voraz: finalizado!");
                    }
                }
            });


        });
