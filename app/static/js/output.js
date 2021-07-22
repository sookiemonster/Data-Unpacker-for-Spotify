$(document).ready(function () {

  $("#artist-select").click(function () {
    $(".song-title, .song-artist, .track-img").hide();
    $(".artist, .artist-img").show();
    $("#popular-header").html("Your Favorite Artists");
    $("#artist-select").addClass("active-button");
    $("#song-select").removeClass("active-button");
  });

  $("#song-select").click(function () {
    $(".artist, .artist-img").hide();
    $(".song-title, .song-artist, .track-img").show();
    $("#popular-header").html("Your Favorite Songs");
    $("#song-select").addClass("active-button");
    $("#artist-select").removeClass("active-button");
  });
});
