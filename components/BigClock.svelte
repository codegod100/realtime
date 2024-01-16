<script>
  import { emojisplosion, emojisplosions } from "emojisplosion";
  let time = new Date();

  // Update the time every second
  setInterval(() => {
    time = new Date();
  }, 1000);
  let hours = time.getHours();
  let period = "AM";

  if (hours >= 12) {
    period = "PM";
  }

  if (hours > 12) {
    hours -= 12;
  } else if (hours === 0) {
    hours = 12;
  }
  // emojisplosion();
  let audio = new Audio();
  audio.src = "/static/flask.mp3";
</script>

<div class="clock-widget roll-in">
  <div>
    Clock made with  <button
      class="heart"
      on:click={() => {
        emojisplosion({ emojis: ["💖"] });
        audio.play();
      }}>💖</button
    > in <b>svelte</b> using <b>devbox</b>
  </div>
  <div class="clock text-6xl text-center">
    {hours}:{time.getMinutes() < 10
      ? "0" + time.getMinutes()
      : time.getMinutes()}:{time.getSeconds() < 10
      ? "0" + time.getSeconds()
      : time.getSeconds()}
  </div>
</div>

<style>
  .clock {
    font-family: "Digital-7 Mono";
    /* color: #ff0000;
    background-color: #000000; */
    padding: 20px;
    border-radius: 10px;
  }
  .clock-widget {
    position: fixed;
    bottom: 0;
    right: 0;
  }

  .roll-in {
    animation: roll-in-animation 2s cubic-bezier(0, 0, 1, 1) 0s 1 normal both
      running;
  }

  @keyframes roll-in-animation {
    0% {
      opacity: 0;
      transform: translate(-100%, 0) rotate(-120deg);
    }

    100% {
      opacity: 1;
      transform: translate(0, 0) rotate(0deg);
    }
  }
</style>
