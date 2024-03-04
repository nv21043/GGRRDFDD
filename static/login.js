// login.js

function scanQRCode() {
    var video = document.getElementById('qr-video');
    var canvasElement = document.getElementById('qr-canvas');
    var canvas = canvasElement.getContext('2d');

    var qrResult = document.getElementById('qr-result');

    navigator.mediaDevices.getUserMedia({ video: { facingMode: 'environment' } })
        .then(function(stream) {
            video.srcObject = stream;
            video.setAttribute('playsinline', true);
            video.play();

            requestAnimationFrame(tick);
        });

    function tick() {
        if (video.readyState === video.HAVE_ENOUGH_DATA) {
            canvasElement.hidden = false;
            canvasElement.height = video.videoHeight;
            canvasElement.width = video.videoWidth;
            canvas.drawImage(video, 0, 0, canvasElement.width, canvasElement.height);
            var imageData = canvas.getImageData(0, 0, canvasElement.width, canvasElement.height);
            var code = jsQR(imageData.data, imageData.width, imageData.height);

            if (code) {
                qrResult.innerText = code.data;
                // Redirect to SIS login page with extracted username and password
                var credentials = parseQRCode(code.data);
                window.location.href = `https://sis.nvtc.edu.bh/site/login?username=${credentials.username}&password=${credentials.password}`;
            } else {
                qrResult.innerText = 'Scanning QR code...';
                requestAnimationFrame(tick);
            }
        } else {
            requestAnimationFrame(tick);
        }
    }
}

function parseQRCode(data) {
    var parts = data.split(',');
    var username = parts.find(part => part.startsWith('username:')).split(':')[1];
    var password = parts.find(part => part.startsWith('password:')).split(':')[1];
    return { username: username, password: password };
}

document.addEventListener('DOMContentLoaded', function() {
    scanQRCode();
});
