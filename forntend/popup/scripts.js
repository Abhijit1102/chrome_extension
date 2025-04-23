const apiUrl = "https://chromeextensionbackend-production.up.railway.app/api/v1";
function showInitialMessage() {
  appendMessage("bot", "Please wait until content is uploaded...");
}

document.addEventListener("DOMContentLoaded", () => {
  showInitialMessage();
  const closeBtn = document.getElementById("closeBtn");
  const sendBtn = document.getElementById("sendBtn");
  const userInput = document.getElementById("userInput");

  // ✅ Attach button listeners
  closeBtn.addEventListener("click", closeChat);
  sendBtn.addEventListener("click", sendMessage);
  userInput.addEventListener("keypress", function (e) {
    if (e.key === "Enter") {
      sendMessage();
    }
  });

  // ✅ Get active tab URL and send to background for processing
  chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
    if (tabs.length > 0) {
      const activeTab = tabs[0];
      console.log("🌐 Active Tab URL:", activeTab.url);
      chrome.runtime.sendMessage({
        type: "process_url",
        url: activeTab.url,
      });
    } else {
      console.error("❌ No active tab found.");
    }
  });
});

// ✅ Listen for background messages (processed URL results)
chrome.runtime.onMessage.addListener((message) => {
  if (message.type === "url_processed") {
    console.log("📩 Message from background:", message.message);
    appendMessage("bot", message.message);
  }
});

// ✅ Send user input to chatbot and get response
function sendMessage() {
  const userInput = document.getElementById("userInput");
  const userInputValue = userInput.value.trim();
  if (userInputValue === "") return;

  appendMessage("user", userInputValue);
  userInput.value = "";

  getBotReply(userInputValue);
}

// ✅ Append message to chat window
function appendMessage(type, message) {
  const chatBox = document.getElementById("chat-box");
  const messageDiv = document.createElement("div");
  messageDiv.classList.add("chat-message", type);
  messageDiv.innerText = message;
  chatBox.appendChild(messageDiv);
  chatBox.scrollTop = chatBox.scrollHeight; // Auto-scroll to bottom
}

// ✅ Get chatbot reply from backend
async function getBotReply(userInput) {
  const url = `${apiUrl}/get_answer`;

  const data = {
    query_text: userInput,
  };

  try {
    const response = await fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });

    if (!response.ok) {
      const errorResult = await response.json();
      console.error("❌ API Error:", errorResult);
      appendMessage("bot", `Error: ${errorResult.detail || "Unknown error"}`);
      return;
    }

    const result = await response.json();
    const botReply = result?.answer || "I'm not sure.";
    console.log("🤖 Bot Reply:", botReply);
    appendMessage("bot", botReply);
  } catch (error) {
    console.error("❌ Error:", error);
    appendMessage("bot", "Oops! Something went wrong.");
  }
}

async function closeChat() {
  if (window.confirm("Are you sure you want to close this window?")) {
    window.close(); 
  } else {
    console.log("🔄 Chat window not closed.");
  }
}

window.addEventListener("beforeunload", (event) => {
  event.preventDefault();
  event.returnValue = "";
});
