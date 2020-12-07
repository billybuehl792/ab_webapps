$(document).ready(function() {
    // Calculate from table
    function calculate() {
        // Calculate totals from item-table
        var subtotal = 0;
        var taxRate = parseFloat($("#tax-rate").html());

        $(".item-table tr").each(function() {
            let price = parseFloat($(this).find(".price").text()) || 0;
            let multiplier = parseInt($(this).find(".quantity").val()) || 0;
            subtotal += Math.round(price * multiplier * 100) / 100;
        });
        var tax = Math.round(subtotal * taxRate * 100) / 100;
        var total = Math.round((subtotal + tax) * 100) / 100;

        // Insert values into HTML
        $("#total").html(total);
        $("#subtotal").html(subtotal);
        $("#tax").html(tax);
    }

    // Change value > calculate
    $(".quantity").each(function() {
        $(this).change(calculate);
    });

    // Clear calculator > calculate
    $("#clear").click(function() {
        $("input").each(function() {
            $(this).val("");
        });
        calculate();
    });

    // Build/ Print page
    $("#print").click(function() {
        $("#print-section").html("");
        let printElem = "";

        // Append customer info to string
        $(".customer-info input").each(function() {
            printElem += "<h2>";
            printElem += $(this).attr('name') + ": " + $(this).val();
            printElem += "</h2>";
        });

        // Append table information to string
        printElem += "<table>";
        printElem += "<tr><th>Material</th><th>Item($)</th><th>Quantity</th></tr>";
        $(".items").each(function() {
            printElem += "<tr>";
            printElem += "<td>" + $(this).find(".item-name").text() + "</td>";
            printElem += "<td>" + $(this).find(".price").text() + "</td>";
            printElem += "<td>" + (parseInt($(this).find(".quantity").val()) || 0) + "</td>";
            printElem += "</tr>";
        });
        printElem += "<tr><td>Tax Rate</td><td>" + $("#tax-rate").text() +"</td></tr>";
        printElem += "</table>";

        // Append totals to string
        printElem += "<h1>Total: $" + $("#total").text() + "</h1>";
        printElem += "<h2>Subtotal: $" + $("#subtotal").text() + "</h2>";
        printElem += "<h2>Tax: $" + $("#tax").text() + "</h2>";

        // Append print string to page
        $("#print-section").append(printElem);
        window.print();
    });

    // Build/ Email string
    $("#send-email").click(function() {
        let emailString = "";

        // Append customer info to string
        $(".customer-info input").each(function() {
            emailString += $(this).attr('name') + ": " + $(this).val() + "%0D%0A";
        });
        emailString += "%0D%0A";

        // Append table info to string
        $(".items").each(function() {
            emailString += $(this).find(".item-name").text() + "($" + $(this).find(".price").text() + "): ";
            emailString += (parseInt($(this).find(".quantity").val()) || 0) + "%0D%0A";
        });
        emailString += "%0D%0A%0D%0ATotal: $" + $("#total").text();
        emailString += "%0D%0ASubtotal: $" + $("#subtotal").text();
        emailString += "%0D%0ATax: $" + $("#tax").text();

        // Create and direct to link
        var link = "mailto:aandbroofing1595@gmail.com"
        + "?cc="
        + "&subject=" + "Estimate Calculator"
        + "&body=" + emailString;
        
        window.location.href = link;
    });
});