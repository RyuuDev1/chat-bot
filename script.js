
const chatBox = document.getElementById('chat-box');
const userInput = document.getElementById('user-input');

function appendMessage(sender, message) {
  const msgDiv = document.createElement('div');
  msgDiv.classList.add('message');
  msgDiv.innerHTML = `<strong>${sender}:</strong> ${message}`;
  chatBox.appendChild(msgDiv);
  chatBox.scrollTop = chatBox.scrollHeight;
}

function sendMessage() {
  const message = userInput.value.trim();
  if (message === '') return;

  appendMessage('You', message);
  userInput.value = '';

  // Simulate a response (backend integration will be added later)
  setTimeout(() => {
    appendMessage('Valentine Girl', getBotResponse(message));
  }, 500);
}

function getBotResponse(input) {
  const responses = [
    "Hey you! 💕 I've been waiting for you all day!",
    "Aww, you're so sweet! Tell me more... 😘",
    "You make my heart skip a beat! ❤️",
    "Haha, you're cute! So, what’s on your mind? 😍",
    "I could chat with you forever! 💖"
  ];
  return responses[Math.floor(Math.random() * responses.length)];
}
