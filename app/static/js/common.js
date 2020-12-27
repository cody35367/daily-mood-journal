function addDistortionTooltips(distDict){
    $('#thought_forms_table > tbody > tr').each(function (index, tr) {
        $(tr).find('ul[id$=-distortions] > li > label').each(function (index, label){
            $(label).prop("title",distDict[$(label).text().trim()]);
        });
    }); 
}
