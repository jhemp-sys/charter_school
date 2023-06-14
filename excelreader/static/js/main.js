function toggleTab(tabNumber) {
    var contentDivs = document.getElementsByClassName("excel-content");
    var tabs = document.getElementsByClassName("excel-tab");
    for (var i = 0; i < contentDivs.length; i++) {
    contentDivs[i].classList.remove("active");
    tabs[i].classList.remove("active");
    }
    document.getElementById("content" + tabNumber).classList.add("active");
    tabs[tabNumber - 1].classList.add("active");
}