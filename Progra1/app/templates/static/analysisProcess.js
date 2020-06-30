    $(".analysisProcess").on("click", ".startAnalysisProcess",
        function () {
            url = $(this).attr("methodUrl");
            var status  = $('.status-AnalysisiProcess');
            var analysisInfo = $('.analysisProcessInfo');
            status.text('Analizando datos...');
            $.ajax({
                url: url, //the page containing python script
                type: "get", //request type,

                success: function (markup) {
                    if(markup === "False"){
                        status.text("¿Qué haces? Ocupamos los datos del voraz");
                    }
                    else{
                        status.text("Listo!");
                        analysisInfo.empty();
                        analysisInfo.append(markup);
                    }
                }
            });


        });
