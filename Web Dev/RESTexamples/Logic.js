function GetBreed(){

	var settings = {
  "url": "https://api.thecatapi.com/v1/breeds/search?q=" + document.getElementById("catTerm").value,
  "method": "GET",
  "timeout": 0,
  "headers": {
    "x-api-key": "YOURKEY",
    "Cookie": "YOURCOOKIE"
			},
					};

	$.ajax(settings).done(function (response) {
		if (response[0] == undefined){
			console.log("nada");
		}
		else{
	  console.log(response[0]['wikipedia_url']);
	  document.getElementById("CatLink").href= response[0]['wikipedia_url']
	  document.getElementById("CatLink").text = document.getElementById("catTerm").value
		}
	})
};

function returnBtcVal(){
	var settings = {
  "url": "https://coinlib.io/api/v1/coin?pref=USD&symbol=BTC&key=YOURKEY",
  "method": "GET",
	"timeout": 0,
	"headers": {
    "Cookie": "YOURCOOKIE"
  },}
	
	$.ajax(settings).done(function (response) {
		

	  if (response['price'] == undefined){
			console.log("nada");
		}
		else{
	  document.getElementById("btcprice").innerHTML = "Value in USD: " + response['price'];
		}
	})
}

function ReturnPokemon(){
	var settings = {
  "url": "https://pokeapi.co/api/v2/pokemon/" + document.getElementById("Pokename").value.toLowerCase(),
  "method": "GET",
  "timeout": 0,
  "headers": {
    "Cookie": "YOUR COOKIE"
	},
	};

	$.ajax(settings).done(function (response) {
	var x = "Pokemon " + document.getElementById("Pokename").value + " has the following moves:"
	function getMoves(val){
		x = x + " " + val['move']['name'] + ",";
	}
	response['moves'].forEach(getMoves);
	console.log(x);
	var y = x.replace(/.$/,".");
	document.getElementById("PokeMoves").innerHTML = y;
	});
}