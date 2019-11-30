const createRow = (i, accountName) => {
	let numCell = document.createElement('td');
	numCell.innerText = i;

	let namaCell = document.createElement('td');
	namaCell.innerText = accountName;

	let careerCell = document.createElement('td');
	careerCell.innerHTML = `<span class="label label-info pull-left" data-effect="pop" >Career details</span>`

	let socialCell = document.createElement('td');
	socialCell.innerHTML = `<span class="label label-info pull-left" data-effect="pop" >Social details</span>`

	careerCell.addEventListener('click', () => detailCareer(accountName));
	socialCell.addEventListener('click', () => detailSocial(accountName));
	
	let row = document.createElement('tr');
	row.appendChild(numCell);
	row.appendChild(namaCell);
	row.appendChild(careerCell);
	row.appendChild(socialCell)

	let table = document.getElementById('tabelHR');
	table.appendChild(row);
}

const createTwitterProfile = (i, username, description, status, following, followers) => {
	let numCell = document.createElement('td');
	numCell.innerText = i;

	let usernameCell = document.createElement('td');
	usernameCell.innerText = username;

	let descriptionCell = document.createElement('td');
	descriptionCell.innerText = description;

	let statusCell = document.createElement('td');
	statusCell.innerText = status;

	let followingCell = document.createElement('td');
	followingCell.innerText = following;

	let followersCell = document.createElement('td');
	followersCell.innerText = followers;

	let row = document.createElement('tr');
	row.appendChild(numCell);
	row.appendChild(usernameCell);
	row.appendChild(descriptionCell);
	row.appendChild(statusCell);
	row.appendChild(followingCell);
	row.appendChild(followersCell);

	let table = document.getElementById('tabelTwitterProfile');
	table.appendChild(row);
}

const createTwitterStats = (i, accountAge, accountAverage) => {
	let numCell = document.createElement('td');
	numCell.innerText = i;

	let accountAgeCell = document.createElement('td');
	accountAgeCell.innerText = accountAge;

	let accountAverageCell = document.createElement('td');
	accountAverageCell.innerText = accountAverage;

	let row = document.createElement('tr');
	row.appendChild(numCell);
	row.appendChild(accountAgeCell);
	row.appendChild(accountAverageCell);

	let table = document.getElementById('tabelTwitterStats');
	table.appendChild(row);
}

const createTwitterTweets = (i, tweet1, tweet2, tweet3, tweet4, tweet5) => {
	let numCell = document.createElement('td');
	numCell.innerText = i;

	let tweet1Cell = document.createElement('td');
	tweet1Cell.innerText = tweet1;

	let tweet2Cell = document.createElement('td');
	tweet2Cell.innerText = tweet2;

	let tweet3Cell = document.createElement('td');
	tweet1Cel3.innerText = tweet3;

	let tweet4Cell = document.createElement('td');
	tweet1Cell.innerText = tweet4;

	let tweet5Cell = document.createElement('td');
	tweet1Cell.innerText = tweet5;

	let row = document.createElement('tr');
	row.appendChild(numCell);
	row.appendChild(tweet1Cell);
	row.appendChild(tweet2Cell);
	row.appendChild(tweet3Cell);
	row.appendChild(tweet4Cell);
	row.appendChild(tweet5Cell);

	let table = document.getElementById('tabelTwitterTweets');
	table.appendChild(row);
}


const loadData = async () => {
	let result = await fetch('http://3.227.193.57:8001/users/all');
	let data = await result.json();
	let tabel = document.getElementById('tabelHR');
	
	let i = 1;
	for (let item of data) {
		createRow(i, item.account_name);
		i++;
	}
}

const detailCareer = async (accountID) => {
  let urlPart1 = window.location.href.split('/');
  window.location = urlPart1.splice(0, urlPart1.length-1).join('/') + '/carreer.html';

  window.localStorage.setItem('accountCareer', accountName);
}

const detailSocial = async (accountName) => {
  let urlPart2 = window.location.href.split('/');
  window.location = urlPart2.splice(0, urlPart2.length-1).join('/') + '/social.html';

  window.localStorage.getItem('accountCareer', accountName);
}

const getTwitterProfileByName = async () => {
  let accountName = window.localStorage.getItem('accountNameSocial');
  let result = await fetch('http://3.227.193.57:8002/users/accounts/profile/' + accountName);
  let json = await result.json();
  let tabel = document.getElementById('tabelTwitterProfile');
  tabel.innerHTML = '';
  let i = 1;
  for(let item of json){
  	createTwitterProfile(i, item.account_username, item.account_description, item.account_status, item.account_friends, item.account_followers);
  	i++;
  }
}

const getTwitterStatsByName = async () => {
  let accountName = window.localStorage.getItem('accountName');
  let result = await fetch('http://3.227.193.57:8001/users/accounts/stats/' + accountName);
  let json = await result.json();
  let tabel = document.getElementById('tabelTwitterStats');
  tabel.innerHTML = '';
  let i = 1;
  for(let item of json){
  	createTwitterStats(i, item.account_age, item.account_username);
  	i++;
  }
}

const getTwitterTweetsByName = async () => {
  let accountName = window.localStorage.getItem('accountName');
  let result = await fetch('http://3.227.193.57:8001/users/accounts/tweets/' + accountName);
  let json = await result.json();
  let tabel = document.getElementById('tabelTwitterTweets');
  tabel.innerHTML = '';
  let i = 1;
  for(let item of json){
  	createTwitterTweets(i, item.tweet1, item.tweet2, item.tweet3, item.tweet4, item.tweet5);
  	i++;
  }
}
