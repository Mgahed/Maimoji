alert("ugsgs")
const video = document.getElementById('video')

Promise.all([
  faceapi.nets.tinyFaceDetector.loadFromUri('C:\Users\Lenovo\maimoji\src\models'),
  faceapi.nets.faceLandmark68Net.loadFromUri('C:\Users\Lenovo\maimoji\src\models'),
  faceapi.nets.faceRecognitionNet.loadFromUri('C:\Users\Lenovo\maimoji\src\models'),
  faceapi.nets.faceExpressionNet.loadFromUri('C:\Users\Lenovo\maimoji\src\models')
]).then(startVideo)

function startVideo() {
  navigator.getUserMedia(
    { video: {} },
    stream => video.srcObject = stream,
    err => console.error(err)
  )
}
var neutral1 = -1;
var happy1 = -1;
var sad1 = -1;
video.addEventListener('play', () => {
  const canvas = faceapi.createCanvasFromMedia(video)
  document.body.append(canvas)
  const displaySize = { width: video.width, height: video.height }
  faceapi.matchDimensions(canvas, displaySize)
  setInterval(async () => {
    const detections = await faceapi.detectAllFaces(video, new faceapi.TinyFaceDetectorOptions()).withFaceLandmarks().withFaceExpressions()
    const resizedDetections = faceapi.resizeResults(detections, displaySize)
    canvas.getContext('2d').clearRect(0, 0, canvas.width, canvas.height)
    // faceapi.draw.drawDetections(canvas, resizedDetections)
    // faceapi.draw.drawFaceLandmarks(canvas, resizedDetections)
    // faceapi.draw.drawFaceExpressions(canvas, resizedDetections)
    var neutral = detections[0].expressions.neutral
    var happy = detections[0].expressions.happy
    var sad = detections[0].expressions.sad
    if (neutral<=1&&neutral>=0) {
      neutral1 = neutral;
      sessionStorage.setItem("neutral1",neutral1);
    }
    if (happy<=1&&happy>=0) {
      happy1 = happy;
      sessionStorage.setItem("happy1",happy1);
    }
    if (sad<=1&&sad>=0) {
      sad1 = sad;
      sessionStorage.setItem("sad1",sad1);
    }

    console.log("happy : " + happy1);
    console.log("neutral : " + neutral1);
    console.log("sad : " + sad1);
  }, 100)
})
function fn(){
return [neutral1, happy1, sad1];
}
