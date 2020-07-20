import * as faceapi from 'face-api.js';

// Load models and weights
export async function loadModels() {
  const MODEL_URL = process.env.PUBLIC_URL + '/models';
  await faceapi.loadTinyFaceDetectorModel(MODEL_URL);
  await faceapi.loadFaceLandmarkTinyModel(MODEL_URL);
  await faceapi.loadFaceRecognitionModel(MODEL_URL);
  await faceapi.loadFaceExpressionModel(MODEL_URL);
  // alert(MODEL_URL)
}
var neutral = "-1";
var happy = "-1";
var sad = "-1";
export async function getFullFaceDescription(blob, inputSize = 512) {
  // const detections = await faceapi.detectAllFaces(blob, new faceapi.TinyFaceDetectorOptions()).withFaceLandmarks().withFaceExpressions();
  // const resizedDetections = faceapi.resizeResults(detections, inputSize);
  // var neutral = detections[0].expressions.neutral;
  // console.log(neutral)
  // var happy = detections[0].expressions.happy;
  // var sad = detections[0].expressions.sad;
  // tiny_face_detector options;
  let scoreThreshold = 0.5;
  const OPTION = new faceapi.TinyFaceDetectorOptions({
    inputSize,
    scoreThreshold
  });
  // const useTinyModel = true;

  // fetch image to api
  let img = await faceapi.fetchImage(blob);

  // detect all faces and generate full description from image
  // including landmark and descriptor of each face
  let fullDesc = await faceapi
    .detectAllFaces(img, OPTION)
    .withFaceExpressions();

  console.log(fullDesc)
  try {
    neutral = fullDesc[0].expressions.neutral;
    happy = fullDesc[0].expressions.happy;
    sad = fullDesc[0].expressions.sad;
    sessionStorage.setItem("neutral",neutral)
    sessionStorage.setItem("happy",happy)
    sessionStorage.setItem("sad",sad)
    console.log("neutarl = " + neutral)
    console.log("happy = " + happy)
    console.log("sad = " + sad)
  } catch{ console.log("No Dedection")
  sessionStorage.setItem("neutral",neutral)
  sessionStorage.setItem("happy",happy)
  sessionStorage.setItem("sad",sad)
  console.log("no neutarl = " + neutral)
  console.log("no happy = " + happy)
  console.log("no sad = " + sad)
 }
  return fullDesc;
}

const maxDescriptorDistance = 0.5;
export async function createMatcher(faceProfile) {
  // Create labeled descriptors of member from profile
  let members = Object.keys(faceProfile);
  let labeledDescriptors = members.map(
    member =>
      new faceapi.LabeledFaceDescriptors(
        faceProfile[member].name,
        faceProfile[member].descriptors.map(
          descriptor => new Float32Array(descriptor)
        )
      )
  );

  // Create face matcher (maximum descriptor distance is 0.5)
  let faceMatcher = new faceapi.FaceMatcher(
    labeledDescriptors,
    maxDescriptorDistance
  );
  return faceMatcher;
}
