document.addEventListener('DOMContentLoaded', function() {

  var x = document.getElementsByName("Poetry");
var i;

for (i = 0; i < x.length; i++) {

x[i].className = "card text-white bg-secondary mb-3";
x[i].getElementsByTagName("A")[0].className = "text-primary";
x[i].getElementsByTagName("A")[1].className = "text-primary";

} 
var y = document.getElementsByName("Fiction");
var i;
for (i = 0; i < y.length; i++) {
y[i].getElementsByTagName("P")[0].className = "lead";
} 

/*
var all = document.getElementsById("All");
var fiction = document.getElementsById("Fiction");
var philo = document.getElementsById("Philosophy");
var poetry = document.getElementsById("Poetry");

if (all.dataset.genre != "All") {

all.className = "tab-pane fade";
document.getElementById("navAll").className = "nav-link";

if (fiction.dataset.genre == "Fiction") {

  fiction.className = "tab-pane fade show active";
  document.getElementById("navFiction").className = "nav-link active";

}

if (philo.dataset.genre == "Philosophy") {

  philo.className = "tab-pane fade show active";
  document.getElementById("navPhilo").className = "nav-link active";

}

if (poetry.dataset.genre == "Poetry") {

  poetry.className = "tab-pane fade show active";
  document.getElementById("navPoetry").className = "nav-link active";

}

} 

*/





let input = document.getElementById("search");
     
input.onkeyup = function() {

let word = input.value;
var list = document.getElementById("found"); 

if (word == ""){

while (list.firstChild) {
list.removeChild(list.firstChild);
}
}



fetch(`/search/${word}`)
.then(response => response.json())
.then(found => {
found.forEach(element => {



let author = `${element.author}`;
let book = `${element.book}`;
let lowerword = word.toLowerCase();



if (author.toLowerCase().includes(lowerword)) {




let opt2 = document.createElement('option');
opt2.innerHTML = `${element.author}`;
document.getElementById("found").append(opt2);

let options = []

document.querySelectorAll('#found > option').forEach((option) => {
  if (options.includes(option.value)) option.remove()
  else options.push(option.value)
})

}
if (book.toLowerCase().includes(lowerword)) {
let opt3 = document.createElement('option');
opt3.innerHTML = `${element.book}`;
document.getElementById("found").append(opt3);

let options = []

document.querySelectorAll('#found > option').forEach((option) => {
  if (options.includes(option.value)) option.remove()
  else options.push(option.value)
})
}


});

});

};
})


function newExcerpt(){

  
 
  fetch(`/maxday`)
    .then(response => response.json())
    .then(created => {
      var todaytot = `${created}`
      if (todaytot == 3) {
        document.getElementById("nomore").style.display = "block";

      }
      else{document.getElementById("newexcerptform").style.display = "block";}
  });
   }
   

function editExcerpt(thisexcerpt){
    document.getElementById(`editexcerptform${thisexcerpt}`).style.display = "block";
    var txt = document.getElementById(`text${thisexcerpt}`);
    var author = document.getElementById(`author${thisexcerpt}`);
    var book = document.getElementById(`book${thisexcerpt}`);
    var genre = document.getElementById(`genre${thisexcerpt}`);
    document.getElementById(`edittext${thisexcerpt}`).value = txt.dataset.text;
    document.getElementById(`editauthor${thisexcerpt}`).value = author.dataset.thisauthor;
    document.getElementById(`editbook${thisexcerpt}`).value = book.dataset.thisbook;
    document.getElementById(`editgenre${thisexcerpt}`).value = genre.dataset.thisgenre;
   }
   
   function closeForm(item){
     var thisitem = item.name;
     document.getElementById(thisitem).style.display = "none";

     
    
    
   }

   function alertDelete(thisexcerpt){
    
    document.getElementById(`deleteornot${thisexcerpt}`).style.display = "block";

    
   
   
  }

   function deletethis(thisexcerpt) {

    document.getElementById(`excerpt${thisexcerpt}`).style.display = "none";
    document.getElementById(`all${thisexcerpt}`).style.display = "none";

        fetch(`/delete/${thisexcerpt}`, {
        method: 'POST',
        
      })
      
      
    }  
    function unsentRewards(){
      document.getElementById("unsent").style.display = "block"
      fetch(`/rewardlist`)
      .then(response => response.json())
      .then(rewards => {
      rewards.forEach(reward => {
        
      let opt = document.createElement('option');
      opt.innerHTML = `${reward.title} (won by ${reward.user})`;
      opt.value = `${reward.id}`;
      document.getElementById("rewards").append(opt);
      let options = []
    
    document.querySelectorAll('#rewards > option').forEach((option) => {
        if (options.includes(option.value)) option.remove()
        else options.push(option.value)
    })
      
      });
      
      });
                
    }
    
    function sendReward() {

      if (document.getElementById("sentcheck").checked == true)
      {
        document.getElementById("sentyes").value = "yes";
      }else{
        document.getElementById("sentyes").value = "no";
      }
     
     /*
      fetch(`/sending/`, {
      method: 'POST',
      body: JSON.stringify({
      
      sent: document.getElementById("sentcheck").checked,
      tracking: document.getElementById("tracking").value,
      rewardid: document.getElementById("rewards").value,
                  
    })
    
  })
  */
   
      }


    function detailReward() {
         
          fetch(`/reward/`, {
          method: 'POST',
          body: JSON.stringify({
          rewardid: document.getElementById("rewards").value,
                      
        })
        
      })
      .then(response => response.json())
      .then(reward => {
        document.getElementById("winner").innerHTML = `${reward.user}`;
        document.getElementById("rewardtitle").innerHTML = `${reward.title}`;
        document.getElementById("rewardauthor").innerHTML = `${reward.author}`;
        document.getElementById("rewardnbr").innerHTML = `${reward.id}`;
        document.getElementById("rewardnb").value = `${reward.id}`;
        document.getElementById("rewarddate").innerHTML = `${reward.date}`;
        document.getElementById("winneraddress").innerHTML = `${reward.address}`;
        document.getElementById("tracking").value = `${reward.tracking}`;
      })
        
        
      }

