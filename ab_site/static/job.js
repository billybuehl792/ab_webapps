function toggleWork() {
    var workSection = document.getElementById("work-section");
    var workOption = document.getElementById("work-option");

    workSection.classList.add("inactive");

    if (workOption.checked == true) {
        workSection.classList.remove("inactive");
    } else {
        workSection.classList.add("inactive");
    }

    workOption.addEventListener("change", ()=> {
        //toggle work section
        workSection.classList.toggle("inactive");
    });
}

function toggleTime() {
    var timeOption = document.getElementById("time-option");
    var duration = document.getElementById("duration");
    var startComplete = document.getElementById("start-complete");

    startComplete.classList.toggle("inactive");

    if (timeOption.checked == true) {
        startComplete.classList.remove("inactive");
        duration.classList.add("inactive");
        // clear duration field
    } else {
        startComplete.classList.add("inactive");
        duration.classList.remove("inactive");
    }

    timeOption.addEventListener("change", () => {
        duration.classList.toggle("inactive");
        startComplete.classList.toggle("inactive");
    });
}

const job = () => {
    toggleWork();
    toggleTime();
}