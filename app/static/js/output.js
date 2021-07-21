$(document).ready(function () {

  $(".artist-img").hide();

  $("#artist-select").click(function () {
    $(".song-title, .song-artist, .track-img").hide();
    $(".artist, .artist-img").show();
    $("#popular-header").html("Your Favorite Artists");
  });

  $("#song-select").click(function () {
    $(".artist, .artist-img").hide();
    $(".song-title, .song-artist, .track-img").show();
    $("#popular-header").html("Your Favorite Songs");
  });
});
