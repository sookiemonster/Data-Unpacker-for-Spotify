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
    if($(window).width() > 500){
      $(".artist-count").show();
    }  

    $(".song-title, .song-artist, .track-img, .track-count, .clip-container").hide();
    $(".artist, .artist-img").show();
    $("#popular-header").html("Your Favorite Artists");
    $("#artist-select").addClass("active-button");
    $("#song-select").removeClass("active-button");
  });

  $("#song-select").click(function() {
    if($(window).width() > 500){
      $(".track-count").show();
    }

    $(".artist, .artist-count, .artist-img").hide();
    $(".song-title, .song-artist, .track-img, .clip-container").show();
    $("#popular-header").html("Your Favorite Songs");
    $("#song-select").addClass("active-button");
    $("#artist-select").removeClass("active-button");
  });

  $(window).on("resize",function() {  
    if($(window).width() <= 500) {
      $(".track-count").hide();
      $(".artist-count").hide();
    } else {
      if ($("#song-select").hasClass("active-button")) {
        $(".track-count").show();
      } else {
        $(".artist-count").show();
      }
    }
 });

});
