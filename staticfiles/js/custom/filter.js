
$(document).ready(function () {
    // Attach event handler to all checkboxes with class 'filter-checkbox'
    $('.filter-checkbox').change(updateFilters);

    function updateFilters() {
        // Get selected values for each filter
        var selectedCategories = getSelectedValues('.category-checkbox');
        var selectedBrands = getSelectedValues('.brand-checkbox');
        var selectedWarranty = getSelectedValues('.warranty-checkbox');
        var selectedSellers = getSelectedValues('.seller-checkbox');

        // Hide all products
        $('.product').hide();

        // Show products based on selected filters
        showProductsByFilter('category', selectedCategories);
        showProductsByFilter('brand', selectedBrands);
        showProductsByFilter('warranty', selectedWarranty);
        showProductsByFilter('seller', selectedSellers);

        // Show all products if no filters are selected
        if (selectedCategories.length === 0 && selectedBrands.length === 0 && selectedWarranty.length === 0 && selectedSellers.length === 0) {
            $('.product').show();
        }
    }

    function getSelectedValues(checkboxClass) {
        // Get an array of selected values for a given checkbox class
        return $(checkboxClass + ':checked').map(function () {
            return this.value;
        }).get();
    }

    function showProductsByFilter(filterType, selectedValues) {
        // Show products based on a specific filter type and selected values
        $.each(selectedValues, function (index, value) {
            $('.product.' + filterType + '-' + value).show();
        });
    }
});
