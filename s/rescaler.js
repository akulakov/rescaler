$(document).on('change', 'select', function() {
    var item1 = $('#id_item1').find('option:selected')[0].value;
    var item2 = $('#id_item2').find('option:selected')[0].value;

    $.ajax({
        type: "POST",
        url: "/do_rescale/",
        data: { item1: item1, item2: item2, }
      })
        .done(function( items ) {
          if (items) {
            $('#items').html(items['items']);
          }
    });
});
