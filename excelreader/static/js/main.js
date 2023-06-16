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

const addButton = document.getElementById('addButton');
const minusButton = document.getElementById('minusButton');
const hiddenColumns = document.getElementsByClassName('hidden-column');

    addButton.addEventListener('click', function () {
        for (let i = 0; i < hiddenColumns.length; i++) {
            // if (hiddenColumns[i].style.display === 'none') {
            //     hiddenColumns[i].style.display = 'table-cell';
            //     foldButton.textContent = 'Fold';
            // } else {
            //     hiddenColumns[i].style.display = 'none';
            //     foldButton.textContent = 'Unfold';
            // }
            hiddenColumns[i].style.display = 'table-cell';
        }
    });

    minusButton.addEventListener('click', function(){
        addButton.style.display = 'none';
        for (let i=0; i<hiddenColumns.length; i++){
            hiddenColumns[i].style.display = 'none';
        }
    })