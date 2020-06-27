
    $(document).ready(function(){
        isRunning();
    });

    function isRunning(){
        $.ajax({
            url:"/isConvertRunning", //the page containing python script
            type: "get", //request type,
            success:function(isRunning){
                console.log("IsRunning: " + isRunning);
                if(isRunning === "True"){
                    $(".convertProgress").text("voraz: iniciando...");
                    startConvertProcess();
                }
                else{
                    stopConvertProcess();
                }
            }
        });
    }

    function isFinished(){
        var finished = false;
        $.ajax({
            url:"/isConvertFinished", //the page containing python script
            type: "get", //request type,
            success:function(isFinished){
                console.log("isFinished: " + isFinished);
                if(isFinished === "True"){
                    finished = isFinished;
                    $(".convertProgress").text("voraz: finalizado");
                }
                else{
                    $(".convertProgress").text("voraz: iniciando...");
                }
            }
        });
        return finished;
    }


    function convertProcess() {
        var processImageDiv = $(".convertProgressImage");
        $.ajax({
            url:"/convertProcess", //the page containing python script
            type: "get", //request type,
            success:function(plot_model){
                if(plot_model === "False"){
                    stopConvertProcess();
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
        $(".startConvertProcess").show();
        console.log("Ciclo detenido");
    }

    function startConvertProcess(){
        var milliseconds = 5000;
        window.processInterval = setInterval("convertProcess()",milliseconds);
        $(".startConvertProcess").show();
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
                    if(t === "False"){
                        stopConvertProcess();
                        $(".convertProgress").text("voraz: no!");
                    }
                }
            });


        });

