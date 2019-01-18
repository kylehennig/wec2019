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

function sendMessage(message) {
    // TODO
}

function clientJoin(size) {
    const message = {
        header: "JOIN",
        body: {
            size: size,
            seed: Date.now()
        }
    }
    return sendMessage(message);
}

function clientBoard() {
    const message = {
        header: "BOARD"
    }
    return sendMessage(message);
}

function clientMove(x, y) {
    const message = {
        header: "MOVE",
        body: {
            x: x,
            y: y
        }
    }
    return sendMessage(message);
}
