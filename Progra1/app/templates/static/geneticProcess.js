
    //CREAR OBJETO GENETICO
    $(".geneticProcess").on("click", ".createGenetic",
        function () {
            url = $(this).attr("methodUrl");
            var geneticStatus = $(this).parent().children('.status').children(".status-createGenetic");
            var button = $(this);
            button.hide();
            $.ajax({
                url: url, //the page containing python script
                type: "get", //request type,
                success: function (status) {
                    if(status === "False"){
                        button.show();
                        geneticStatus.text("Creo que olvidas algo...");
                        console.log("False");
                    }
                    else{
                        geneticStatus.text("Estructura creada");
                        console.log("True");
                    }
                }
            });
    });


    // INICIO DE GENETICO
    $(".geneticProcessInfo").on("click", ".startGeneticProcess",
        function () {
            url = $(this).attr("methodUrl");
            flowerPartId = $(this).attr("flowerPartId");
            processStatus = $(this).parent().parent().children(".info").children('.status-geneticProcess');
            $.ajax({
                url: url + "/" + flowerPartId, //the page containing python script
                type: "get", //request type,
                success: function (status) {
                    if(status === "False"){
                        processStatus.text("¿Ya creaste la estuctura?");
                        $(this).show();
                        console.log("False");
                    }
                    else{
                        processStatus.text("en ejecucion");
                        console.log("True");
                    }
                }
            });
    });

    // PAUSAR  GENETICO
    $(".geneticProcessInfo").on("click", ".pauseGeneticProcess",
        function () {
            pauseButton = $(this);
            url = pauseButton.attr("methodUrl");
            flowerPartId = pauseButton.attr("flowerPartId");
            processStatus = pauseButton.parent().parent().children('.info').children('.status-geneticProcess');
            $.ajax({
                url: url + "/" + flowerPartId, //the page containing python script
                type: "get", //request type,
                success: function (status) {
                    if(status === "False"){
                        processStatus.text("Primero inicia el genético");
                        console.log("Pausa error");
                    }
                    else{
                        if(pauseButton.first().text() === "Pausar"){
                            pauseButton.text("Continuar");
                            processStatus.text("En pausa");
                        }
                        else{
                           pauseButton.text("Pausar");
                           processStatus.text("En ejecucion");
                        }

                        console.log("Pausa ejecutada");
                    }
                }
            });
    });




       //MOSTAR PROGESO GENETICO
    $(".geneticProcessInfo").on("click", ".showGeneticProcess",
        function () {
            url = $(this).attr("methodUrl");
            flowerPartId = $(this).attr("flowerPartId");
            imageProgressDiv = $(this).parent().parent().children('.geneticInfo').children('.imageGeneticProgress');
            infoGeneticProgress = $(this).parent().parent().children('.geneticInfo').children('.infoGeneticProgress');
            console.log("Show genetic progress");
            $.ajax({
                url: url + "/" + flowerPartId, //the page containing python script
                type: "get", //request type,
                success: function (plotModel) {
                    if(plotModel === "False"){
                        console.log("Mostrar progreso Error");
                    }
                    else{

                        $.ajax({
                            url: "showGeneticInfo/" + flowerPartId, //the page containing python script
                            type: "get", //request type,
                            success: function (infoPlotModel) {
                                if(plotModel === "False"){
                                    console.log("Mostrar info Error");
                                }
                                else{
                                    infoGeneticProgress.empty();
                                    infoGeneticProgress.append(infoPlotModel);
                                    console.log("Markup info agregado");
                                }
                            }
                        });

                        imageProgressDiv.empty();
                        imageProgressDiv.append(plotModel);
                        console.log("Markup agregado");
                    }
                }
            });
    });

    //GENERAR NUEVA FLOR
        // INICIO DE GENETICO
    $(".geneticNewFlower").on("click", ".newFlower",
        function () {
            url = $(this).attr("methodUrl");
            flowerPartId = $(this).attr("flowerPartId");
            newFlowerDiv = $(this).parent().children('.showNewFlower');
            $.ajax({
                url: url, //the page containing python script
                type: "get", //request type,
                success: function (plotModel) {
                    if(plotModel === "False"){
                        console.log("New flower error")
                    }
                    else{
                        newFlowerDiv.empty();
                        newFlowerDiv.append(plotModel);
                        console.log("New flower");
                    }
                }
            });
    });