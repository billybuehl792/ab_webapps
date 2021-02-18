$(document).ready(function() {
    var workOption = $("#work-option");
    var workSection = $("#work-section");
    var timeOption = $("#time-option");
    var timeSection = $("#start-complete")
    var duration = $("#duration");

    // toggle work location
    if (workOption.prop("checked")) {
        workSection.show();
    } else {
        workSection.hide();
    }
    $(workOption).click(function() {
        if (workOption.prop("checked")) {
            workSection.slideDown(200);
        } else {
            workSection.slideUp(200);
        }
    });

    // toggle start/completion time
    if (timeOption.prop("checked")) {
        duration.hide();
        timeSection.show();
    } else {
        duration.show();
        timeSection.hide();
    }
    $(timeOption).click(function() {
        if (timeOption.prop("checked")) {
            duration.slideUp(200);
            timeSection.slideDown(200);
        } else {
            timeSection.slideUp(200);
            duration.slideDown(200);
        }
    });

    // live customer search
    $("#customer-search").on("input", function(e) {
        var inputText = $("#customer-search").val();

        // set temp text
        $("#search-results").html("searching!");

        // GET request to customer-search
        $.ajax({
            method: "GET",
            url: "/customer-search",
            data: {text:inputText},
            success: function(res) {
                $("#search-results").html("");
                if (res.length > 0) {
                    $("#search-results").slideDown(200);
                    $.each(res, function(index, item) {
                        var inputElem = document.createElement("input");
                        inputElem.type = "button";
                        inputElem.value = item["name"] + " - " + item["phone"] + " - " + item["address"];
                        inputElem.className = "customer-element";
                        inputElem.onclick = (function() {
                            $("#customer-name").val(item["name"]);
                            $("#customer-id").val(item["public_id"]);
                            $("#customer-search").val("");
                            $("#search-results").slideUp(200);
                        });
                        $("#search-results").append(inputElem);
                    });
                } else {
                    $("#search-results").slideUp(200);
                }
            },
            error: function() {
                console.log("error!!");
            }
        });
    });

    // submit disabled
    $('form').submit(function(e) {
        $(':disabled').each(function(e) {
            $(this).removeAttr('disabled');
        })
    });
});