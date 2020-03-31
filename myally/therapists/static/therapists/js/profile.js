window.addEventListener('DOMContentLoaded', (event) => {
    var form = $("#form-activity");
    var online = $("#id_online");
    var busy = $("#id_busy");

    online.click(function(e) {
        uncheck_busy();
        form.submit();
    });

    busy.click(function(e) {
        if (!uncheck_busy()) {
            form.submit();
        }
    });

    var uncheck_busy = function() {
        if (!online.is(":checked") && busy.is(":checked")) {
            busy.prop("checked", false);
            return true
        }
    }

    form.on("submit", function(e) {
        e.preventDefault();
        $.post("/therapist/profile/save_status", $(this).serialize())
    });

    if (uncheck_busy()) {
        // might happen that database has online=false and busy=true
        form.submit()
    }
})
