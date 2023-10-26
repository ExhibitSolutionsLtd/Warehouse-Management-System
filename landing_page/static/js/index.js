
document.getElementById('id_order_type').addEventListener('change', function() {
    if (this.value == 'inbound') {
        document.getElementById('div_id_supplier').style.display = 'block';
        document.getElementById('div_id_customer').style.display = 'none';
    } else {
        document.getElementById('div_id_supplier').style.display = 'none';
        document.getElementById('div_id_customer').style.display = 'block';
    }
});
