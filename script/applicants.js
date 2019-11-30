const register = async () => {
  let linkedinEmail = document.getElementById('linkedinEmail').value;
  let twitterUsername = await document.getElementById('twitterUsername').value;
  window.localStorage.setItem('twitterUsername',twitterUsername);

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

//convert image to Base64
function getBase64(file,cb){
  var reader = new FileReader();
  reader.readAsDataURL(file);
  reader.onload = function(){
    console.log(reader.result);
    cb(reader.result);
  };
  reader.oneerror = function (error) {
    console.log('Error: ', error);
  }
}

const uploadPhoto = async(data) => {
  await fetch('http://3.227.193.57:10100/users/accounts/photo/'+localStorage.getItem('twitterUsername'),{
    method: 'PUT',
    mode: 'cors',
      headers: {
        'Content-Type':'application/json'
      },
      body: JSON.stringify(data)
  })
}

const uploadButton = async() => {
  var files = await document.getElementById("foto").files;
  var data = {};
  if (files.length > 0){
    getBase64(files[0], function(result){
      data.Photo = result;
      console.log(data.Photo);
      uploadPhoto(data);
      console.log(data);
    })
  }
  else {
    uploadPhoto(data);
  }
}