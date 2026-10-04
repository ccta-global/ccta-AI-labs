const messageInput = document.getElementById("message-input");
const sendButton = document.getElementById("send-button");
const chatContainer = document.getElementById("chat-container");


// Conversation history
let messages = [
    {
        role: "system",
        content: "You are a helpful assistant."
    }
];


function addMessage(role, text) {

    const messageDiv = document.createElement("div");

    messageDiv.classList.add(
        "message",
        role
    );


    const label = document.createElement("div");

    label.classList.add("message-label");

    label.textContent =
        role === "user"
            ? "You"
            : "Assistant";


    const textDiv = document.createElement("div");

    textDiv.classList.add("message-text");

    textDiv.textContent = text;


    messageDiv.appendChild(label);

    messageDiv.appendChild(textDiv);

    chatContainer.appendChild(messageDiv);


    chatContainer.scrollTop =
        chatContainer.scrollHeight;


    return textDiv;
}


async function sendMessage() {

    const message =
        messageInput.value.trim();


    if (!message) {
        return;
    }


    // Display user message
    addMessage("user", message);


    // Add user message to conversation
    messages.push({
        role: "user",
        content: message
    });


    // Clear input
    messageInput.value = "";


    // Disable button
    sendButton.disabled = true;

    sendButton.textContent = "Thinking...";


    try {

        const response = await fetch(
            "/chat",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    messages: messages
                })
            }
        );


        const data = await response.json();


        if (!response.ok) {

            throw new Error(
                data.error || "Something went wrong"
            );

        }


        // Display assistant response
        addMessage(
            "assistant",
            data.response
        );


        // Save assistant response
        messages.push({
            role: "assistant",
            content: data.response
        });


    } catch (error) {

        addMessage(
            "assistant",
            "Error: " + error.message
        );

    }


    sendButton.disabled = false;

    sendButton.textContent = "Send";

    messageInput.focus();
}


// Send when button is clicked
sendButton.addEventListener(
    "click",
    sendMessage
);


// Send when Enter is pressed
messageInput.addEventListener(
    "keydown",
    function(event) {

        if (
            event.key === "Enter" &&
            !event.shiftKey
        ) {

            event.preventDefault();

            sendMessage();
        }

    }
);