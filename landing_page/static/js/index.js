
// show and hide supplier and customer divs when the value for order type is inbound or outbound

document.getElementById('id_order_type').addEventListener('change', function() {
    if (this.value == 'inbound') {
        document.getElementById('div_id_supplier').style.display = 'block';
        document.getElementById('div_id_customer').style.display = 'none';
    } else {
        document.getElementById('div_id_supplier').style.display = 'none';
        document.getElementById('div_id_customer').style.display = 'block';
    }
});


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
document.getElementsByClassName('tablink')[0].click();

