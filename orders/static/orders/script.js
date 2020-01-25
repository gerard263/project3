
function categoryChange() {
    var category = document.getElementById("categorySelect").value;
    if (category === 'Pizza') {
        showsizes();
        showpizzatypes();
        showtoppings();
    }
    //alert(`${category}`);
};
function showsizes() {
    var sizeshtml = `
    <select id="sizesSelect">
        {% for size in sizes %}
        <option value="{{ size }}">{{ size }}</option>
        {% endfor %}
    </select>`
    document.getElementById("sizesid").innerHTML = sizeshtml;
    //alert(`${sizeshtml}`);
};
document.addEventListener('DOMContentLoaded', () => {        
$('input[type=checkbox]').on('change', function (e) {            
    if ($('input[type=checkbox]:checked').length > 5) {
        $(this).prop('checked', false);
        alert("allowed only 5");
    }
    });         
});
