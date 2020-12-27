function makeCheckList(){
    $('#thought_forms_table > tbody > tr').each(function (index, tr) {
        $(tr).find('ul[id$=-distortions] > li').each(function (index, li){
            var distortion_checkbox = $(li).find('input[type=checkbox]')
            if(distortion_checkbox.is(':checked')){
                distortion_checkbox.remove();
            } else {
                li.remove();
            }
        });
    });
}
