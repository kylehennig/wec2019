/**
 * Provides a way to communicate with the server.
 *
 * Usage:
 *   client.join(size)
 *   client.board()
 *   client.move(x, y)
 */
const client = (function () {
    const socket = new WebSocket("ws://localhost:8888/player");
    let open = false;
    socket.onopen = () => {
        open = true;
    };

    function sendMessage(message) {
        return new Promise((resolve, reject) => {
            socket.onmessage = (event) => {
                const message = JSON.parse(event.data);
                const body = message.body;
                resolve(body);
            };

            if (!open) {
                setTimeout(() => {
                    if (!open) {
                        throw new Error("Could not connect to socket.");
                    }
                    socket.send(JSON.stringify(message))
                }, 1000);
            } else {
                socket.send(JSON.stringify(message));
            }

            setTimeout(() => {
                reject("Request took more than one minute.");
            }, 60000);
        });
    }

    function join(size) {
        const message = {
            header: "JOIN",
            body: {
                size: size,
                seed: Date.now()
            }
        }
        return sendMessage(message);
    }

    function board() {
        const message = {
            header: "BOARD"
        }
        return sendMessage(message);
    }

    function move(x, y) {
        const message = {
            header: "MOVE",
            body: {
                x: x,
                y: y
            }
        }
        return sendMessage(message);
    }

    return {
        join: join,
        board: board,
        move: move
    }
})();
