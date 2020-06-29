
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

    function getCurrentStep(){
        var currentStepText = $(".currentStep");
        $.ajax({
            url:"/currentStep", //the page containing python script
            type: "get", //request type,
            success:function(step){
                currentStepText.text("Etapa: " + step);
            }
        });
        var totalSteps = $(".totalSteps");
        $.ajax({
            url:"/totalSteps", //the page containing python script
            type: "get", //request type,
            success:function(total){
                totalSteps.text("Total: " + total);
            }
        });
    }

    function stopConvertProcess(){
        clearInterval(window.processIntervalProcess);
        clearInterval(window.processIntervalCurrentStep);
        $(".startConvertProcess").show();
        console.log("Ciclo detenido");
    }

    function startConvertProcess(){
        var millisecondsProcess = 5000;
        window.processIntervalProcess = setInterval("convertProcess()",millisecondsProcess);
        var millisecondsCurrentStep = 1000;
        window.processIntervalCurrentStep = setInterval("getCurrentStep()",millisecondsCurrentStep);

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

