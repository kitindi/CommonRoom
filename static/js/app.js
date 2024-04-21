const answerButton = document.getElementById("answer-btn");
const content = document.getElementById("answer-content");

answerButton.addEventListener("click", (e) => {
  const questionReply = e.target.value;
  console.log(questionReply);
});
