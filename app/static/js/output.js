$(document).ready(function () {

  // var top_expanded = false;

  $(".artist, .artist-img, .artist-count").hide();

  $("#icon-image").filter(function() {
    return $(this).attr('src')==='';
  }).hide();

  $("#no-icon").filter(function() {
    return $("#icon-image").attr('src')!='';
  }).hide();

  $("#artist-select").click(function() {
    $(".song-title, .song-artist, .track-img, .track-count").hide();
    $(".artist, .artist-img, .artist-count").show();
    $("#popular-header").html("Your Favorite Artists");
    $("#artist-select").addClass("active-button");
    $("#song-select").removeClass("active-button");
  });

  $("#song-select").click(function() {
    $(".artist, .artist-img, .artist-count").hide();
    $(".song-title, .song-artist, .track-img, .track-count").show();
    $("#popular-header").html("Your Favorite Songs");
    $("#song-select").addClass("active-button");
    $("#artist-select").removeClass("active-button");
  });

  $("#expand-button").click(function() {
    $(".top-list li:nth-of-type(1n + 6)").toggle();
    if ($("#expand-arrow").hasClass("flip")) {
      $("#expand-arrow").removeClass("flip");
    } else {
      $("#expand-arrow").addClass("flip");
    }
  });
});
