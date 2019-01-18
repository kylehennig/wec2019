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
    function sendMessage(message) {
        return new Promise((resolve, reject) => {
            if (!open) {
                socket.onopen = () => {
                    socket.send(JSON.stringify(message));
                    open = true;
                };
            } else {
                socket.send(JSON.stringify(message));
            }

            socket.onmessage = (event) => {
                const message = JSON.parse(event.data);
                const body = message.body;
                resolve(body);
            };

            setTimeout(() => {
                reject("Request took more than one minute.")
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
