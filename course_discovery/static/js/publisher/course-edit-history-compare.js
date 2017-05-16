$(document).ready(function () {
    $('.history').each(function () {
        if ($('#id_history_revision').val() > 0) {
            var dmp = new diff_match_patch();
            var element_id = this.id.split('_revision')[0];

            var current_course_object = $('#' + element_id).val();
            var history_object_value = $(this).val().trim();

            var d = dmp.diff_main(history_object_value, current_course_object);
            dmp.diff_cleanupEfficiency(d)
            tinymce.get(element_id).setContent(decodeEntities(dmp.diff_prettyHtml(d)))
        }
    });
});

function decodeEntities(encodedString) {
    var textArea = document.createElement('textarea');
    textArea.innerHTML = encodedString;
    return textArea.value;
}