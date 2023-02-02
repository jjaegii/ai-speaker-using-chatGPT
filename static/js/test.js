window.SpeechRecognition =
  window.SpeechRecognition || window.webkitSpeechRecognition;

// stt 인스턴스 생성
const recognition = new SpeechRecognition();
function sttSet() {
  // true면 음절을 연속적으로 인식하나 false면 한 음절만 기록함
  recognition.interimResults = false;
  // 값이 없으면 HTML의 <html lang="en">을 참고합니다. ko-KR, en-US
  recognition.lang = "ko-KR";
  // true means continuous, and false means not continuous (single result each time.)
  // true면 음성 인식이 안 끝나고 계속 됩니다.
  recognition.continuous = true;
  // 숫자가 작을수록 발음대로 적고, 크면 문장의 적합도에 따라 알맞은 단어로 대체합니다.
  // maxAlternatives가 크면 이상한 단어도 문장에 적합하게 알아서 수정합니다.
  recognition.maxAlternatives = 10000;
}
sttSet();

function tts(text) {
  const utterance = new SpeechSynthesisUtterance(text);
  window.speechSynthesis.speak(utterance);
}

let isCalled = false;
recognition.addEventListener("result", (e) => {
  for (let i = e.resultIndex, len = e.results.length; i < len; i++) {
    let transcript = e.results[i][0].transcript;
    console.log(transcript);
    if (transcript == "야") {
      tts("부르셨나요?");
      isCalled = true;
    }
    if (isCalled == true) {
      fetch("http://192.168.0.128:5000/ask", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(transcript),
      })
        .then((response) => response.json())
        .then((data) => tts(data));

      isCalled = false;
    }
  }
});

// 음성인식이 끝나면 자동으로 재시작합니다.
// recognition.addEventListener("end", recognition.start);

// 음성 인식 시작
recognition.start();
