
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
                        stopConvertProcess();
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
            processStatus = $(this).parent('.geneticFlowerPart').children(".info").children('.status-geneticProcess');
            $.ajax({
                url: url + "/" + flowerPartId, //the page containing python script
                type: "get", //request type,
                success: function (status) {
                    if(status === "False"){
                        processStatus.text("Algo extraño sucedio...");
                        $(this).show();
                        console.log("False");
                    }
                    else{
                        stopConvertProcess();
                        processStatus.text("en ejecucion");
                        console.log("True");
                    }
                }
            });
    });

    // PAUSAR  GENETICO
    $(".geneticProcessInfo").on("click", ".pauseGeneticProcess",
        function () {
            url = $(this).attr("methodUrl");
            flowerPartId = $(this).attr("flowerPartId");
            processStatus = $(this).parent('.geneticFlowerPart').children('.status-geneticProcess');
            $.ajax({
                url: url + "/" + flowerPartId, //the page containing python script
                type: "get", //request type,
                success: function (status) {
                    if(status === "False"){
                        processStatus.text("Algo extraño sucedio...");
                        $(this).show();
                        console.log("False");
                    }
                    else{
                        stopConvertProcess();
                        processStatus.text("en ejecucion");
                        console.log("True");
                    }

                }
            });
    });
