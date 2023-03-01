
/////////////////////////////////////////////////////////////
/////  Function to show or hide DIVs panel in general   /////
/////  when is defined as off, it will stop at a        /////
/////  minimum height, wont completeley disappear       /////
/////////////////////////////////////////////////////////////

 function expandOtherDiv(element) {
  const panelID = element.id + "Target"
  const panel = document.getElementById(element.id+"Target");
  if (panel.className == "expandOtherDivOff") {
    panel.className = "expandOtherDivOn";
  } else {
    panel.className = "expandOtherDivOff";
  }
}


/////////////////////////////////////////////////////////////
/////  Function to show or hide DIVs panel in general   /////
/////  similar to previous function, mas just turns on  /////
/////  or off.                                          /////
/////////////////////////////////////////////////////////////

function hideOtherDiv(element) {
  const panelID = element.id + "Target"
  const panel = document.getElementById(element.id+"Target");
  if (panel.style.display == "none") {
    panel.style.display = "inline-block";
  } else {
    panel.style.display = "none";
  }
}



/////////////////////////////////////////////////////////////
/////  Function to show or hide DIVs panel in general   /////
/////  similar to previous function, mas just turns on  /////
/////  or off.                                          /////
/////////////////////////////////////////////////////////////
function detailsExpand() {
    const element = document.getElementById("details-page");
    if (element.className == "desligado") {
      element.className = "ligado";
    } else {
      element.className = "desligado";
    }
  }



//////////////////////////////////////////////////////////////////
/////       function to show or hide the details panel       /////
//////////////////////////////////////////////////////////////////
////   DATA to copy: record_id,user_id,Genres,Title,Rating,  /////
////   Duration,Type,Platform,Trailer,Country,Writer,Cast,   /////
////   Poster,Watched,Plot,Comment,Year                      /////
//////////////////////////////////////////////////////////////////

function showDetails(selectedItem) {
  // Get specific movie attributes from the current selected item
  const detailsPage = document.getElementById("details-page");
  let dId = selectedItem.getAttribute("dId")
  let dGenres = selectedItem.getAttribute("dGenres")
  let dTitle = selectedItem.getAttribute("dTitle")
  let dRating = selectedItem.getAttribute("dRating")
  let dDuration = selectedItem.getAttribute("dDuration")
  let dType = selectedItem.getAttribute("dType")
  let dPlatform = selectedItem.getAttribute("dPlatform")
  let dTrailer = selectedItem.getAttribute("dTrailer")
  let dCountry = selectedItem.getAttribute("dCountry")
  let dWriter = selectedItem.getAttribute("dWriter")
  let dCast = selectedItem.getAttribute("dCast")
  let dPoster = selectedItem.getAttribute("dPoster")
  let dWatched = selectedItem.getAttribute("dWatched")
  let dPlot = selectedItem.getAttribute("dPlot")
  let dComment = selectedItem.getAttribute("dComment")
  let dYear = selectedItem.getAttribute("dYear")

  // If movie trailer is empty, hide that section
  if (dTrailer == "") {
    document.getElementById("divTrailer").className = "desligado";
  }
  else {
    document.getElementById("divTrailer").className = "ligado";   
  }

  // If details tab is closed, open it
  if (detailsPage.className == "desligado") {  
    detailsPage.className = "ligado";
    document.getElementById("recordIdEdit").value = dId;
    document.getElementById("recordIdDelete").value = dId;
    document.getElementById("recordIdWatched").value = dId;
    document.getElementById("dGenres").innerHTML = dGenres;
    document.getElementById("dTitle").innerHTML = dTitle;
    document.getElementById("dRating").innerHTML = dRating;
    document.getElementById("dDuration").innerHTML = dDuration;
    document.getElementById("dType").innerHTML = dType;
    document.getElementById("dPlatform").innerHTML = dPlatform;
    document.getElementById("dTrailer").src = dTrailer;
    document.getElementById("dCountry").innerHTML = dCountry;
    document.getElementById("dWriter").innerHTML = dWriter;
    document.getElementById("dCast").innerHTML = dCast;
    document.getElementById("dPoster").src = dPoster;
    document.getElementById("dWatched").innerHTML = dWatched;
    document.getElementById("dPlot").innerHTML = dPlot;
    document.getElementById("dComment").innerHTML = dComment;
    document.getElementById("dYear").innerHTML = dYear;
    
  // If details tab is already opened, close it first, wait 0.75 s and call the function again, to open it, with new info
  } else if (detailsPage.className == "ligado") {  
    detailsPage.className = "desligado";
    //turn off trailer from playing in the background
    document.getElementById("dTrailer").innerHTML = "";
    const myTimeout = setTimeout(function () {showDetails(selectedItem);}, 750);
  }
}


/////////////////////////////////////////////////
/////  Copy IMDB search to new entry form   /////
/////////////////////////////////////////////////

