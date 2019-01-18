window.addEventListener("", () => {
    let lastMessage = null;
    const socket = new WebSocket("ws://localhost:8888/player");
    socket.onopen(() => {
        const message = {
            header: "JOIN",
            body: {
                size: "100"
            }
        }
        socket.send(JSON.stringify(message));
        lastMessage = message.header;
    });
    socket.onmessage((event) => {
        const message = event.data;
        const header = message.header;
        const body = message.body;
        if (body.success === true) {
            if (lastMessage === "BOARD") {
                const board = body.board;
            }
        } else {
            console.alert("Request to server failed.")
        }
    })
});