function confirmReward(){

  fetch(`/booklist`)
  .then(response => response.json())
  .then(books => {
  books.forEach(book => {
    
  let opt = document.createElement('option');
  opt.innerHTML = `${book.title}, ${book.author}`;
  opt.value = `${book.id}`;
  document.getElementById("choosereward").append(opt);
  let options = []

document.querySelectorAll('#choosereward > option').forEach((option) => {
    if (options.includes(option.value)) option.remove()
    else options.push(option.value)
})
  
  });
  
  });
  
  document.getElementById("reward").style.display = "block"

}

function saveReward(thisreward) {

   
  document.getElementById("reward").style.display = "none"


      fetch(`/completereward/${thisreward}`, {
      method: 'POST',
        body: JSON.stringify({
          address: document.getElementById("thisaddress").value,
          book :  document.getElementById("choosereward").value,
          
      })
      
    })
    document.getElementById("congrats").style.display = "none"
    document.getElementById("rewardinfosent").style.display = "block"
    
  }

function savedit(thisexcerpt) {

  var text = document.getElementById(`edittext${thisexcerpt}`).value 
    var author = document.getElementById(`editauthor${thisexcerpt}`).value 
    var book = document.getElementById(`editbook${thisexcerpt}`).value 
    document.getElementById(`text${thisexcerpt}`).innerHTML = "&ldquo;" + text + "&rdquo;";
    document.getElementById(`author${thisexcerpt}`).innerHTML = author;
    document.getElementById(`book${thisexcerpt}`).innerHTML = book;
    document.getElementById(`editexcerptform${thisexcerpt}`).style.display = "none";

      fetch(`/edit/${thisexcerpt}`, {
      method: 'POST',
      body: JSON.stringify({
          text: document.getElementById(`edittext${thisexcerpt}`).value,
          author :  document.getElementById(`editauthor${thisexcerpt}`).value,  
          book :  document.getElementById(`editbook${thisexcerpt}`).value,
          genre :  document.getElementById(`editgenre${thisexcerpt}`).value,
      })
      
    })
    
    
  }



function like(thisexcerpt) {


  fetch(`/likes/${thisexcerpt}`)
  .then(response => response.json())
  .then(excerpt => {
    document.getElementById(`this${thisexcerpt}`).innerHTML = `${excerpt.nbr_likes} likes`;
});


    if (document.getElementById( `${thisexcerpt}`).getAttribute('src') == ylike) 
    {
      document.getElementById( `${thisexcerpt}`).src = nolike;
    }else{
      document.getElementById( `${thisexcerpt}`).src = ylike;
    }
    
    if (document.getElementById( `mylike${thisexcerpt}`).getAttribute('src') == ylike) 
    {
      document.getElementById( `mylike${thisexcerpt}`).src = nolike;
    }else{
      document.getElementById( `mylike${thisexcerpt}`).src = ylike;
    }
    

   
}

function navtab(item) {
  var navitem = item.innerHTML;
  var x = document.getElementsByClassName("tab-pane fade show active");
  var y = document.getElementsByClassName("nav-link active");
  for (i = 0; i < x.length; i++) {
  
    x[i].className = "tab-pane fade";
  
} 
for (i = 0; i < y.length; i++) {
  
  y[i].className = "nav-link";
 
} 
  
  document.getElementById(navitem).className = "tab-pane fade show active";

}
function byauthor(item) {

  var thisauthor = item.innerHTML;
 
  var y = document.querySelectorAll('[data-excerpts="all"]');
  
 
for (i = 0; i < y.length; i++) {
  
  if(y[i].dataset.author != `${thisauthor}`){

    y[i].style.display = "none"

  }
 
}

}

function bybook(book) {

  var thisbook = book.innerHTML;
 
  var y = document.querySelectorAll('[data-excerpts="all"]');
  
 
for (i = 0; i < y.length; i++) {
  
  if(y[i].dataset.title != `${thisbook}`){

    y[i].style.display = "none"

  }
 
}

}


function dropdown() {

  
if (document.getElementById("drop").style.display == "block"){

  document.getElementById("drop").style.display = "none"

}else{

  document.getElementById("drop").style.display = "block"
}
 
    

}