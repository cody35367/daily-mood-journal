// Original reference: https://www.djangosnippets.org/snippets/1389/

function updateElementIndex(el, prefix, ndx) {
    var id_regex = new RegExp('(' + prefix + '-\\d+)');
    var replacement = prefix + '-' + ndx;
    if ($(el).prop("for")) $(el).prop("for", $(el).prop("for").replace(id_regex, replacement));
    if ($(el).prop("id")) $(el).prop("id", $(el).prop("id").replace(id_regex, replacement));
    if ($(el).prop("name")) $(el).prop("name", $(el).prop("name").replace(id_regex, replacement));
}

function addForm(btn, prefix) {
    var formCount = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
    var row = $('.' + prefix + '-dynamic-form:first').clone(true).get(0);
    $(row).removeAttr('id').insertAfter($('.' + prefix + '-dynamic-form:last')).children('.hidden').removeClass('hidden');
    var form_id_hidden = $(row).find('input[type=hidden]');
    updateElementIndex(form_id_hidden, prefix, formCount);
    $(form_id_hidden).prop("value", formCount+1);
    $(row).children().not(':last').children().each(function () {
        updateElementIndex(this, prefix, formCount);
        $(this).val('');
        if ($(this).is('ul[id$=-distortions]')){
            $(this).find('li').each(function(){
                var dist_label=$(this).find('label');
                updateElementIndex(dist_label, prefix, formCount);
                var dist_checkbox=$(this).find('input[type=checkbox]');
                updateElementIndex(dist_checkbox, prefix, formCount);
                $(dist_checkbox).prop("checked", false);
            });
        }
    });
    $(row).find('.delete-row').click(function () {
        deleteForm(this, prefix);
    });
    $('#id_' + prefix + '-TOTAL_FORMS').val(formCount + 1);
    return false;
}

function deleteForm(btn, prefix) {
    $(btn).parents('.' + prefix + '-dynamic-form').remove();
    var forms = $('.' + prefix + '-dynamic-form');
    $('#id_' + prefix + '-TOTAL_FORMS').val(forms.length);
    for (var i = 0, formCount = forms.length; i < formCount; i++) {
        var form_id_hidden = $(forms.get(i)).find('input[type=hidden]');
        updateElementIndex(form_id_hidden, prefix, i);
        $(form_id_hidden).prop("value", i+1);
        $(forms.get(i)).children().not(':last').children().each(function () {
            updateElementIndex(this, prefix, i);
            if ($(this).is('ul[id$=-distortions]')){
                $(this).find('li').each(function(){
                    var dist_label=$(this).find('label');
                    updateElementIndex(dist_label, prefix, i);
                    var dist_checkbox=$(this).find('input[type=checkbox]');
                    updateElementIndex(dist_checkbox, prefix, i);
                });
            }
        });
    }
    return false;
}

function setOtherTextState() {
    $('#emotion_forms_table > tbody > tr').each(function (index, tr) {
        var select_emotion = $(tr).find('select[id$=-emotion]')
        if (select_emotion.val() != "other") {
            $(tr).find('input[id$=-other_text').prop("disabled", true);
        } else {
            $(tr).find('input[id$=-other_text').prop("disabled", false);
        }
        select_emotion.change(setOtherTextState);
    });
}
