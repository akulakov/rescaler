$(document).on('change', 'select', function() {
    console.log($(this).val()); // the selected options’s value

    // if you want to do stuff based on the OPTION element:
    var item1 = $(this).find('#id_item1 option:selected')[0];
    var item2 = $(this).find('#id_item2 option:selected')[0];

    var item1 = $('#id_item1').find('option:selected')[0].value;
    var item2 = $('#id_item2').find('option:selected')[0].value;
    console.log(item1);
    console.log(item2);

    $.ajax({
        type: "POST",
        url: "/do_rescale/",
        data: { item1: item1, item2: item2, }
      })
        .done(function( items ) {
          // alert( "msg: " + msg );
          if (items) {
            $('#items').html(items['items']);
          }
    });
});
