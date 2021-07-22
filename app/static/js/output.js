$(document).ready(function() {

  $("#artist-select").click(function() {
    $(".song-title, .song-artist, .song-icon").hide();
    $(".artist, .artist-icon").show();
    $("#popular-header").html("Your Favorite Artists");
    $("#artist-select").addClass("active-button");
    $("#song-select").removeClass("active-button");
  });

  $("#song-select").click(function() {
    $(".artist, .artist-icon").hide();
    $(".song-title, .song-artist, .song-icon").show();
    $("#popular-header").html("Your Favorite Songs");
    $("#song-select").addClass("active-button");
    $("#artist-select").removeClass("active-button");
  });
});