function copyValueToForm() {
  // Movie Title
  let labelTitle = document.getElementById("searchLabelMovieTitle").getAttribute("form-data");
  let elementTextMovieTitle = document.getElementById("textMovieTitle").value = labelTitle;
  
  // Movie Type
  let labelType = document.getElementById("searchLabelMovieType").getAttribute("form-data");
  if (labelType == "tv series"){
    let optionMovieTypeTvseriesElement = document.getElementById("optionMovieTypeTvseries");
    optionMovieTypeTvseriesElement.selected="on";}
    else if (labelType == "movie") {
    let optionMovieTypeMovieElement = document.getElementById("optionMovieTypeMovie");
    optionMovieTypeMovieElement.selected="on";}
  
    // Movie Duration
  let labelDuration = document.getElementById("searchLabelMovieDuration").getAttribute("form-data");
  labelDuration = Number(labelDuration);
  if (labelDuration <= "30"){
    document.getElementById("optionMovieDuration30").selected="on";}
  else if (labelDuration <= "45"){
    document.getElementById("optionMovieDuration45").selected="on";}
  else if (labelDuration <= "60"){
    document.getElementById("optionMovieDuration60").selected="on";}
  else if (labelDuration <= "90"){
    document.getElementById("optionMovieDuration90").selected="on";}
  else if (labelDuration <= "105"){
    document.getElementById("optionMovieDuration105").selected="on";}
  else if (labelDuration <= "120"){
    document.getElementById("optionMovieDuration120").selected="on";}
  else if (labelDuration <= "135"){
    document.getElementById("optionMovieDuration135").selected="on";}
  else if (labelDuration > "135"){
    document.getElementById("optionMovieDuration150").selected="on";}
  
  // Movie Rating
  let labelRating = document.getElementById("searchLabelMovieRating").getAttribute("form-data");
  document.getElementById("textMovieRating").value = labelRating;

  // Movie Country
  let labelCountry = document.getElementById("searchLabelMovieCountry").getAttribute("form-data");
  document.getElementById("textMovieCountry").value = labelCountry;
  
  // Movie Writer
  let labelWriter = document.getElementById("searchLabelMovieWriter").getAttribute("form-data");
  document.getElementById("textMovieWriter").value = labelWriter;

  // Movie Plot
  let labelPlot = document.getElementById("searchLabelMoviePlot").getAttribute("form-data");
  document.getElementById("textMoviePlot").value = labelPlot;

  // Movie Writer
  let labelCast = document.getElementById("searchLabelMovieCast").getAttribute("form-data");
  document.getElementById("textMovieCast").value = labelCast;
 
  // Movie Poster
  let labelImage = document.getElementById("searchLabelImageurl").getAttribute("form-data");
  document.getElementById("textMoviePoster").value = labelImage;

  // Movie Poster
  let labelYear = document.getElementById("searchLabelMovieYear").getAttribute("form-data");
  document.getElementById("textMovieYear").value = labelYear;
  
  // Movie Genres
  for (let i = 0; i < genreList.length; i++) {
    for (let j = 0; j < genreMovie.length; j++) {
      if (genreList[i] == genreMovie[j]) {
        let temporaryID = "cbGenre" + genreMovie[j];
        const checkbox = document.getElementById(temporaryID);
        checkbox.checked = "true";
      }
    }
  }
}



////////////////////////////
/////   Filter cards   /////
////////////////////////////

// Create three NodeLists: genres, duration and items
const cboxesGenres = document.querySelectorAll("input[name='cbGenre']");
const cboxesDuration = document.querySelectorAll("input[name='cbDuration']");
const items = document.querySelectorAll(".item");

// Create array of genres, for each item showed in index.html page, delivered by the Records database table
let itemsGenreList = [];
let itemsDurationList = [];
const lenItem = items.length;
for (let j = 0; j < lenItem; j++){
  itemsGenreList.push(items[j].getAttribute("dGenres").split(','));
  itemsDurationList.push(items[j].getAttribute("dDuration"));
}

// Call to action at each time a change occurs in the checkboxes state
cboxesGenres.forEach(function (cbox){
  cbox.addEventListener("change", updateFilters)
});

cboxesDuration.forEach(function (cbox){
  cbox.addEventListener("change", updateFilters)
});

// Whenever a checkbox is changed, this function will update the list of current checkboxes values
function updateFilters() {
  // Update cboxSelectedGenresList to current selected genres
  let cboxSelectedGenreList = [];
  const lenGenre = cboxesGenres.length;
  for (let i = 0; i < lenGenre; i++){
    if (cboxesGenres[i].checked == true ){
      cboxSelectedGenreList.push(cboxesGenres[i].value);
    }
  }

  // Update cboxSelectedDurationList to current selected genres
  let cboxSelectedDurationList = [];
  const lenDuration = cboxesDuration.length;
  for (let i = 0; i < lenDuration; i++){
    if (cboxesDuration[i].checked == true ){
      cboxSelectedDurationList.push(cboxesDuration[i].value);
    }
  }  
 
  let lenSelGenre = cboxSelectedGenreList.length;
  let lenSelDuration = cboxSelectedDurationList.length;

  //Search if items have the selected checkboxes genres
  for (let j = 0; j < lenItem; j++){
    items[j].style.display = "inline-block";  // cleans all genre filters at each iteration
    for (let i = 0; i < lenSelGenre; i++){        
      if (!itemsGenreList[j].includes(cboxSelectedGenreList[i])){
        items[j].style.display = "none";
      }
    }

     //Search if items have the selected checkboxes duration
    for (let k = 0; k < lenSelDuration; k++){        
      if (!cboxSelectedDurationList[k].includes(itemsDurationList[j])){
        items[j].style.display = "none";
      }
    }
  }
}


