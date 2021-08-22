$(document).ready(function() {
  
  // Resest File Chooser on Load
  $("#choose-file").val("");

  // Open Info Page
  $(".info").click(function() {
    $("#wave-container").css({
      "transition" : "width 0.6s ease",
      "width" : "0vw",
      "z-index" : "-1" });

    $(".header-container").addClass("slide-left");
    $("#file-page").addClass("slide-right");

    setTimeout(function() {
      $("#info-page").fadeIn(500);
    }, 250);
  });

  // Close Info Page
  $("#close-button").click(function() {
    $("#info-page").fadeOut(200);

    $(".header-container").removeClass("slide-left");
    $("#file-page").removeClass("slide-right");

    $("#wave-container").css({
      "transition" : "width 0.6s ease",
      "width" : "53vw",
      "z-index" : "-1" });
    
    setTimeout(function() {
      $("#wave-container").css("transition", "");
    }, 600);
  });

  // Change File Chooser Text on Upload
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


  // Upload File
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
