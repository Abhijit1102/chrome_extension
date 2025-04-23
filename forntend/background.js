chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.type === "process_url") {
    console.log("Processing URL in background:", message.url);
    processActiveTabURL(message.url);
  }
});

async function processActiveTabURL(tabUrl) {
  try {
    const response = await fetch("https://chromeextensionbackend-production.up.railway.app/api/v1/process_url", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ url: tabUrl })
    });

    if (!response.ok) {
      throw new Error("Failed to process URL.");
    }

    const data = await response.json();
    console.log("Tab content processed successfully:", data);

    chrome.runtime.sendMessage({
      type: "url_processed",
      message: "Tab content processed successfully."
    });
  } catch (error) {
    console.error("Error processing URL:", error);
    chrome.runtime.sendMessage({
      type: "url_processed",
      message: "Failed to process tab content."
    });
  }
}