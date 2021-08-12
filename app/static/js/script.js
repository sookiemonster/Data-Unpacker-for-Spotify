$(document).ready(function() {
  $("#choose-file").change(function() {
    var value = $("#choose-file").val();
    if (!value.endsWith(".zip")) {
      if (value == "" || value == undefined) {
        alert("Please select a file to upload.");
      } else {
        alert("Please select a zip file.");
        $("#choose-file").val('');
      }
      return false;
    } else if (value != "" && value != undefined) {
      $("#choose-text").html(
        "Selected File:"
      )
      console.log(value.split("\\").splice(-1,1)[0]);
      $("#file-selected").html(
        value.split("\\").splice(-1,1)[0]
      );
    }
  });

  $("#upload-file").click(function() {
    var value = $("#choose-file").val();
    if (value == "" || value == undefined) {
      alert("Please select a file to upload.");
      return false;
    } else {
      // Transition
      $("#wave-container").css({
        "transition" : "width 0.5s ease-in",
        "width" : "110vw",
        "z-index" : "-1" });

      setTimeout(function() {
        $("#wave-container").css("transition", "").hide();
        $("body").css("background", "black");
      }, 550);
      $(".layout-container").fadeOut('slow');
    }
  });
});
