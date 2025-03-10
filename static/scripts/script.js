function validate_input(num1, num2) {
	num1 = parseInt(num1);
	num2 = parseInt(num2);
	
	if ((Number.isFinite(num1)) && (Number.isFinite(num2))) {
		return true;
	}
	else {
		return false;
	}
}


// validate input from html using the function, then make an API call if input is all good
function add_submit() {
	// get the input from the html page
	var num1 = document.getElementById('num1').value;
	var num2 = document.getElementById('num2').value;
	
	
	// if the input is valid
	if (validate_input(num1, num2)) {
		// parse the numbers
		num1 = parseInt(num1);
		num2 = parseInt(num2);
		
		// make an API call
		const url = api_url;
		
		fetch(url, 
		{
			method: "POST",
			body: JSON.stringify
			({num1: num1, num2: num2}),
			headers: {
				"Content-type": "application/json",
			},
		})
		
		.then(response => response.json())
		
		.then(json => {
			console.log(JSON.stringify(json));
			const obj = JSON.parse(JSON.stringify(json));
			console.log(obj.output);
			alert(obj.output);
		})
		
	}
	// input is not valid
	else {
		alert("input is not valid");
	}
	
	
	

	
}
