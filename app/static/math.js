function upload(input) {
	if(input.files && input.files[0]) {
		var file = input.files[0]
		reader = new FileReader();
		reader.onload = function() {
			document.getElementById('displayImage').setAttribute('src', reader.result);
		}
		reader.readAsDataURL(file);
	}
}