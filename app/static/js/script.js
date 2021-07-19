$(document).ready(function() {
  $("#choose-file").change(function() {
    var value = $("#choose-file").val();
    if (value != "" && value != undefined) {
      $("#choose-text").html(
        "Selected File:"
      )

      $("#file-selected").html(
        value.split("\\").splice(-1,1)[0]
      );
    }
  });

  $("#upload-file").click(function() {
    var value = $("#choose-file").val();
    if (value == "" || value == undefined) {
      alert("Please select a file to upload");
      return false;
    }
  })
});
