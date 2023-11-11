<script>
  import { io } from "socket.io-client";
  let socket = io();
  let response = "";
  socket.on("connect", function () {
    console.log("Connected to server");
  });

  socket.on("disconnect", function () {
    console.log("Disconnected from server");
  });

  socket.on("message", function (data) {
    console.log("Received message:", data);
    response = data;
  });
  let text = "";

  function sendMessage() {
    socket.emit("message", text);
  }
</script>

<input
  class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
  type="text"
  id="messageInput"
  placeholder="Enter a message"
  bind:value={text}
/>
<button
  class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
  on:click={sendMessage}>Send</button
>
{#if response}
  <div>Response from sample api:</div>
  <div>{JSON.stringify(response)}</div>
{/if}
