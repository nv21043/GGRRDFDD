// qr_generator.js

document.getElementById('generate-btn').addEventListener('click', function() {
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    var qrCodeDiv = document.getElementById('qr-code');
    qrCodeDiv.innerHTML = '';

    var qr = new QRCode(qrCodeDiv, {
        text: `username:${username},password:${password}`,
        width: 200,
        height: 200
    });

    // Show download button
    document.getElementById('download-btn').style.display = 'block';
});

document.getElementById('download-btn').addEventListener('click', function() {
    var qrCodeDataUrl = document.getElementsByTagName('canvas')[0].toDataURL('image/png');

    // Create a link element and set its attributes
    var downloadLink = document.createElement('a');
    downloadLink.href = qrCodeDataUrl;
    downloadLink.download = 'qr_code.png';

    // Append the link element to the document body and trigger a click event
    document.body.appendChild(downloadLink);
    downloadLink.click();

    // Remove the link element from the document body
    document.body.removeChild(downloadLink);
});
