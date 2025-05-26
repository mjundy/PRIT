let qrContentInput = document.getElementById("qr-content");
	let qrGenerationForm = 
	document.getElementById("qr-generation-form");
	let qrCode;
	
	function generateQrCode(qrContent) {
	return new QRCode("qr-code", {
		text: qrContent,
		width: 256,
		height: 256,
		colorDark: "#000000",
		colorLight: "#ffffff",
		correctLevel: QRCode.CorrectLevel.H,
	});
	}
	
	// Event listener for form submit event
	qrGenerationForm.addEventListener("submit", function (event) {
	// Prevent form submission
	event.preventDefault();
	let qrContent = qrContentInput.value;
	if (qrCode == null) {
		
		// Generate code initially
		qrCode = generateQrCode(qrContent);
	} else {
		
		// If code already generated then make 
		// again using same object
		qrCode.makeCode(qrContent);
	}
	});