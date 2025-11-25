function openChat() {
    const chatBox = document.getElementById("chatbotBox");
    chatBox.classList.add("open");

    // Optional: focus input when chat opens
    const input = document.getElementById("chatInput");
    setTimeout(() => input.focus(), 200);
}


document.addEventListener("DOMContentLoaded", () => {

    const chatBox = document.getElementById("chatbotBox");
    const closeBtn = document.getElementById("closeChat");
    const messagesDiv = document.getElementById("chatMessages");
    const input = document.getElementById("chatInput");
    const suggestions = document.querySelectorAll(".suggestion");

    // Open chat when clicking predefined buttons
    suggestions.forEach(btn => {
        btn.addEventListener("click", () => {
            chatBox.classList.add("open");
            handleSuggestion(btn);
        });
    });

    // Close chat
    closeBtn.addEventListener("click", () => {
        chatBox.classList.remove("open");
    });

    // Send message manually
    input.addEventListener("keydown", (e) => {
        if (e.key === "Enter" && input.value.trim() !== "") {
            sendUserMessage(input.value.trim());
            autoReply(input.value.trim());
            input.value = "";
        }
    });

    function addMessage(text, sender) {
        const msg = document.createElement("div");
        msg.className = sender === "user"
            ? "msg user"
            : "msg bot";
        msg.innerText = text;
        messagesDiv.appendChild(msg);
        messagesDiv.scrollTop = messagesDiv.scrollHeight;
    }

    function sendUserMessage(text) {
        addMessage(text, "user");
    }

    const REPLIES = {
        "Tell me about Yash": "Yash is a B.Tech CSE (AI/ML) student who builds AI tools, full-stack apps, and practical ML projects.",
        "Show projects": "Projects: Chanakya (AI Assistant), Wanderlust, Arka Chatbot, MathSuite, QR/Calc tools.",
        "What skills do you have?": "Skills: Python, Java, C, Django, Node.js, Express, MongoDB, FastAPI, ML, Bootstrap, HTML/CSS.",
        "How to contact Yash?": "Email: yashawasthi854@gmail.com • LinkedIn available above."
    };

    function autoReply(question) {
        setTimeout(() => {
            addMessage(REPLIES[question] || "I don't have an answer for that yet 😄", "bot");
        }, 400);
    }

    function handleSuggestion(btn) {
        const text = btn.innerText;

        sendUserMessage(text);
        autoReply(text);

        btn.style.display = "none";
    }

});
