const createRow = (i, accountName) => {
	let numCell = document.createElement('td');
	numCell.innerText = i;

	let namaCell = document.createElement('td');
	namaCell.innerText = accountName;

	let careerCell = document.createElement('td');
	careerCell.innerHTML = `<span class="label label-info pull-left" data-effect="pop" >Career details</span>`

	let socialCell = document.createElement('td');
	socialCell.innerHTML = `<span class="label label-success pull-left" data-effect="pop" >Social details</span>`

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

const loadData = async () => {
	let result = await fetch('http://3.227.193.57:8001/users/all');
	let data = await result.json();
	
	let i = 1;
	for (let item of data) {
		createRow(i, item.account_name);
		i++;
	}
}

const detailCareer = async (accountName) => {
  window.localStorage.setItem('accountCareer', accountName);
  let tes = localStorage.getItem('accountCareer');

  let hasil = await fetch('http://3.227.193.57:8001/users/all');
  let data = await hasil.json()
  for(let item of data){
  	let accountNama = window.localStorage.getItem('accountCareer');
  	if(accountNama === item.account_name){
  		let account_id = item.account_id;
  		window.localStorage.setItem('accountIDCareer',account_id );
  	}
  }

  let urlPart1 = window.location.href.split('/');
  window.location = urlPart1.splice(0, urlPart1.length-1).join('/') + '/carreer.html';
}

const detailSocial = async (accountName) => {
  window.localStorage.setItem('accountSocial', accountName);
  let tes = localStorage.getItem('accountSocial');

  let hasil = await fetch('http://3.227.193.57:8001/users/all');
  let data = await hasil.json()
  for(let item of data){
  	let accountNama = window.localStorage.getItem('accountSocial');
  	if(accountNama === item.account_name){
  		let account_id = item.account_id;
  		window.localStorage.setItem('accountIDSocial',account_id );
  	}
  }

  let urlPart2 = window.location.href.split('/');
  window.location = urlPart2.splice(0, urlPart2.length-1).join('/') + '/social.html';

}

const getLinkedinGeneral = async () => {
  let accountIDCareer = window.localStorage.getItem('accountIDCareer');
  console.log(accountIDCareer);
  let result = await fetch('http://3.227.193.57:8001/users/accounts/general');
  let json = await result.json();
  for(let item of json){
  	if(item.account_id == accountIDCareer){
		let accountIdElem = document.getElementById('account_id');
	    let accountNameElem = document.getElementById('account_name');
	    let accountTitleElem = document.getElementById('account_title');
	    let accountRegionElem = document.getElementById('account_region');

	    accountIdElem.innerHTML = item.account_id;
	    accountNameElem.innerHTML = item.account_name;
	    accountTitleElem.innerHTML = item.account_title;
	    accountRegionElem.innerHTML = item.account_region;
	}
  }
}

const getLinkedinEducation = async () => {
  let accountID = window.localStorage.getItem('accountIDCareer');
  console.log(accountID);
  let result = await fetch('http://3.227.193.57:8001/users/accounts/education');
  let json = await result.json();
  for(let item of json){
  	if(item.account_id == accountID){
		let institutionElem = document.getElementById('institution');
        let educationTitleElem = document.getElementById('educationTitle');

        institutionElem.innerHTML = item.education_institution;
        educationTitleElem.innerHTML = item.education_title;
	}
  }
}


const getLinkedinWorkplace = async () => {
  let accountID = window.localStorage.getItem('accountIDCareer');
  console.log(accountID);
  let result = await fetch('http://3.227.193.57:8001/users/accounts/workplace');
  let json = await result.json();
  for(let item of json){
  	if(item.account_id == accountID){
		let currentWorkplaceElem = document.getElementById('currentWorkplace');
		let previousWorkplaceElem = document.getElementById('previousWorkplace');

		currentWorkplaceElem.innerHTML = item.workplace1;
		previousWorkplaceElem.innerHTML = item.workplace2;
	}
  }
}

const getTwitterProfile = async () => {
  let accountID = window.localStorage.getItem('accountIDSocial');
  let result = await fetch('http://3.227.193.57:8001/applicants');
  let json = await result.json();
  for(let item of json){
  	if(item.linkedin_email == accountID){
  		let hasil = await fetch('http://3.227.193.57:8002/users/accounts/profile/' + item.twitter_username);
  		let results = await hasil.json();
  		let output = results;

  		let usernameElem = document.getElementById('username');
        let namaElem = document.getElementById('nama');
        let descriptionElem = document.getElementById('deskripsi');
        let statusElem = document.getElementById('status');
        let followingElem = document.getElementById('following');
        let followersElem = document.getElementById('followers');
        let photoElem = document.getElementById('photo');

        usernameElem.innerHTML = output.account_username;
        namaElem.innerHTML = output.account_name;
        descriptionElem.innerHTML = output.account_description;
        statusElem.innerHTML = output.account_status;
        followingElem.innerHTML = output.account_friends;
        followersElem.innerHTML = output.account_followers;
        photoElem.innerHTML = "<img src="+output.photo+" alt=No Photo"+'""'+" border="+3+" height="+200+" width="+200+"></img>";
  	}
  }
}


const getTwitterStats = async () => {
  let accountID = window.localStorage.getItem('accountIDSocial');
  let result = await fetch('http://3.227.193.57:8001/applicants');
  let json = await result.json();
  for(let item of json){
  	if(item.linkedin_email == accountID){
  		let hasil = await fetch('http://3.227.193.57:8002/users/accounts/stats/' + item.twitter_username);
  		let results = await hasil.json();
  		let output = results;

  		let ageElem = document.getElementById('account_age');
        let averageElem = document.getElementById('average_tweets');

        ageElem.innerHTML = output.account_age;
        averageElem.innerHTML = output.average_tweets;
  	}
  }
}

const getTwitterTweets = async () => {
  let accountID = window.localStorage.getItem('accountIDSocial');
  let result = await fetch('http://3.227.193.57:8001/applicants');
  let json = await result.json();
  for(let item of json){
  	if(item.linkedin_email == accountID){
  		let hasil = await fetch('http://3.227.193.57:8002/users/accounts/tweets/' + item.twitter_username);
  		let results = await hasil.json();
  		let output = results;
  		
		let tweet1Elem = document.getElementById('tweet1');
        let tweet2Elem = document.getElementById('tweet2');
        let tweet3Elem = document.getElementById('tweet3');
        let tweet4Elem = document.getElementById('tweet4');
        let tweet5Elem = document.getElementById('tweet5');

        tweet1Elem.innerHTML = output.tweet1;
        tweet2Elem.innerHTML = output.tweet2;
        tweet3Elem.innerHTML = output.tweet3;
        tweet4Elem.innerHTML = output.tweet4;
        tweet5Elem.innerHTML = output.tweet5;

	  }
  	}
  }
