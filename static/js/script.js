class Chatbox {
    constructor() {
        this.args = {
            openButton: document.querySelector('.chatbox__button button'),
            chatBox: document.querySelector('.chatbox__support'),
            sendButton: document.querySelector('.send__button'),
            inputField: document.querySelector('.chatbox__footer input'),
            chatMessages: document.querySelector('.chatbox__messages'),
        };
        this.state = false;
        this.messages = [];
    }

    display() {
        const { openButton, chatBox, sendButton, inputField } = this.args;

        openButton.addEventListener('click', () => this.toggleState(chatBox));

        sendButton.addEventListener('click', () => this.onSendButton());

        inputField.addEventListener("keyup", (event) => {
            if (event.key === "Enter") {
                this.onSendButton();
            }
        });
    }

    toggleState(chatBox) {
        this.state = !this.state;
        chatBox.classList.toggle('chatbox--active', this.state);
    }

    onSendButton() {
        const { inputField } = this.args;
        let userMessage = inputField.value.trim();
        if (userMessage === "") return;

        this.messages.push({ name: "User", message: userMessage });
        this.updateChatText();

        inputField.value = "";

        fetch("/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: userMessage }),
        })
            .then(response => response.json())
            .then(data => {
                this.messages.push({ name: "Bot", message: data.response });
                this.updateChatText();
            })
            .catch(error => console.error("Error:", error));
    }

    updateChatText() {
        const { chatMessages } = this.args;
        chatMessages.innerHTML = this.messages.map(msg => {
            return `<div class="messages__item ${msg.name === "User" ? "messages__item--right" : "messages__item--left"}">${msg.message}</div>`;
        }).join('');

        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
}

document.addEventListener("DOMContentLoaded", () => {
    const chatbox = new Chatbox();
    chatbox.display();
});
