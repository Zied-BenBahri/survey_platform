$(document).ready(function () {
    $("#id_delegation").change(function () {
        var delegationId = $(this).val();
        if (delegationId) {
            $.ajax({
                url: "/enquete/load-localites",
                data: { delegation_id: delegationId },
                success: function (data) {
                    $("#id_localite").html(data);
                },
            });
        } else {
            $("#id_localite").html('<option value="">Select a delegation first</option>');
        }
    });
});
