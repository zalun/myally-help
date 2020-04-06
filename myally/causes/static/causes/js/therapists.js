window.addEventListener('DOMContentLoaded', (event) => {
    $('#reload_button').click(function() {
        location.reload();
    });
    $('[data-toggle="tooltip"]').tooltip()
    $(".therapists .disabled .a").click(function(e) {
        e.stopPropagation();
        e.preventDefault();
    });
    $("#invite_therapist_form .btn").click(function(e) {
        alert("YEAH");
        $("#invite_therapist_form").submit();
    });
})
