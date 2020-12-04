function calculate() {
    // calculate totals
    var subtotal = 0;
    var inputItems = document.querySelectorAll(".items .item");
    var taxRate = document.getElementById("tax").innerHTML;

    inputItems.forEach((item) => {
        let priceNum = item.querySelector(".price .priceNum").innerHTML;
        let multiplier = item.querySelector(".quantity input").value
        subtotal += priceNum * multiplier;
    });

    var tax = (subtotal * taxRate);
    var total = subtotal + tax;
    
    document.getElementById("totalVal").innerHTML = Math.round(total * 100) / 100;
    document.getElementById("subtotalVal").innerHTML = Math.round(subtotal * 100) / 100;
    document.getElementById("taxVal").innerHTML = Math.round(tax * 100) / 100;
}

function calculator() {
    //create event listeners
    var inputItems = document.querySelectorAll(".items .item");

    inputItems.forEach((item) => {
        item.querySelector(".quantity input").addEventListener("change", calculate);
    });
}

function clear() {
    var clearButton = document.getElementById("clear");
    var inputItems = document.querySelectorAll(".items .item");

    //clear form
    clearButton.addEventListener("click", () => {
        inputItems.forEach((item) => {
            item.querySelector(".quantity input").value = "";
        document.getElementById("customer").value="";
        document.getElementById("address").value="";
        document.getElementById("phone").value = "";
        document.getElementById("email").value = "";
        });
        calculate();
    });
}

function printForm() {
    //open print options with formatted calc
    var printButton = document.getElementById("print");
    var printSection = document.getElementById("printSection");

    function getPrintString() {
        let printElem = "";
        
        if (document.getElementById("customer").value != "") {
            printElem += "<p>" + "Customer: " + document.getElementById("customer").value + "</p>";
        }
        if (document.getElementById("address").value != "") {
            printElem += "<p>" + "Customer Address: " + document.getElementById("address").value + "</p>";
        }
        if (document.getElementById("phone").value != "") {
            printElem += "<p>" + "Customer Phone: " + document.getElementById("phone").value + "</p>";
        }
        if (document.getElementById("email").value != "") {
            printElem += "<p>" + "Customer Email: " + document.getElementById("email").value + "</p>";
        }
        
        printElem += "<table><tr><th>Material</th><th>Item($)</th><th>Quantity</th></tr>";
        document.querySelectorAll(".items .item").forEach((item) => {
            if(item.querySelector(".quantity input").value != "") {
                printElem += "<tr>";
                printElem += "<td>" + item.querySelector(".itemName").innerHTML + "</td>";
                printElem += "<td>" + "$" + item.querySelector(".price .priceNum").innerHTML + "</td>";
                printElem += "<td>" + item.querySelector(".quantity input").value + "</td>";
                printElem += "</tr>";
            }
        });
    
        printElem += "</table>";
    
        printElem += "<h1>Total: $" + document.getElementById("totalVal").innerHTML + "</h1>";
        printElem += "<h2>Subtotal: $" + document.getElementById("subtotalVal").innerHTML + "</h2>";
        printElem += "<h2>Tax: $" + document.getElementById("taxVal").innerHTML + "</h2>";

        return(printElem);
    }

    printButton.addEventListener("click", () => {
        printSection.innerHTML = getPrintString();
        window.print();
        printSection.innerHTML = "";
    });
}

function emailForm() {
    var emailButton = document.getElementById("sendEmail");

    //compose and send email to a&b roofing
    emailButton.addEventListener("click", () => {
        let emailString = "";

        if (document.getElementById("customer").value != "") {
            emailString += "Customer: " + document.getElementById("customer").value + "%0D%0A";
        }
        if (document.getElementById("address").value != "") {
            emailString += "Customer Address: " + document.getElementById("address").value + "%0D%0A";
        }
        if (document.getElementById("phone").value != "") {
            emailString += "Customer Phone: " + document.getElementById("phone").value + "%0D%0A";
        }
        if (document.getElementById("email").value != "") {
            emailString += "Customer Email: " + document.getElementById("email").value + "%0D%0A%0D%0A";
        }
        
        document.querySelectorAll(".items .item").forEach((item) => {
            if(item.querySelector(".quantity input").value != '') {
                emailString += item.querySelector(".itemName").innerHTML + "(";
                emailString += "$" + item.querySelector(".price .priceNum").innerHTML + "): ";
                emailString += item.querySelector(".quantity input").value + "%0D%0A";
            }
        });

        emailString += "%0D%0ATotal: $" + document.getElementById("totalVal").innerHTML + "%0D%0A";
        emailString += "Subtotal: $" + document.getElementById("subtotalVal").innerHTML + "%0D%0A";
        emailString += "Tax: $" + document.getElementById("taxVal").innerHTML + "%0D%0A";

        var link = "mailto:aandbroofing1595@gmail.com"
        + "?cc="
        + "&subject=" + "Estimate Calculator"
        + "&body=" + emailString;
        
        window.location.href = link;
    });
}


const calc = () => {
    calculator();
    clear();
    printForm();
    emailForm();
}