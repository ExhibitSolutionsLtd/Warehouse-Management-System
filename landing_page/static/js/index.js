
// show and hide supplier and customer divs when the value for order type is inbound or outbound
orderBtn = document.getElementById('orderBtn')


if (orderBtn!=null){
    orderBtn.addEventListener('click', ()=>{
        let input = document.getElementById("id_order_type")
        input.disabled = true
        input.value = "Inbound"
        document.getElementById('div_id_supplier').style.display = 'block';
        document.getElementById('div_id_customer').style.display = 'none';
    })
}




// if (order_type_elem!=null){
//     order_type_elem.addEventListener('change', function() {
//         if (this.value == 'Inbound') {
//             document.getElementById('div_id_supplier').style.display = 'block';
//             document.getElementById('div_id_customer').style.display = 'none';
//             div_id_supplier.querySelector('select').required = true;
//             div_id_customer.querySelector('select').required = false;
//         } else {
//             document.getElementById('div_id_supplier').style.display = 'none';
//             document.getElementById('div_id_customer').style.display = 'block';
//             div_id_supplier.querySelector('select').required = false;
//             div_id_customer.querySelector('select').required = true;
//         }
//     });
// }


// functionality for the Orders Tabs

function openTab(tabName, elmnt) {
    // Hide all tab contents
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    // Remove the background color of all tab links/buttons
    tablinks = document.getElementsByClassName("tablink");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    // Show the specific tab content and set the button to active
    document.getElementById(tabName).style.display = "block";
    elmnt.className += " active";
}

// Default open the first tab
let tablink = document.getElementsByClassName('tablink')[0]
if (tablink!=null){
    tablink.click();
}

let status_elems = document.querySelectorAll(".orderStatus");
//loop through each element in nodelist
status_elems.forEach((status_elem)=>{
    // Check the text content of each element
    if (status_elem.textContent.trim() === "Pending") {
        status_elem.style.backgroundColor = "red";
        status_elem.style.color = "white";
    } else if(status_elem.textContent.trim() === "Processing"){
        status_elem.style.backgroundColor = "yellow";
        status_elem.style.color = "black";
    } else{
        status_elem.style.backgroundColor = "green";
        status_elem.style.color = "white";
    }
})


// modify rows attribute value in text area elements
let textareaDivs = document.querySelectorAll(".textarea");
textareaDivs.forEach((textareaDiv)=>{
    textareaDiv.rows = "4";
})
//function that triggers printing of document
function printDocument() {
    printJS('productTbl', 'html');
  }

  document.addEventListener("DOMContentLoaded", function() {
    // Get the sidebar and toggle button elements
    var sidebar = document.getElementById("sidebar");
    var toggleSidebarButton = document.getElementById("toggleSidebar");

    // Add click event listener to the toggle button
    toggleSidebarButton.addEventListener("click", function() {
        // Toggle the "closed" class based on its presence
        if (sidebar.classList.contains("closed")) {
            sidebar.classList.remove("closed");
            toggleSidebarButton.classList.remove("closed")
        } else {
            sidebar.classList.add("closed");
            toggleSidebarButton.classList.add("closed")
        }
    });
});


//jQuery
$(document).ready(()=>{
    $("#printme").click(()=>{
        $("#header").append("<legend>Inventory List</legend>")
        $(".actions").remove()
        $("#printableContent").printThis({
            pageTitle:"Receipt"
        });
        $(".actions").add()
    });
});
  

// console.log(textareaDivs)
// alert('Hello')