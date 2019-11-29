const register = async () => {
  let linkedinEmail = document.getElementById('linkedinEmail').value;
  let twitterUsername = document.getElementById('twitterUsername').value;


  let response = await fetch('http://3.227.193.57:8001/applicants');
  let data = await response.json();
  var validate = true;
  for (let item of data) {
    if (item.linkedin_email == linkedinEmail || item.twitter_username == twitterUsername) {
    	console.log(item.linkedin_email);
      validate = false;
      break;
    }
  }
  
  if (validate == false){
    alert('Sudah pernah apply sebelumnya');
  }
  else{
    let linkedinEmailElem = document.getElementById('linkedinEmail');
    let twitterUsernameElem = document.getElementById('twitterUsername');

    console.log(JSON.stringify({
	     "linkedin_email": linkedinEmailElem.value ,
	     "twitter_username": twitterUsernameElem.value})
	   )

  await fetch(`http://3.227.193.57:8001/applicants`, {
	 method: 'POST',
	 mode:'cors',
	    headers: {
	      'Content-Type': 'application/json'
	    },
	    body: JSON.stringify({
	      "linkedin_email": linkedinEmailElem.value ,
	      "twitter_username":twitterUsernameElem.value,
	    })
	  })
    }
  };