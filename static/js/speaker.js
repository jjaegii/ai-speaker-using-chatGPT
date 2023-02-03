const start_btn = document.getElementById("start_btn");
start_btn.addEventListener("click", () => {
  tts('안녕하세요 반갑습니다. 저를 부르시려면 "야" 라고 불러주세요');
  q.hidden = false;
  a.hidden = false;
});

const q = document.getElementById("q");
const a = document.getElementById("a");

const synth = window.speechSynthesis;

function tts(text) {
  if (!window.speechSynthesis) {
    alert("음성 재생을 지원하지 않는 브라우저입니다.");
  }

  const utterance = new SpeechSynthesisUtterance(text);
  const lang = "ko-KR";

  utterance.onerror = function (e) {
    console.log("error", e);
  };

  utterance.lang = lang;
  utterance.pitch = 1;
  utterance.rate = 1;

  console.log(text);
  window.speechSynthesis.speak(utterance);
  a.innerText = "A:" + text;
}

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
  recognition.continuous = false;
  // 숫자가 작을수록 발음대로 적고, 크면 문장의 적합도에 따라 알맞은 단어로 대체합니다.
  // maxAlternatives가 크면 이상한 단어도 문장에 적합하게 알아서 수정합니다.
  recognition.maxAlternatives = 10000;
}
sttSet();

let isCalled = false;
recognition.addEventListener("result", (e) => {
  for (let i = e.resultIndex, len = e.results.length; i < len; i++) {
    let transcript = e.results[i][0].transcript;
    console.log(transcript);
    q.innerText = "Q:" + transcript;
    if ((transcript == "야" || transcript == " 야") && isCalled == false) {
      tts("네 부르셨나요?");
      isCalled = true;
    }
    if (transcript != "야" && isCalled == true) {
      fetch("/ask", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(transcript),
      })
        .then((response) => response.json())
        .then((data) => {
          console.log(data["answer"]);
          tts(data["answer"]);
        })
        .then(() => (isCalled = false));
    }
  }
});

// 음성인식이 끝나면 자동으로 재시작합니다.
recognition.addEventListener("end", recognition.start);

// 음성 인식 시작
recognition.start();
