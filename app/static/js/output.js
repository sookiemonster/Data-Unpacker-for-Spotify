$(document).ready(function() {

  $("#artist-select").click(function() {
    $(".song-title, .song-artist").hide();
    $(".artist").show();
    $("#popular-header").html("Your Favorite Artists");
  });

  $("#song-select").click(function() {
    $(".artist").hide();
    $(".song-title, .song-artist").show();
    $("#popular-header").html("Your Favorite Songs");
  });
});
